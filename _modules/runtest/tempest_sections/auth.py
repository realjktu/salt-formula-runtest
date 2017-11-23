
import base_section

from runtest import conditions

class Auth(base_section.BaseSection):

    name = "auth"
    options = [
        'admin_domain_name',
        'admin_password',
        'admin_project_name',
        'admin_username',
        'create_isolated_networks',
        'default_credentials_domain_name',
        'tempest_roles',
        'test_accounts_file',
        'use_dynamic_credentials',
    ]


    @property
    def admin_domain_name(self):
        pass

    @property
    def admin_password(self):
        c = conditions.BaseRule('keystone.server.enabled', 'eq', True)
        return self.get_item_when_condition_match(
            'keystone.server.admin_password', c)

    @property
    def admin_project_name(self):
        c = conditions.BaseRule('keystone.server.enabled', 'eq', True)
        return self.get_item_when_condition_match(
            'keystone.server.admin_tenant', c)

    @property
    def admin_username(self):
        c = conditions.BaseRule('keystone.server.enabled', 'eq', True)
        return self.get_item_when_condition_match(
            'keystone.server.admin_name', c)

    @property
    def create_isolated_networks(self):
        pass

    @property
    def default_credentials_domain_name(self):
        pass

    @property
    def tempest_roles(self):
        pass

    @property
    def test_accounts_file(self):
        pass

    @property
    def use_dynamic_credentials(self):
        pass

