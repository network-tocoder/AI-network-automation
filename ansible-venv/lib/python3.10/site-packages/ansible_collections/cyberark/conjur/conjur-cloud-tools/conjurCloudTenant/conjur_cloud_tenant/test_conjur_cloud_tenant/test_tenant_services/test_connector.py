import unittest
from unittest.mock import MagicMock, patch
from tenant_services.connector import TenantConnector
from tenant_services.tenant import Tenant
from tenant_services.verify_everest_response import _verify_response
from everest_env_utils.env_mapping import AwsEnv, ROOT_DOMAIN

class TestTenantConnector(unittest.TestCase):

    @patch("tenant_services.connector.TME2EConnector")
    def setUp(self, mock_connector):
        # Mock the connector to avoid making real calls
        mock_connector.return_value = MagicMock()
        self.tenant_connector = TenantConnector(
            ssm_role_arn="ssm_role_arn",
            external_id="external_id",
            region="region",
            everest_running_env="integration"
        )
        self.assertIsInstance(self.tenant_connector.connector, MagicMock)

    def test_create_new_tenant(self):
        # Mock the response from the connector
        response = MagicMock()
        response.id = "tenant_id"
        response.status = "ACTIVE"
        self.tenant_connector.connector.get_tenant = MagicMock(return_value=response)
        self.tenant_connector.connector.create_tenant = MagicMock(return_value=response)

        # Call the method under test
        tenant = self.tenant_connector.create_new_tenant(
            tenant_name_prefix="prefix",
            tenant_type="TESTING",
            customer_type="INTERNAL"
        )

        # Assert that the tenant object is returned
        self.assertIsInstance(tenant, Tenant)
        self.assertEqual(tenant.id, response.id)

    def test_get_all_existing_tenants(self):
        # Mock the response from the connector
        response = MagicMock()
        response.id = "tenant_id"
        self.tenant_connector.connector.get_all_tenants = MagicMock(return_value=[response])

        # Call the method under test
        existing_tenants = self.tenant_connector.get_all_existing_tenants()

        # Assert that the list of tenants is returned
        self.assertIsInstance(existing_tenants, list)
        self.assertEqual(len(existing_tenants), 1)
        self.assertIsInstance(existing_tenants[0], Tenant)
        self.assertEqual(existing_tenants[0].base, response)

    def test_get_existing_tenant(self):
        # Mock the response from the connector
        response = MagicMock()
        response.id = "tenant_id"
        self.tenant_connector.connector.get_tenant = MagicMock(return_value=response)

        # Call the method under test
        existing_tenant = self.tenant_connector.get_existing_tenant("tenant_id")

        # Assert that the tenant object is returned
        self.assertIsInstance(existing_tenant, Tenant)
        self.assertEqual(existing_tenant.base, response)


if __name__ == '__main__':
    unittest.main()
