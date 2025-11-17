#!/bin/bash

# This script is used to authenticate a tenant in Conjur Cloud.
# It takes command line arguments to specify the authentication details and performs the necessary steps to retrieve the required tokens.
# The script also builds a Docker image if it is not already present.

# Set git toplevel path variable
GIT_TOPLEVEL_PATH=$(git rev-parse --show-toplevel)
TOP_CONJUR_CLOUD_TENANT_PATH="${GIT_TOPLEVEL_PATH}/conjurCloudTenant"
CONJUR_CLOUD_TENANT_PATH="${GIT_TOPLEVEL_PATH}/conjurCloudTenant/conjur_cloud_tenant"
AUTH_TENANT_PATH="${TOP_CONJUR_CLOUD_TENANT_PATH}/tenant_authentication"

# Parse command line arguments
# The script uses a while loop to iterate through the command line arguments and assigns the corresponding values to variables.
# The supported arguments include --identity-url, --username, --password, --conjur-url, --identity-token, --conjur-token, and --conjur-edge.
# If an invalid argument is provided, the script displays an error message and exits.
# The shift command is used to move to the next argument.
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        --identity-url)
            IDENTITY_URL="$2"
            shift
            ;;
        --username)
            USERNAME="$2"
            shift
            ;;
        --password)
            PASSWORD="$2"
            shift
            ;;
        --conjur-url)
            CONJUR_URL="$2"
            shift
            ;;
        --identity-token)
            IDENTITY_TOKEN="$2"
            shift
            ;;
        --conjur-token)
            CONJUR_TOKEN="$2"
            shift
            ;;
        --edge-name)
            EDGE_NAME="$2"
            shift
            ;;
        *)
            echo "Invalid argument: $1"
            exit 1
            ;;
    esac
    shift
done

# Function to build Docker image
build_docker_image() {
    # Build Docker image if not already present
    # The function checks if the Docker image "auth-tenant:latest" is already present.
    # If it is not present, it uses the Docker build command to build the image using the Dockerfile in the AUTH_TENANT_PATH directory.
    if [[ "$(docker images -q auth-tenant:latest 2> /dev/null)" == "" ]]; then
        pushd "${AUTH_TENANT_PATH}" > /dev/null || exit
            docker build \
            -f Dockerfile \
            -t auth-tenant \
            .
        popd > /dev/null || exit
    fi
}

# Function to retrieve identity token
get_identity_token() {
    # Allow for optional summon command
    summon_cmd=$1

    # The function runs a Docker container using the auth-tenant image and passes the necessary arguments to retrieve the identity token.
    # The identity token is stored in the variable "identity_token".
    $summon_cmd \
        docker run \
            -e CONJUR_CLOUD_ADMIN_PASS \
            auth-tenant:latest \
            --identity-url="$IDENTITY_URL" \
            --username="$USERNAME" \
            --password="$PASSWORD"
}

# Function to retrieve synchronizer credentials
get_synchronizer_creds() {
    # The function runs a Docker container using the auth-tenant image and passes the necessary arguments to retrieve the synchronizer credentials.
    # The credentials are stored in the variable "synchronizer_creds".
    docker run \
        auth-tenant:latest \
        --conjur-url="$CONJUR_URL" \
        --conjur-token="$CONJUR_TOKEN"
}

# Function to create Conjur Edge
create_conjur_edge() {
    # The function runs a Docker container using the auth-tenant image and passes the necessary arguments to create a Conjur Edge.
    # The Conjur Edge token is stored in the variable "conjur_edge".
    docker run \
        auth-tenant:latest \
        --conjur-url="$CONJUR_URL" \
        --conjur-token="$CONJUR_TOKEN" \
        --conjur-edge="$EDGE_NAME"
}

# Function to retrieve Conjur token
get_conjur_token() {
    # The function runs a Docker container using the auth-tenant image and passes the necessary arguments to retrieve the Conjur token.
    # The Conjur token is stored in the variable "conjur_token".
    docker run \
        auth-tenant:latest \
        --conjur-url="$CONJUR_URL" \
        --identity-token="$IDENTITY_TOKEN"
}

