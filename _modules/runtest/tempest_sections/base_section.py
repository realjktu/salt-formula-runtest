
import abc
import jsonpath_rw as jsonpath

import salt

from runtest import conditions

class BaseSection(object):

    def __init__(self, pillar, runtest_opts):
        super(BaseSection, self).__init__()
        self.pillar = pillar
        self.runtest_opts = runtest_opts
        self.salt_client = salt.client.get_local_client()

    @abc.abstractproperty
    def name(self):
        """"""

    @abc.abstractproperty
    def options():
        """"""

    def get_item_when_condition_match(self, item_path, condition):
        """Get specified item from pillar when condition match.
     
        """

        for node, npillar in self.pillar.items():
            for match in jsonpath.parse(condition.field).find(npillar):
                if condition.op == 'eq':
                    if match.value == condition.value:
                        res = jsonpath.parse(item_path).find(npillar)
                        if res:
                            return res[0].value

    def get_nodes_where_condition_match(self, condition):
        """ Return a list of nodes that have pillar that matches condition.
        """

        res = []
        for node, npillar in self.pillar.items():
            if condition.check(npillar):
                res.append(node)
        return res

    def authenticated_openstack_module_call(self, target, module, *args, **kwargs):
        """Calls specified openstack module from admin keystone user.
        """
        auth_profile = {}
        ks = conditions.BaseRule(field='keystone.server.enabled', op='eq', val=True)
        auth_profile['connection_password'] = self.get_item_when_condition_match(
            'keystone.server.admin_password', ks)
        auth_profile['connection_user'] = self.get_item_when_condition_match(
            'keystone.server.admin_name', ks)
        auth_profile['connection_tenant'] = self.get_item_when_condition_match(
            'keystone.server.admin_tenant', ks)
        auth_profile['connection_region_name'] = self.get_item_when_condition_match(
            'keystone.server.region', ks)
        address = self.get_item_when_condition_match(
            'keystone.server.bind.public_address', ks)
        port = self.get_item_when_condition_match('keystone.server.bind.public_port', ks)
        auth_profile['connection_auth_url'] = "http://{}:{}/v2.0".format(address, port)

        kwargs.update(auth_profile)

        return self.salt_client.cmd(target, 'neutronng.list_networks', timeout=5,
                                    gather_job_timeout=15, arg=args, kwarg=kwargs)       
