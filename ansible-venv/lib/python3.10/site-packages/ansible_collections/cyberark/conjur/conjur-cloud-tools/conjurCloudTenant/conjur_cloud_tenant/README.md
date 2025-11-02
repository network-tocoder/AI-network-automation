# Conjur Cloud Tenant
Conjur Cloud Tenant is a tool that will allow the creation of Cloud tenants for CI/CD pipeline use.

## Local Development

To build the Docker image for local development, follow these steps:

1. Make sure you have Docker installed on your machine.

2. Create a `.netrc` file in the root directory of your project. This file should contain your Conjur credentials in the following format:
    ```
    machine cyberark.jfrog.io
    login <artifactory-username>
    password <artifactory-token>
    ```

3. Obtain the `moderna.crt` file from cloud artifactory and place it in the root directory of your project.

4. Open a terminal and navigate to the root directory of your project.

5. Run the following command to build the Docker image:
    ```bash
    docker build -t <image-name> .
    ```
    Replace `<image-name>` with the desired name for your Docker image.

6. Once the image is built, you can run a container using the following command:
    ```bash
    docker run --rm -it --entrypoint bash <image-name>
    ```
    Replace `<image-name>` with the name of the Docker image you built

7. The Ec2 instance that runs this already has permission, but for local development you'll have to export AWS keys that are able to assume the required role.

    ```
    export AWS_ACCESS_KEY_ID="<aws-access-key>"
    export AWS_SECRET_ACCESS_KEY="<aws-secret-access-key>"
    export AWS_SESSION_TOKEN="<aws-token>"
    export AWS_DEFUALT_REGION="us-east-1"
    ```

