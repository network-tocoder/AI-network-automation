"""
This module contains the implementation of the Tenant class, which
represents a tenant in the tenant management system.

The Tenant class provides methods for suspending, activating, and
deleting a tenant, as well as checking the tenant's state and managing identity users.

"""

from http import HTTPStatus
import logging
from typing import Union, Optional, List
import requests
from tm_export_schemes.crud_requests import TMTenantUpdate
from tm_export_schemes.crud_response import (
    TMSuspendTenantResponse, BaseTenantResponse,
    TMActivateTenantResponse, TMDeleteTenantResponse, TMUpdateTenantResponse,
    BaseTenant)
from tenant_management_integrations.schemas.common import TenantMgmtException, Service
from tenant_management_integrations_e2e.tm_e2e_connector import TME2EConnector, TokenProviders
from tenant_management_integrations_e2e.constants import generate_auth_headers
from utils.common_schemas import OperationFlag
from tenant_services.errors import UnexpectedEverestResponseStatus
from tenant_services.verify_everest_response import _verify_response
from tenant_management_integrations.identity_mgmt.utilities import get_role_id_by_name


class Tenant:
    """
    Represents a tenant in the system.

    Attributes:
        logger (logging.Logger): The logger object used for logging.
        connector (TME2EConnector): The connector object used to 
            communicate with the tenant management service.
        tenant_id (str): The ID of the tenant.
        tenant_name (Optional[str]): The name of the tenant.
        base (Optional[BaseTenant]): The base tenant object.
    """

    def __init__(self, connector: TME2EConnector, tenant_id: str) -> None:
        """
        Initializes a Tenant object.

        Args:
            connector (TME2EConnector): The connector object used to
                communicate with the tenant management service.
            tenant_id (str): The ID of the tenant.
        """
        self.logger: logging.Logger = logging.getLogger(__name__)
        self.connector: TME2EConnector = connector
        self.id: str = tenant_id
        self.base: Optional[BaseTenant]

    def suspend(self, wait=False) -> Union[BaseTenantResponse, Exception]:
        """
        Suspends the tenant.

        Returns:
            Union[BaseTenantResponse, Exception]: The response from
                the tenant management service or an exception if an error occurs.
        """
        response: Union[TMSuspendTenantResponse, None]
        status: str = OperationFlag.suspending.value
        if wait:
            status: str = OperationFlag.suspended.value

        try:
            response = self.connector.suspend_tenant(
                self.id, sync_wait=wait)
            return _verify_response(self.logger, response, status)
        except TenantMgmtException as e:
            self.logger.error("Error while suspending tenant. Error: %s", e)
            return e

    def activate(self, wait=False) -> Union[BaseTenantResponse, Exception]:
        """
        Activates the tenant.

        Returns:
            Union[BaseTenantResponse, Exception]: The response from the
                tenant management service or an exception if an error occurs.
        """
        try:
            response: Union[TMActivateTenantResponse, None]
            response = self.connector.activate_tenant(
                self.id, sync_wait=wait)
            return _verify_response(self.logger, response,
                                    OperationFlag.active.value)
        except TenantMgmtException as e:
            self.logger.error("Error while activating tenant. Error: %s", e)
            return e

    def delete(self) -> Union[BaseTenantResponse, Exception]:
        """
        Deletes the tenant.

        Returns:
            Union[BaseTenantResponse, Exception]: The response from the tenant
                management service or an exception if an error occurs.
        """

        response: Union[TMDeleteTenantResponse, None]
        status: str = OperationFlag.deleting.value
        if not self.is_tenant_in_state(OperationFlag.suspended.value):
            self.suspend(wait=True)

        try:
            response = self.connector.delete_tenant(self.id)
            return _verify_response(self.logger, response, status)
        except TenantMgmtException as e:
            self.logger.error("Error while deleting tenant. Error: %s", e)
            return e

    def is_tenant_deleted(self) -> Union[bool, Exception]:
        """
        Checks if the tenant is deleted.

        Returns:
            Union[bool, Exception]: True if the tenant is deleted, False
                otherwise. Returns an exception if an error occurs.
        """
        try:
            response: Union[BaseTenantResponse, None]
            response = self.connector.get_tenant(self.id)
            if response is not None and (
                response.status == OperationFlag.deleted.value or
                response is None
            ):
                return True
            return False
        except TenantMgmtException as e:
            self.logger.error("Error while checking if tenant is deleted. Error: %s", e)
            return e

    def is_tenant_in_state(self, tenant_state: str) -> Union[bool, Exception]:
        """
        Checks if the tenant is in the specified state.

        Args:
            tenant_state (str): The state to check for.

        Returns:
            Union[bool, Exception]: True if the tenant is in the specified
                state, False otherwise. Returns an exception if an error occurs.
        """
        try:
            response: Union[BaseTenantResponse, None]
            response = self.connector.get_tenant(self.id)
            _verify_response(self.logger, response, tenant_state)
            return True
        except UnexpectedEverestResponseStatus:
            return False
        except TenantMgmtException as e:
            self.logger.error("Error while getting tenant state. Error: %s", e)
            return e

    def _is_service_deleted(self, service: Service) -> Union[bool, Exception]:
        """
        Checks if the specified service is deleted.

        Args:
            service (Service): The service to check for.

        Returns:
            Union[bool, Exception]: True if the service is deleted, False
                otherwise. Returns an exception if an error occurs.
        """
        try:
            response: Union[BaseTenantResponse, None] = self.connector.get_tenant(self.id)
            return response is None or response.services.get(service) is None
        except TenantMgmtException as e:
            self.logger.error("Error while checking if service {service} is deleted. Error: %s", e)
            return e

    def is_conjur_state_deleted(self) -> Union[bool, Exception]:
        """
        Checks if the Conjur state is deleted.

        Returns:
            bool: True if the Conjur state is deleted, False otherwise.
        """
        return self._is_service_deleted(Service.SECRETS_MANAGER)

    def create_identity_user(self, username: str, password: str, email: str,
                                display_name: Optional[str] = '') -> str:
        """
        Creates an identity user.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
            email (str): The email address of the user.
            display_name (Optional[str], optional): The display name of the user. Defaults to ''.

        Returns:
            str: The ID of the created user.
        """
        return self.connector.create_identity_user(username, password,
                                                    email, self.id,
                                                    display_name)

    def assign_role_to_identity_user(self, username: str, role_name: str) -> None:
        """
        Assigns a role to an identity user.

        Args:
            username (str): The username of the user.
            role_name (str): The NAME of the role to assign.
        """
        token_providers = TME2EConnector._get_token_providers(self.connector, self.id)
        role_id = get_role_id_by_name(logger=self.logger, access_token=token_providers.tenant_access_token, tenant_endpoint=token_providers.tenant_endpoint, role_name=role_name)
        self.connector.assign_role_to_identity_user(username, role_id, self.id)

    def login_identity_user(self, username: str, password: str) -> str:
        """
        Logs in an identity user.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            str: The access token of the logged-in user.
        """
        return self.connector.login_identity_user(username, password, self.id)

    def get_user_suffix(self) -> str:
        """
        Retrieves the user suffix pattern from the tenant management service.

        Args:
            tenant_id (str): The ID of the tenant.

        Returns:
            str: The user suffix in the following pattern cyberark.cloud.{number}
        """
        token_providers: TokenProviders = self.connector._get_token_providers(self.id)
        list_user_url: str = f'{token_providers.tenant_endpoint}/cdirectoryservice/GetUsers'
        response: requests.Response
        response = requests.post(list_user_url,
                                headers=generate_auth_headers(token_providers.tenant_access_token),
                                verify=True, timeout=30)
        if not response.status_code == HTTPStatus.OK:
            self.logger.error('Failed to retrieve user from Tenant management service. '
                                'Responded with: %s.text}.', response.text)
            raise TenantMgmtException(
                f'Tenant management service did not return a successful response. '
                f'Expected {HTTPStatus.OK}, got {response.status_code}'
            )
        user: str = response.json()['Result']['Results'][0]['Row']['Name']
        return user.partition("@")[2]

    def send_action_conjur_service(self, action: str, tenant_name: str, tenant_id: str) -> None:
        """
        Sends an action to the Conjur service.

        Args:
            action (str): The action to send.
            tenant_name (str): The name of the tenant.
            tenant_id (str): The ID of the tenant.
        """
        try:
            params: dict = {'name': tenant_name, 'services_to_' + action: [Service.SECRETS_MANAGER]}
            service_request: TMTenantUpdate = TMTenantUpdate(**params)
            response: Optional[TMUpdateTenantResponse]
            response = self.connector.update_tenant(update_tenant_details=service_request,
                                                    tenant_id=tenant_id
                                                    )
            tenant_status: OperationFlag = OperationFlag.activating if action == 'activate' else OperationFlag.updating
            _ = _verify_response(self.logger, response, tenant_status.value)
            self.connector._wait_for_status(status_list=[
                    OperationFlag.active,
                    OperationFlag.service_error
                ], tenant_id=tenant_id)
        except TenantMgmtException as e:
            self.logger.error("Error while %s conjur service. Error: %s", action, e)
