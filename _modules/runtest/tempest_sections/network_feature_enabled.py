
import base_section

from runtest import conditions

class NetworkFeatureEnabled(base_section.BaseSection):

    name = "network-feature-enabled"
    options = [
        'api_extensions',
        'floating_ips',
        'ipv6',
        'ipv6_subnet_attributes',
        'port_admin_state_change',
        'port_security',
    ]


    @property
    def api_extensions(self):
        # We will get this when running
        # tox -evenv -- tempest verify-config -uro tempest_config_file
        pass

    @property
    def floating_ips(self):
        pass

    @property
    def ipv6(self):
        pass

    @property
    def ipv6_subnet_attributes(self):
        pass

    @property
    def port_admin_state_change(self):
        pass

    @property
    def port_security(self):
        c = conditions.BaseRule('neutron.server.enabled', 'eq', True)
        ext = self.get_item_when_condition_match(
            'neutron.server.backend.extension', c)

        if 'port_security' in ext:
            return ext['port_security'].get('enabled', False)

        return True
