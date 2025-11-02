import logging
from boto3.session import Session
from aws_web_services.session import AwsSession
from boto3.exceptions import Boto3Error
from botocore.exceptions import ClientError

class AwsSts:
    """
    This class provides methods to interact with AWS Security Token Service (STS).
    It allows you to retrieve the ARN (Amazon Resource Name) of the caller identity.

    Example usage:
    session = boto3.Session(profile_name='my_profile')
    sts = AwsSts(session)
    role_arn = sts.get_role_arn()
    print(role_arn)
    """
    def __init__(self, session: Session) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)
        #self._sts_client: Session.client.STSClient = session.client('sts')
        self._sts_client = session.client('sts')

    def get_role_arn(self) -> str:
        """
        Retrieves the ARN (Amazon Resource Name) of the caller identity.

        Returns:
            str: The ARN of the caller identity.
        """
        response = self._sts_client.get_caller_identity()
        return response['Arn']

    def assum_role(self):
        try:
            response = self._sts_client.assume_role(
                RoleArn='arn:aws:iam::601277729239:role/InstanceReadJenkinsExecutorHostFactoryToken',
                RoleSessionName='InstanceReadJenkinsExecutorHostFactoryToken'
            )
        except Boto3Error as e:
            print(f"Couldn't assume role: {e}")
            return None
        except ClientError as e:
            print(f"Couldn't assume role: {e}")
            return None

        credentials = response['Credentials']

        session: Session = AwsSession()
        session.aws_access_key_id = credentials['AccessKeyId']
        session.aws_secret_access_key = credentials['SecretAccessKey']
        session.aws_session_token = credentials['SessionToken']
        assumed_session = session.get_session()
        return assumed_session

