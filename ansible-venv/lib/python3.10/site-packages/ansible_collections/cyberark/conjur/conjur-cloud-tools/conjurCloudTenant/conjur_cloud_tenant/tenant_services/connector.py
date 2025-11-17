"""
This module provides a connector for managing tenants in Everest.

It contains the `TenantConnector` class, which allows creating new tenants,
retrieving existing tenants, and performing other operations related to tenant management.

Example usage:
    connector = TenantConnector(trusting_account_role_arn, ssm_role_arn, external_id, region, everest_running_env)
    new_tenant = connector.create_new_tenant(tenant_name_prefix, region, tenant_type, customer_type)
    existing_tenants = connector.get_all_existing_tenants()
    existing_tenant = connector.get_existing_tenant(tenant_id)
"""

import logging
import uuid
import datetime
from time import sleep
from typing import Any, Dict, List, Union, Optional
from pydantic import HttpUrl
from tenant_management_integrations.schemas.common import TenantMgmtException, Service
from tenant_management_integrations_e2e.tm_e2e_connector import TME2EConnector
from utils.common_schemas import ContactDetails, OperationFlag
from tm_export_schemes.crud_requests import TMCreateTenant
from tm_export_schemes.crud_response import TMCreateTenantResponse, BaseTenantResponse
from everest_env_utils.env_mapping import AwsEnv, ROOT_DOMAIN
from tenant_services.verify_everest_response import _verify_response
from tenant_services.tenant import Tenant
from tenant_services.errors import (TenantServiceError, BaseTenantResponseNone,
                                        UnexpectedEverestResponseStatus,
                                        EverestServiceError)


class TenantConnector:
    """
    A class that represents a connector for managing tenants in Everest.

    Args:
        ssm_role_arn (str): The ARN of the SSM role.
        external_id (str): The external ID.
        region (str): The region.
        everest_running_env (str): The running environment in Everest.

    Attributes:
        logger (Logger): The logger instance.
        ssm_role_arn (str): The ARN of the SSM role.
        external_id (str): The external ID.
        region (str): The region.
        everest_running_env (AwsEnv): The running environment in Everest.
        connector (TME2EConnector): The connector instance.

    """

    def __init__(
            self, ssm_role_arn: str,
            external_id: str, region: str, everest_running_env: str,
            internal_role_arn: Optional[str] = None
        ) -> None:
        """
        Initializes the Connector object.

        Args:
            ssm_role_arn (str): The ARN of the SSM role.
            external_id (str): The external ID.
            region (str): The AWS region.
            everest_running_env (str): The running environment of Everest.

        Returns:
            None
        """
        self.logger: logging.Logger = logging.getLogger(__name__)
        self.ssm_role_arn: str = ssm_role_arn
        self.external_id: str = external_id
        self.region: str = region
        self.everest_running_env: AwsEnv = AwsEnv[everest_running_env.upper()]
        self.internal_role_arn = internal_role_arn

        self.connector: TME2EConnector = TME2EConnector(
            logger=self.logger, ssm_role_arn=self.ssm_role_arn,
            external_id=self.external_id, tm_environment=self.everest_running_env,
            region=self.region, internal_role_arn=self.internal_role_arn
        )

    def create_new_tenant(
        self, tenant_name_prefix: str,
        tenant_type: str, customer_type: str,
        extra_fields: Optional[Dict[str, Dict[str, Any]]] = None
    ) -> Optional[Tenant]:
        """
        Creates a new tenant in the Everest system.

        Args:
            tenant_name_prefix (str): The prefix to be used in the tenant name.
            tenant_type (str): The type of the tenant.
            customer_type (str): The type of the customer.

        Returns:
            Tenant: The created tenant object if
                successful

        Raises:
            TenantMgmtException: If there is an error while creating the tenant.
        """
        create_event_details: ContactDetails = ContactDetails(
            name='Conjops',
            email='conj_ops@cyberark.com',
            phone='+1-617-765-7979',
        )

        tenant_uuid = str(uuid.uuid4())[:6]
        tenant_name = f"{tenant_name_prefix}-{tenant_uuid}"
        tenant_url = f"https://{tenant_name}.{ROOT_DOMAIN[self.everest_running_env]}"
        tenant_subdomain_url: HttpUrl = HttpUrl(tenant_url, scheme='https')
        tomorrow: str = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        tenant_details: TMCreateTenant = TMCreateTenant(
            contact_details=create_event_details, # type: ignore
            region='Ireland',
            name=tenant_name,
            tenant_type=tenant_type,
            customer_type=customer_type,
            customer_name=tenant_name,
            tenant_subdomain = tenant_subdomain_url,
            size=1,
            services=[Service.SECRETS_MANAGER],
            rnd_group="Conjur Cloud",
            expiration_date=tomorrow,
            sf_tenant_id=None,
            extra_fields=extra_fields,
            sfdc_url=None,
            customer_success_manager=None,
            customer_id=None,
            non_platform_services=None,
            services_data=None,
            login_name='Conjops'
        )

        try:
            # sync_wait is set to False, otherwise it will reach a timeout
            # window which disrupts the exposed failure status from returning an object.
            response: TMCreateTenantResponse = self.connector.create_tenant(
                create_tenant_details=tenant_details,
                sync_wait=False,
                expose_failure_status=True,
            )
            verified_response = _verify_response(self.logger, response)
            tenant : Tenant = Tenant(self.connector, verified_response.id)
        except UnexpectedEverestResponseStatus as e:
            self.logger.error("Unexpected Everest response status. Error: %s", e)
            raise e

        return tenant


    def get_all_existing_tenants(self) -> List[Tenant]:
        """
        Retrieves all existing tenants from the connector.

        Returns:
            A list of Tenant objects representing the existing tenants.
        """
        existing_tenants: List[Tenant] = []
        all_tenants: List[BaseTenantResponse] = self.connector.get_all_tenants()
        for tenant in all_tenants:
            create_tenant = Tenant(self.connector, tenant.id)
            create_tenant.base = tenant
            existing_tenants.append(create_tenant)
        return existing_tenants


    def get_existing_tenant(self, tenant_id: str) -> Optional[Tenant]:
        """
        Retrieves an existing tenant based on the provided tenant ID.

        Args:
            tenant_id (str): The ID of the tenant to retrieve.

        Returns:
            Tenant: An instance of the Tenant class representing the retrieved tenant.
        """
        try:
            existing_tenant: Optional[BaseTenantResponse] = self.connector.get_tenant(tenant_id)
            verified_existing_tenant = _verify_response(self.logger, existing_tenant)
        except TenantMgmtException as e:
            self.logger.error("Error while getting tenant. Error: %s", e)
            raise e

        tenant = Tenant(self.connector, verified_existing_tenant.id)
        tenant.base = verified_existing_tenant
        return tenant


    def wait_for_status(self, status_list: List[OperationFlag], tenant_id: str) -> Optional[Tenant]:
        is_requested_status: bool = False
        retries_num: int = 80

        while not is_requested_status and (retries_num > -1):
            tenant_response = self.get_existing_tenant(tenant_id=tenant_id)
            self.logger.info(f"Tenant Status: {tenant_response.base.status}")
            if tenant_response:
                is_requested_status = any(status.value == tenant_response.base.status for status in status_list)
            if is_requested_status:
                return tenant_response
            retries_num -= 1
            sleep(10)

        self.logger.exception(f"Final Status: {tenant_response.base.status}")
        raise TenantServiceError(f"Failed to meet requested tenant status")
