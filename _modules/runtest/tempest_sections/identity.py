
import base_section

from runtest import conditions

class Identity(base_section.BaseSection):

    name = "identity"
    options = [
        'admin_domain_scope',
        'admin_role',
        'auth_version',
        'ca_certificates_file',
        'catalog_type',
        'default_domain_id',
        'disable_ssl_certificate_validation',
        'region',
        'uri',
        'uri_v3',
        'user_lockout_duration',
        'user_lockout_failure_attempts',
        'user_unique_last_password_count',
        'v2_admin_endpoint_type',
        'v2_public_endpoint_type',
        'v3_endpoint_type',
    ]


    @property
    def admin_domain_scope(self):
        pass

    @property
    def admin_role(self):
        pass

    @property
    def auth_version(self):
        return 'v3'

    @property
    def ca_certificates_file(self):
        c = conditions.BaseRule('keystone.server.enabled', 'eq', True)
        return self.get_item_when_condition_match(
            'keystone.server.cacert', c)

    @property
    def catalog_type(self):
        pass

    @property
    def default_domain_id(self):
        pass

    @property
    def disable_ssl_certificate_validation(self):
        pass

    @property
    def region(self):
        c = conditions.BaseRule('keystone.server.enabled', 'eq', True)
        return self.get_item_when_condition_match(
            'keystone.server.region', c)

    @property
    def uri(self):
        c = conditions.BaseRule('keystone.server.enabled', 'eq', True)
        vip = self.get_item_when_condition_match(
            '_param.cluster_vip_address', c)
        port = self.get_item_when_condition_match(
            'keystone.server.bind.private_port', c)
        return "http://{}:{}/v2.0".format(vip, port)

    @property
    def uri_v3(self):
        c = conditions.BaseRule('keystone.server.enabled', 'eq', True)
        vip = self.get_item_when_condition_match(
            '_param.cluster_vip_address', c)
        port = self.get_item_when_condition_match(
            'keystone.server.bind.private_port', c)
        return "http://{}:{}/v3".format(vip, port)

    @property
    def user_lockout_duration(self):
        pass

    @property
    def user_lockout_failure_attempts(self):
        pass

    @property
    def user_unique_last_password_count(self):
        pass

    @property
    def v2_admin_endpoint_type(self):
        pass

    @property
    def v2_public_endpoint_type(self):
        pass

    @property
    def v3_endpoint_type(self):
        pass
