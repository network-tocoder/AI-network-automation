import unittest
from unittest.mock import MagicMock, patch
import conjur_cloud_tenant

class TestConjurCloudTenant(unittest.TestCase):
    def setUp(self):
        conjur_cloud_tenant.CONNECTOR = MagicMock()
        self.mock_connector = conjur_cloud_tenant.CONNECTOR

    @patch('conjur_cloud_tenant.write_tenant_to_file')
    @patch('conjur_cloud_tenant.setup_tenant')
    @patch('conjur_cloud_tenant.wait_for_tenant_status')
    @patch('conjur_cloud_tenant.cleanup_tenants')
    @patch('conjur_cloud_tenant.delete_tenant')
    @patch('conjur_cloud_tenant.create_tenant')
    def test_main_create_tenant(self, 
                                mock_create_tenant, 
                                mock_delete_tenant, 
                                mock_cleanup_tenants,
                                mock_wait_for_tenant_status,
                                mock_setup_tenant,
                                mock_write_tenant_to_file):
        conjur_cloud_tenant.ARGS = MagicMock()
        conjur_cloud_tenant.ARGS.delete = False
        conjur_cloud_tenant.ARGS.cleanup = False
        # Run the main function
        conjur_cloud_tenant.main()

        # Verify that the proper functions were called
        mock_delete_tenant.assert_not_called()
        mock_cleanup_tenants.assert_not_called()
        mock_create_tenant.assert_called_once()

    @patch('conjur_cloud_tenant.create_tenant')
    @patch('conjur_cloud_tenant.cleanup_tenants')
    @patch('conjur_cloud_tenant.delete_tenant')
    def test_main_delete_tenant(self, 
                                mock_delete_tenant, 
                                mock_cleanup_tenants, 
                                mock_create_tenant):
        conjur_cloud_tenant.ARGS = MagicMock()
        conjur_cloud_tenant.ARGS.delete = True
        conjur_cloud_tenant.ARGS.cleanup = False
        # Run the main function
        conjur_cloud_tenant.main()

        # Verify that the proper functions were called
        mock_create_tenant.assert_not_called()
        mock_cleanup_tenants.assert_not_called()
        mock_delete_tenant.assert_called_once()

    @patch('conjur_cloud_tenant.create_tenant')
    @patch('conjur_cloud_tenant.delete_tenant')
    @patch('conjur_cloud_tenant.cleanup_tenants')
    def test_main_cleanup_tenants(self, 
                                  mock_cleanup_tenants, 
                                  mock_delete_tenant, 
                                  mock_create_tenant):
        conjur_cloud_tenant.ARGS = MagicMock()
        conjur_cloud_tenant.ARGS.delete = False
        conjur_cloud_tenant.ARGS.cleanup = True
        # Run the main function
        conjur_cloud_tenant.main()
        
        # Verify that the proper functions were called
        mock_create_tenant.assert_not_called()
        mock_delete_tenant.assert_not_called()
        mock_cleanup_tenants.assert_called_once()

    @patch('conjur_cloud_tenant.CONNECTOR.create_new_tenant')
    def test_create_tenant(self, 
                           mock_create_new_tenant):
        mock_tenant = MagicMock()

        mock_create_new_tenant.return_value = mock_tenant 


        # Run the create_tenant function
        conjur_cloud_tenant.create_tenant()

        # Verify that the proper functions were called
        mock_create_new_tenant.assert_called_once_with(
            tenant_name_prefix="conjops",
            tenant_type="TESTING",
            customer_type="INTERNAL",
        )


    @patch('conjur_cloud_tenant.create_admin_user')
    def test_setup_tenant(self,
                           mock_create_admin_user):

        mock_tenant = MagicMock()
        mock_create_admin_user.return_value = 'admin_user'
        conjur_cloud_tenant.setup_tenant(mock_tenant)
        mock_create_admin_user.assert_called_once_with(
            tenant=mock_tenant,
            username='conjurops',
            password=conjur_cloud_tenant.os.environ.get('CONJUR_CLOUD_ADMIN_PASS')
        )

    @patch('conjur_cloud_tenant.tenant_to_dict')
    @patch('conjur_cloud_tenant.json.dump')
    @patch('conjur_cloud_tenant.open')
    def test_write_tenant_to_file(self,
                           mock_open,
                           mock_json_dump,
                           mock_tenant_to_dict):

        mock_tenant = MagicMock()
        mock_file_obj = MagicMock()
        mock_open.return_value = mock_file_obj

        conjur_cloud_tenant.write_tenant_to_file(mock_tenant)

        mock_open.assert_called_once_with('/everest/tenant.json', 'x', encoding='utf-8')

        mock_json_dump.assert_called_once_with(
            mock_tenant_to_dict(),
            mock_file_obj.__enter__(),
            ensure_ascii=False,
            indent=4
        )

    @patch('conjur_cloud_tenant.CONNECTOR.get_existing_tenant')
    def test_delete_tenant_missing_info(self, mock_get_existing_tenant):
        mock_tenant = MagicMock()
        mock_get_existing_tenant.return_value = mock_tenant

        # Run the delete_tenant function
        conjur_cloud_tenant.delete_tenant()

        # Verify that the delete method was not called
        mock_tenant.delete.assert_not_called()

    @patch('conjur_cloud_tenant.CONNECTOR.get_existing_tenant')
    def test_delete_tenant(self, mock_get_existing_tenant):
        mock_tenant = MagicMock()
        mock_tenant.base.name = 'conjops-'
        mock_tenant.base.contact_details.email = 'conj_ops@cyberark.com'
        mock_get_existing_tenant.return_value = mock_tenant

        # Run the delete_tenant function
        conjur_cloud_tenant.delete_tenant()

        # Verify that the delete method was called
        mock_tenant.delete.assert_called_once()

    @patch('conjur_cloud_tenant.CONNECTOR.get_all_existing_tenants')
    def test_cleanup_tenants(self, mock_get_all_existing_tenants):
        mock_tenant1 = MagicMock()
        mock_tenant1.base.name = 'conjops-1'
        mock_tenant1.base.contact_details.email = 'conj_ops@cyberark.com'
        mock_tenant1.base.expiration_date = '2021-12-31'

        mock_tenant2 = MagicMock()
        mock_tenant2.base.name = 'conjops-2'
        mock_tenant2.base.contact_details.email = 'conj_ops@cyberark.com'
        # This will need to be updated in roughly 7,975 years from 2024
        mock_tenant2.base.expiration_date = '9999-01-02'

        mock_tenant3 = MagicMock()
        mock_tenant3.base.name = 'other-tenant'
        mock_tenant3.base.contact_details.email = 'other@cyberark.com'
        mock_tenant3.base.expiration_date = '2022-01-01'
        mock_get_all_existing_tenants.return_value = [mock_tenant1, mock_tenant2, mock_tenant3]

        # Run the cleanup_tenants function
        conjur_cloud_tenant.cleanup_tenants()

        # Verify that the proper functions were called
        mock_tenant1.delete.assert_called_once()
        mock_tenant2.delete.assert_not_called()
        mock_tenant3.delete.assert_not_called()

    @patch('conjur_cloud_tenant.Tenant.assign_role_to_identity_user')
    def test_create_admin_user(self, mock_assign_role_to_identity_user):
        # Mock the necessary objects and methods
        mock_tenant = MagicMock()
        mock_tenant.get_user_suffix.return_value = 'example.com'
        mock_tenant.create_identity_user.return_value = None
        mock_tenant.assign_role_to_identity_user.return_value = None

        # Run the create_admin_user function
        conjur_cloud_tenant.create_admin_user(mock_tenant, 'conjurops', 'password')

        # Verify that the necessary methods were called
        mock_tenant.create_identity_user.assert_called_once_with(
            username='conjurops@example.com',
            password='password',
            email='conj_ops@cyberark.com',
            display_name='Conjurops'
        )
        mock_tenant.assign_role_to_identity_user.assert_any_call(
            username='conjurops@example.com',
            role_name='System Administrator'
        )
        mock_tenant.assign_role_to_identity_user.assert_any_call(
            username='conjurops@example.com',
            role_name='Secrets Manager – Conjur Cloud Admin'
        )

    def test_tenant_to_dict(self):
        # Create a mock tenant object
        class MockTenant:
            def __init__(self):
                self.id = '1234'
                self.base = MockBase()

        class MockBase:
            def __init__(self):
                self.name = 'conjops-1'
                self.contact_details = MockContactDetails()
                self.expiration_date = '2021-12-31'

        class MockContactDetails:
            def __init__(self):
                self.email = 'conj_ops@cyberark.com'

        mock_tenant = MockTenant()

        # Convert the mock tenant object to a dictionary
        result = conjur_cloud_tenant.tenant_to_dict(mock_tenant)

        expected_result = {
            'id': '1234',
            'name': 'conjops-1',
            'contact_details': {
            'email': 'conj_ops@cyberark.com'
            },
            'expiration_date': '2021-12-31'
        }

        # Verify the dictionary structure
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()