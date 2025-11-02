class BaseTenantResponseNone(Exception):
    """Raised when the BaseTenantResponse is None"""
    pass

class UnexpectedEverestResponseStatus(Exception):
    """Raised when the response status does not match the tenant state"""
    pass

class EverestServiceError(Exception):
    """Raised when the response status is SERVICE_ERROR"""
    pass

class TenantServiceError(Exception):
    """Raised when an error occurs in the tenant service"""
    pass
