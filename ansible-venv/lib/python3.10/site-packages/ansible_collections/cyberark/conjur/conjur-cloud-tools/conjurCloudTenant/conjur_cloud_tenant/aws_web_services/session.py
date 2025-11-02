from boto3.session import Session
from aws_web_services.aws_errors import ProfileNotFoundError, NoCredentialsError
import logging
from typing import Optional
import botocore.exceptions

class AwsSession:
    """
    Represents an AWS session.

    Attributes:
        logger (logging.Logger): The logger instance for logging messages.
        profile (Optional[str]): The profile name for the AWS session.

    """

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.profile: Optional[str] = None
        self.aws_access_key_id: Optional[str] = None
        self.aws_secret_access_key: Optional[str] = None
        self.aws_session_token: Optional[str] = None

    def get_session(self) -> Session:
        """
        Get the AWS session.

        Returns:
            Session: The AWS session object.

        Raises:
            ProfileNotFoundError: If the profile is not found or if credentials are not available.
        """
        if self.aws_access_key_id and self.aws_secret_access_key and self.aws_session_token:
            try:
                self.logger.info("Returning assumed session.")
                return Session(aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key, aws_session_token=self.aws_session_token)
            except botocore.exceptions.NoCredentialsError as error:
                self.logger.exception("Unable to locate credentials")
                raise NoCredentialsError("Unable to locate credentials") from error

        if self.profile is None:
            try:
                self.logger.info("Returning caller's default session.")
                return Session()
            except botocore.exceptions.NoCredentialsError as error:
                self.logger.exception("Unable to locate credentials")
                raise NoCredentialsError("Unable to locate credentials") from error

        try:
            self.logger.info("Gathering AWS Session based on caller profile.")
            return Session(profile_name=self.profile)
        except botocore.exceptions.ProfileNotFound as error:
            self.logger.exception("AWS Profile doesn't exist.")
            raise ProfileNotFoundError("AWS Profile doesn't exist.") from error