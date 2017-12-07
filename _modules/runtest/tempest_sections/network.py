
import base_section

from runtest import conditions

class Network(base_section.BaseSection):

    name = "network"
    options = [
        'build_interval',
        'build_timeout',
        'catalog_type',
        'default_network',
        'dns_servers',
        'endpoint_type',
        'floating_network_name',
        'port_vnic_type',
        'project_network_cidr',
        'project_network_mask_bits',
        'project_network_v6_cidr',
        'project_network_v6_mask_bits',
        'project_networks_reachable',
        'public_network_id',
        'public_router_id',
        'region',
        'shared_physical_network',
    ]


    @property
    def build_interval(self):
        pass

    @property
    def build_timeout(self):
        pass

    @property
    def catalog_type(self):
        pass

    @property
    def default_network(self):
        pass

    @property
    def dns_servers(self):
        pass

    @property
    def endpoint_type(self):
        pass

    @property
    def floating_network_name(self):
        pass

    @property
    def port_vnic_type(self):
        pass

    @property
    def project_network_cidr(self):
        pass

    @property
    def project_network_mask_bits(self):
        pass

    @property
    def project_network_v6_cidr(self):
        pass

    @property
    def project_network_v6_mask_bits(self):
        pass

    @property
    def project_networks_reachable(self):
        pass

    @property
    def public_network_id(self):
        c = conditions.BaseRule(field='keystone.client.enabled', op='eq',
                                val=True)
        nodes = self.get_nodes_where_condition_match(c)
        network_name = self.runtest_opts.get(
            'convert_to_uuid', {}).get('public_network_id')

        if not network_name:
          return

        res = self.authenticated_openstack_module_call(
            nodes[0], 'neutronng.list_netowkrs')[nodes[0]]['networks']
        networks = [n['id'] for n in res if n['name'] == network_name]

        if len(networks) != 1:
            raise Exception("Error getting networks: {}".format(networks))

        return networks[0]

    @property
    def public_router_id(self):
        pass

    @property
    def region(self):
        pass

    @property
    def shared_physical_network(self):
        pass