# Function to process identity token call
process_identity_token_call() {
    # The function checks if the PASSWORD variable is empty.
    # If it is empty, it uses the "summon" command with the secrets.yml file and environment variable "ci" to retrieve the identity token.
    # Otherwise, it retrieves the identity token without using the "summon" command.
    # If the identity token is not retrieved successfully, an error message is displayed and the script exits.
    # Otherwise, the identity token is printed and the script exits with a success status.
    if [[ -z "${PASSWORD+""}" ]]; then
        identity_token=$(get_identity_token "summon -f ${CONJUR_CLOUD_TENANT_PATH}/secrets.yml -e ci")
    else
        identity_token=$(get_identity_token)
    fi
    if [[ -z "$identity_token" ]]; then
        echo "Failed to retrieve Identity token." >&2
        exit 1
    fi

    echo "${identity_token}"
    exit 0
}

# Function to process Conjur token call
process_conjur_token_call() {
    # The function retrieves the Conjur token using the get_conjur_token function.
    # If the Conjur token is not retrieved successfully, an error message is displayed and the script exits.
    # Otherwise, the Conjur token is printed and the script exits with a success status.
    conjur_token=$(get_conjur_token)
    if [[ -z "$conjur_token" ]]; then
        echo "Failed to retrieve Conjur token." >&2
        exit 1
    fi

    echo "${conjur_token}"
    exit 0
}

# Function to process Conjur Edge call
process_conjur_edge_call() {
    # The function creates a Conjur Edge using the create_conjur_edge function.
    # If the Conjur Edge token is not retrieved successfully, an error message is displayed and the script exits.
    # Otherwise, the Conjur Edge token is printed and the script exits with a success status.
    conjur_edge=$(create_conjur_edge)
    if [[ -z "$conjur_edge" ]]; then
        echo "Failed to retrieve Conjur Edge token." >&2
        exit 1
    fi
    echo "${conjur_edge}"
    exit 0
}

# Function to process synchronizer call
process_synchronizer_call() {
    # The function retrieves the synchronizer credentials using the get_synchronizer_creds function.
    # If the synchronizer credentials are not retrieved successfully, an error message is displayed and the script exits.
    # Otherwise, the synchronizer credentials are printed and the script exits with a success status.
    synchronizer_creds=$(get_synchronizer_creds)
    if [[ -z "$synchronizer_creds" ]]; then
        echo "Failed to retrieve Synchronizer token." >&2
        exit 1
    fi

    echo "${synchronizer_creds}"
    exit 0
}

# Check if required arguments are provided
# The script checks if the required arguments --identity-url or --conjur-url are provided.
# If any of the required arguments are missing, an error message is displayed and the script exits.
if [[ -z "$IDENTITY_URL" && -z "$CONJUR_URL" ]]; then
    echo "Missing required arguments. Please provide either --identity-url or --conjur-url."
    exit 1
fi
if [[ -n "$IDENTITY_URL" && -z "$USERNAME" ]]; then
    echo "Missing required arguments. Please provide --username."
    exit 1
fi
if [[ -n "$CONJUR_TOKEN" && -z "$CONJUR_URL" ]]; then
    echo "Missing required argument. Please provide --conjur--url"
    exit 1
fi
if [[ -n "$CONJUR_URL" && -z "$IDENTITY_TOKEN" && -z $CONJUR_TOKEN ]]; then
    echo "Missing required argument. Please provide --identity-token."
    exit 1
fi
# Build Docker image
build_docker_image

# Process the appropriate calls based on the provided arguments
# The script checks the provided arguments and calls the corresponding functions to retrieve the required tokens or credentials.
# If no specific arguments are provided, it calls the process_synchronizer_call function by default.
if [[ -n "$IDENTITY_URL" ]]; then
    process_identity_token_call
fi
if [[ -n "$CONJUR_URL" && -n "$IDENTITY_TOKEN" ]]; then
    process_conjur_token_call
fi
if [[ -n "$CONJUR_TOKEN" && -n "$CONJUR_URL" && -n "$EDGE_NAME" ]]; then
    process_conjur_edge_call
else
    process_synchronizer_call
fi
