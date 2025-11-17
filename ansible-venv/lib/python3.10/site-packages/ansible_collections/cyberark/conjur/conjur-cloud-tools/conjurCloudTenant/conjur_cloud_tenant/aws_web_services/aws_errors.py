class ProfileNotFoundError(Exception):
    """Raised when the AWS profile doesn't exist"""
    pass

class NoCredentialsError(Exception):
    """Raised when no AWS credentials exist on the caller host"""
    pass