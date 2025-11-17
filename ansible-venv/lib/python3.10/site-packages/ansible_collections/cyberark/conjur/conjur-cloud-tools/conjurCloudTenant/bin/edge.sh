#!/bin/bash

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -c|--common-name)
            COMMON_NAME="$2"
            shift
            ;;
        -e|--edge-name)
            EDGE_NAME="$2"
            shift
            ;;
        -p|--persistent-path)
            PERSISTENT_PATH="$2"
            shift
            ;;
        -s|--subject-alt-names)
            SUBJECT_ALT_NAMES="$2"
            shift
            ;;
        -t|--token)
            TOKEN="$2"
            shift
            ;;
        -u|--url)
            CONJUR_CLOUD_URL="$2"
            shift
            ;;
        *)
            echo "Invalid argument: $1"
            exit 1
            ;;
    esac
    shift
done

arg_parse() {
    PERSISTENT_PATH="${PERSISTENT_PATH:-/opt/edge/data}"
    COMMON_NAME="${COMMON_NAME:-edge1}"
    SUBJECT_ALT_NAMES="${SUBJECT_ALT_NAMES:-edge1}"

    # Check if TOKEN is provided
    if [[ -z $TOKEN ]]; then
        echo "TOKEN is required" >&2
        exit 1
    fi
    if [[ -z $EDGE_NAME ]]; then
        echo "TOKEN is required" >&2
        exit 1
    fi
    if [[ -z $CONJUR_CLOUD_URL ]]; then
        echo "TOKEN is required" >&2
        exit 1
    fi
    EDGE_IMAGE=registry.tld/cyberark/edge
    EDGE_IMAGE_VERSION=1.2.0
}

start_edge_container() {
    # Run the Docker container
    if ! docker run -d \
        --name "$EDGE_NAME" \
        -e CONJUR_CLOUD_URL="$CONJUR_CLOUD_URL/api" \
        -e EDGE_INITIAL_CREDS="$TOKEN" \
        -p 443:8443 \
        -p 444:8444 \
        --mount type=bind,source="$PERSISTENT_PATH",target=/opt/edge/data \
        -e COMMON_NAME="$COMMON_NAME" \
        -e SAN="$SUBJECT_ALT_NAMES" \
        --restart unless-stopped \
        "$EDGE_IMAGE:$EDGE_IMAGE_VERSION"; then

        echo "Failed to start $EDGE_NAME" >&2
        exit 1
    fi
}

is_container_running() {
    # Check if the Docker container is running
    if ! docker ps -f name="$EDGE_NAME" --format '{{.Names}}' | grep -q "$EDGE_NAME"; then
        echo "Failed to start $EDGE_NAME" >&2
        exit 1
    fi
}

main() {
    # Parse command line arguments
    if arg_parse; then
        echo "Arguments parsed successfully"
    fi
    # Change ownership of persistence folder
    if sudo mkdir -p "$PERSISTENT_PATH" && sudo chown -R 5000:5000 "$PERSISTENT_PATH"; then
        echo "Persistence folder created successfully"
    fi
    if start_edge_container; then
        echo "Edge container started successfully"
    fi
    # Check if the Docker container is running
    if is_container_running; then
        echo "$EDGE_NAME started successfully"
    fi
}

main