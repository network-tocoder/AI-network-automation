"""
This module provides a function to verify the response received from Everest.
    It checks if the response is None, if the response status is 'SERVICE_ERROR',
    or if the response status is unexpected. It raises appropriate exceptions
    in each case. If the response passes all the checks, it is considered verified
    and returned.

    Example usage:
    logger = logging.getLogger(__name__)
    response = get_everest_response()
    tenant_state = 'ACTIVE'
    verified_response = _verify_response(logger, response, tenant_state)
"""
from logging import Logger
from typing import Union
from tm_export_schemes.crud_response import BaseTenantResponse
from tenant_services.errors import (BaseTenantResponseNone,
                                        UnexpectedEverestResponseStatus,
                                        EverestServiceError)

def _verify_response(logger: Logger, response: Union[BaseTenantResponse, None],
                     tenant_state: str = None) -> BaseTenantResponse:
    """
    Verify the response received from Everest.

    Args:
        logger (Logger): The logger object for logging messages.
        response (Union[BaseTenantResponse, None]): The response received from Everest.
        tenant_state (str, optional): The expected tenant state. Defaults to None.

    Returns:
        BaseTenantResponse: The verified response.

    Raises:
        BaseTenantResponseNone: If the response is None.
        EverestServiceError: If the response status is 'SERVICE_ERROR'.
        UnexpectedEverestResponseStatus: If the response status is unexpected.
    """
    if response is None:
        logger.exception("Everest response is None")
        raise BaseTenantResponseNone("Everest response is None")
    if response.status == 'SERVICE_ERROR':
        logger.error(f"Got SERVICE_ERROR tenant state: {response}")
        raise EverestServiceError("Got SERVICE_ERROR tenant state")
    if tenant_state is not None and response.status != tenant_state:
        raise UnexpectedEverestResponseStatus(f"Unexpected Everest response status '{response.status}'")
    return response
