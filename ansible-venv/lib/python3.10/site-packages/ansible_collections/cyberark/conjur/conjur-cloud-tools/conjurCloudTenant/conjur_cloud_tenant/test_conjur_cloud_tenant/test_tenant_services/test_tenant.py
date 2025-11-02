import unittest
from unittest.mock import MagicMock, patch
from tenant_services.tenant import Tenant
from tenant_services.verify_everest_response import _verify_response

class TestTenant(unittest.TestCase):

    @patch("tenant_services.connector.TME2EConnector")
    def setUp(self, mock_connector):
        # Mock the connector to avoid making real calls
        mock_connector.return_value = MagicMock()
        self.tenant = Tenant(mock_connector, "test_tenant_id")
        self.assertIsInstance(self.tenant.connector, MagicMock)

    def test_suspend(self):
        response = MagicMock()
        response.id = "test_tenant_id"
        response.status = "SUSPENDING"
        # Mock the suspend_tenant method of the connector
        self.tenant.connector.suspend_tenant = MagicMock(return_value=response)

        # Call the suspend method
        result = self.tenant.suspend()

        # Verify the response
        self.assertEqual(result, response)
        self.tenant.connector.suspend_tenant.assert_called_once_with('test_tenant_id', sync_wait=False)

    def test_suspend_with_wait(self):
        response = MagicMock()
        response.id = "test_tenant_id"
        response.status = "SUSPENDED"
        # Mock the suspend_tenant method of the connector
        self.tenant.connector.suspend_tenant = MagicMock(return_value=response)

        # Call the suspend method
        result = self.tenant.suspend(wait=True)

        # Verify the response
        self.assertEqual(result, response)
        self.tenant.connector.suspend_tenant.assert_called_once_with('test_tenant_id', sync_wait=True)

    def test_activate(self):
        response = MagicMock()
        response.id = "test_tenant_id"
        response.status = "ACTIVE"
        # Mock the activate_tenant method of the connector
        self.tenant.connector.activate_tenant = MagicMock(return_value=response)

        # Call the activate method
        result = self.tenant.activate()

        # Verify the response
        self.assertEqual(result, response)
        self.tenant.connector.activate_tenant.assert_called_once_with('test_tenant_id', sync_wait=False)

    def test_delete(self):
        response = MagicMock()
        response.id = "test_tenant_id"
        response.status = "SUSPENDING"
        # Mock the suspend_tenant method of the connector
        #self.tenant.connector.suspend_tenant = MagicMock(return_value=response)
        self.tenant.suspend = MagicMock(return_value=response)

        response = MagicMock()
        response.id = "test_tenant_id"
        response.status = "DELETING"
        # Mock the delete_tenant method of the connector
        self.tenant.connector.delete_tenant = MagicMock(return_value=response)

        # Call the delete method
        result = self.tenant.delete()

        # Verify the response
        self.assertEqual(result, response)
        self.tenant.connector.delete_tenant.assert_called_once_with('test_tenant_id')

    def test_is_tenant_deleted(self):
        response = MagicMock()
        response.id = "test_tenant_id"
        response.status = "DELETED"
        # Mock the get_tenant method of the connector
        self.tenant.connector.get_tenant = MagicMock(return_value=response)

        # Call the is_tenant_deleted method
        result = self.tenant.is_tenant_deleted()

        # Verify the response
        self.assertTrue(result)
        self.tenant.connector.get_tenant.assert_called_once_with('test_tenant_id')

    def test_is_tenant_in_state(self):
        response = MagicMock()
        response.id = "test_tenant_id"
        response.status = "ACTIVE"
        # Mock the get_tenant method of the connector
        self.tenant.connector.get_tenant = MagicMock(return_value=response)

        # Call the is_tenant_in_state method
        result = self.tenant.is_tenant_in_state('ACTIVE')

        # Verify the response
        self.assertTrue(result)
        self.tenant.connector.get_tenant.assert_called_once_with('test_tenant_id')

if __name__ == "__main__":
    unittest.main()
