"""
This module provides functionality to create
    a new tenant and save the tenant details to a JSON file.
"""

import argparse
import json
import logging.config
import logging
import yaml
import random
import string
import uuid
import os
from datetime import datetime
from boto3.session import Session
from aws_web_services.session import AwsSession
from tenant_services.tenant import Tenant
from tenant_services.connector import TenantConnector
from utils.common_schemas import OperationFlag
from typing import Optional
from tenant_services.errors import TenantServiceError

with open('logger.yml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser("conjur_cloud_tenant.py")
parser.add_argument("--pamsh", help="Whether to configure for PAM Self-Hosted tenant", type=str, default=False, const=True, nargs='?')
parser.add_argument("--cleanup", help="Whether or not to cleanup expired tenants", type=str, default=False, const=True, nargs='?')
parser.add_argument("--delete", help="Delete a tenant by ID", type=str)

# Global variable to store the parsed arguments
# Ignore any other arguments passed
ARGS, _ = parser.parse_known_args()
# AWS Region environmet variable is needed on everest import or it will fail
SESSION: Session = AwsSession().get_session()
CONNECTOR: TenantConnector = TenantConnector(
    region=SESSION.region_name,
    ssm_role_arn="arn:aws:iam::710725424037:role/JenkinsTenmanTrustManagerMaster-ssm-US-EAST-1",
    external_id="f0431762-797b-4976-82e4-ced4306bf5cb",
    everest_running_env="integration",
    internal_role_arn="arn:aws:iam::238637036211:role/test-tm-get-secret-from-ssm-role-conjur"
)

def main():
    if ARGS.delete:
        delete_tenant()
        return
    if ARGS.cleanup:
        cleanup_tenants()
        logger.info("Expired tenants have been cleaned up. Exiting...")
        return

    logger.info("Creating a new tenant")
    tenant: Tenant = create_tenant()
    logger.info(f"Tenant {tenant.id} has been created successfully.")

    logger.info(f"Waiting for tenant {tenant.id} to become active.")
    try:
        tenant: Tenant = wait_for_tenant_status(tenant)
    except TenantServiceError as e:
        logger.exception(f"An exception occured while waiting for tenant status.")
        logger.info(f"Deleting tenant {tenant.id}")
        # This will delete the failed tenant, however, if the tenant is in
        # an activating state, it cannot be deleted and will remain in this
        # state until someone on the backend deletes it.
        ARGS.delete = tenant.id
        delete_tenant()
        raise e
    logger.info(f"Configuring tenant: {tenant.id}")
    setup_tenant(tenant)
    logger.info("Writing tenant details to file.")
    write_tenant_to_file(tenant)


def create_tenant() -> Tenant:
    """
    Entry point of the program.
    
    This function creates a new tenant and saves the tenant details to a JSON file.
    """

    if ARGS.pamsh:
        return CONNECTOR.create_new_tenant(
            tenant_name_prefix="conjops",
            tenant_type="POC",
            customer_type="INTERNAL",
            extra_fields={'secrets_manager': {'tenant_type': 'pam_self_hosted'}}
        )

    return CONNECTOR.create_new_tenant(
        tenant_name_prefix="conjops",
        tenant_type="TESTING",
        customer_type="INTERNAL",
    )


def wait_for_tenant_status(tenant: Tenant) -> Optional[Tenant]:
    return CONNECTOR.wait_for_status(
        status_list=[
            OperationFlag.active,
        ], tenant_id=tenant.id)


def setup_tenant(tenant: Tenant):
    conjur_cloud_admin_password = os.environ.get('CONJUR_CLOUD_ADMIN_PASS')
    tenant_username = create_admin_user(tenant=tenant, username='conjurops', password=conjur_cloud_admin_password)
    # Confirm the new user authentication
    _ = tenant.login_identity_user(username=tenant_username, password=conjur_cloud_admin_password)

    # Update the login_name to reflect the new user
    tenant.base.login_name = tenant_username


def write_tenant_to_file(tenant: Tenant):
    tenant_dict = tenant_to_dict(tenant)
    # Add the Conjur Cloud URL to the tenant dictionary
    subdomain_parts = tenant.base.tenant_subdomain.split('.')
    conjur_cloud_url = f"{subdomain_parts[0]}.secretsmgr.{'.'.join(subdomain_parts[1:])}"
    tenant_dict['conjur_cloud_url'] = conjur_cloud_url

    # Save the tenant details to a JSON file
    with open('/everest/tenant.json', 'x', encoding='utf-8') as file_obj:
        json.dump(tenant_dict, file_obj, ensure_ascii=False, indent=4)


def delete_tenant():
    tenant = CONNECTOR.get_existing_tenant(ARGS.delete)
    if tenant.base.name.startswith("conjops-") and tenant.base.contact_details.email == "conj_ops@cyberark.com":
        try:
            tenant.delete()
        except Exception as e:
            logger.exception(f"An exception occured while DELETING tenant {tenant.id}")
            raise e
        logger.info(f"Tenant {tenant.id} has been deleted.")


def cleanup_tenants():
    today = datetime.now().strftime("%Y-%m-%d")
    tenants = CONNECTOR.get_all_existing_tenants()
    for tenant in tenants:
        if tenant.base.name.startswith("conjops-") and tenant.base.contact_details.email == "conj_ops@cyberark.com":
            expire = datetime.strptime(tenant.base.expiration_date, "%Y-%m-%d")
            if expire < datetime.strptime(today, "%Y-%m-%d"):
                try:
                    tenant.delete()
                except Exception as e:
                    logger.error(f"An error occured while DELETING tenant {tenant.id}")
    logger.info("Expired tenants have been cleaned up.")


def create_admin_user(tenant: Tenant, username: str, password: str) -> tuple[str, str]:
    """
    Create a new admin user for the tenant.

    This function generates a random password for the admin user and creates a new user with the generated password.
    The admin user is assigned the roles of 'System Administrator' and 'Secrets Manager – Conjur Cloud Admin'.

    Returns:
        A tuple containing the username and password of the created admin user.
    """
    # Unable to update the password of the default user that's created with the tenant so a new user is created.
    # Unable to access the the default user's one time password link that's sent to the user's email.
    tenant_username = f"{username}@{tenant.get_user_suffix()}"
    tenant.create_identity_user(
        username=tenant_username,
        password=password,
        email='conj_ops@cyberark.com',
        display_name='Conjurops'
    )
    tenant.assign_role_to_identity_user(username=tenant_username,
                                               role_name='System Administrator')
    tenant.assign_role_to_identity_user(username=tenant_username,
                                               role_name='Secrets Manager – Conjur Cloud Admin')
    return tenant_username


def tenant_to_dict(tenant_object: Tenant) -> dict:
    """
    Convert a tenant object to a dictionary.

    Args:
        tenant_object (Tenant): The tenant object to convert to a dictionary.

    Returns:
        dict: The tenant object as a dictionary.
    """
    tenant_dict = {}
    for key, value in tenant_object.__dict__.items():
        match key:
            case 'logger':
                continue
            case 'connector':
                continue
            case 'base':
                for key, value in value.__dict__.items():
                    match key:
                        case 'contact_details':
                            tenant_dict[key] = value.__dict__
                        case 'identity_information':
                            tenant_dict[key] = value.__dict__
                        case 'creation_time':
                            continue
                        case 'last_updated':
                            continue
                        case _:
                            tenant_dict[key] = value
            case _:
                tenant_dict[key] = value
    return tenant_dict

if __name__ == "__main__":
    main()
