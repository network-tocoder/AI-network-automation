#!/bin/bash

# Authentication container entrypoint for running tests
test_dirs=(
    "test_conjur_cloud_tenant"
    "test_conjur_cloud_tenant/test_tenant_services"
)

for test in "${test_dirs[@]}"; do
    if ! poetry run python -m unittest discover "${test}" -v; then
        exit 1
    fi
done