8. Edit the everest `e2e_utils.py` to assume the AWS role with the correct permissions to create tenants `InstanceReadJenkinsExecutorHostFactoryToken`. (To easily find the file, you can run `conjur_cloud_tenant.py` and you'll receive an error that will link you to the file that should be modified.)

    ```
    # pylint: disable=no-name-in-module,no-self-argument, import-error
    from datetime import datetime
    from typing import Optional

    import boto3
    import cachetools
    from aws_lambda_powertools.utilities.parameters import GetParameterError
    from botocore.exceptions import ClientError, ParamValidationError
    from dateutil.relativedelta import relativedelta
    from everest_env_utils.env_mapping import ROOT_DOMAIN, AwsEnv, is_gov_cloud
    from everest_env_utils.idaptive_env_mapping import IDAPTIVE_ENV_URLS, IDAPTIVE_TENANT_NAME
    from infra_automation_utils.random_utils import random_string
    from mypy_boto3_ssm import SSMClient
    from pydantic import ValidationError
    from tenant_management_integrations.schemas.common import AssumeResponse, TenantMgmtException

    from tenant_management_integrations_e2e.constants import CACHE_SIZE, CACHE_TTL, TM_SESSION_DURATION

    DEFAULT_EXPIRATION_TIMEFRAME_IN_DAYS = 2


    def get_idaptive_tenant_fqdn(tenant_id: str, tm_environment: AwsEnv) -> str:
        idaptive_env_url = IDAPTIVE_ENV_URLS[tm_environment]
        return f'{tenant_id}.my.{idaptive_env_url}'


    def get_idaptive_fqdn(tm_environment: AwsEnv) -> str:
        return get_idaptive_tenant_fqdn(IDAPTIVE_TENANT_NAME[tm_environment], tm_environment)


    def get_idaptive_base_url_by_profile(tm_environment: AwsEnv) -> str:
        return f'https://{get_idaptive_fqdn(tm_environment)}'


    def get_tenant_mgmt_app_url(env: AwsEnv) -> str:
        root_domain = ROOT_DOMAIN[env]
        if is_gov_cloud():
            return f'https://service.management.{root_domain}'
        return f'https://ui.service.management.{root_domain}'


    @cachetools.cached(cachetools.TTLCache(maxsize=CACHE_SIZE, ttl=CACHE_TTL))
    def get_boto3_client(aws_service: str, role_arn: str, external_id: str, region: str,
                        internal_role_arn: Optional[str] = None) -> boto3.client:
        sts_client = boto3.client('sts')

        if internal_role_arn is not None:
            assume_role_response = sts_client.assume_role(
                    RoleArn="arn:aws:sts::601277729239:role/InstanceReadJenkinsExecutorHostFactoryToken",
                    RoleSessionName='InitialAssumeRoleSession',
                    DurationSeconds=900,
                )

            sts_infra_client = boto3.client('sts', region_name="us-east-1", aws_access_key_id=assume_role_response['Credentials']['AccessKeyId'],
                                        aws_secret_access_key=assume_role_response['Credentials']['SecretAccessKey'],
                                        aws_session_token=assume_role_response['Credentials']['SessionToken'])
            print(f'Assumed INFRA role: {assume_role_response["AssumedRoleUser"]["Arn"]}')

            try:
                assume_role_response = sts_infra_client.assume_role(
                    RoleArn=internal_role_arn,
                    RoleSessionName=f'InitialAssumeRoleSession{random_string(16)}',
                    DurationSeconds=900,
                )
                sts_tenant_client = boto3.client('sts', region_name="us-east-1", aws_access_key_id=assume_role_response['Credentials']['AccessKeyId'],
                                        aws_secret_access_key=assume_role_response['Credentials']['SecretAccessKey'],
                                        aws_session_token=assume_role_response['Credentials']['SessionToken'])
                print(f'Assumed TENANT role: {assume_role_response["AssumedRoleUser"]["Arn"]}')
            except (ClientError, ParamValidationError, ValidationError) as exc:
                error_str = 'unable to assume initial role'
                raise TenantMgmtException(error_str) from exc

        # Call the assume_role method of the STSConnection object and pass the role ARN and a role session name.
        try:
            assumed_role_object = sts_tenant_client.assume_role(
                RoleArn=role_arn,
                DurationSeconds=TM_SESSION_DURATION,
                RoleSessionName=f'AssumeRoleSession{random_string(24)}',  # this should be unique and set to expire ASAP
                ExternalId=external_id,
            )
            print(f'Assumed FINAL role: {assumed_role_object["AssumedRoleUser"]["Arn"]}')
            assume_res = AssumeResponse(**assumed_role_object)
        except (ClientError, ParamValidationError, ValidationError) as exc:
            error_str = 'unable to assume role'
            raise TenantMgmtException(error_str) from exc

        return boto3.client(
            service_name=aws_service,
            region_name=region,
            aws_secret_access_key=assume_res.Credentials.SecretAccessKey,
            aws_access_key_id=assume_res.Credentials.AccessKeyId,
            aws_session_token=assume_res.Credentials.SessionToken,
        )


    def get_caller_aws_account() -> str:
        sts_client = boto3.client('sts')
        response = sts_client.get_caller_identity()
        account_id = response.get('Account', '')
        return str(account_id)


    def generate_default_test_tenant_expiration_date() -> str:
        default_expiration_date = datetime.date(datetime.now() + relativedelta(days=DEFAULT_EXPIRATION_TIMEFRAME_IN_DAYS)).strftime('%Y-%m-%d')
        return default_expiration_date


    def get_param_token(client: SSMClient, param_key: str, is_secured: bool = False) -> Optional[str]:
        # pylint: disable=no-value-for-parameter
        try:
            ret = client.get_parameter(Name=param_key, WithDecryption=is_secured)
        except GetParameterError as exc:
            raise TenantMgmtException(f'failed getting parameter {param_key} (WithDecryption={is_secured}).') from exc

        if ret:
            return ret.get('Parameter', {}).get('Value')
        return None

    ```

9. Run and test code


## Adding and Updating Poetry Dependencies

To add or update dependencies using Poetry, follow these steps:

1. Open a terminal and navigate to the root directory of your project.

2. Run the following command to add a new dependency:
    ```bash
    poetry add <dependency-name>
    ```

    Replace `<dependency-name>` with the name of the package you want to add. Poetry will automatically update your `pyproject.toml` and `poetry.lock` files.

3. To update an existing dependency, use the following command:
    ```bash
    poetry update <dependency-name>
    ```

    Replace `<dependency-name>` with the name of the package you want to update. Poetry will fetch the latest version of the package and update your `pyproject.toml` and `poetry.lock` files.

4. After adding or updating dependencies, you can run the following command to install or update them:
    ```bash
    poetry install
    ```

    This command will install or update all the dependencies listed in your `pyproject.toml` file.

5. To update all the dependencies in your project to their latest versions, you can use the following command:
    ```bash
    poetry update
    ```

    Running `poetry update` without specifying a package name will update all the dependencies in your project to their latest versions.
