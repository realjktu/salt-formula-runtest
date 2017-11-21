
import base_section

class DnsFeatureEnabled(base_section.BaseSection):

    name = "dns_feature_enabled"
    options = [
        'api_admin',
        'api_v1',
        'api_v1_servers',
        'api_v2',
        'api_v2_quotas',
        'api_v2_root_recordsets',
        'bug_1573141_fixed',
    ]

    
    @property
    def api_admin(self):
        pass
    
    @property
    def api_v1(self):
        pass
    
    @property
    def api_v1_servers(self):
        pass
    
    @property
    def api_v2(self):
        pass
    
    @property
    def api_v2_quotas(self):
        pass
    
    @property
    def api_v2_root_recordsets(self):
        pass
    
    @property
    def bug_1573141_fixed(self):
        pass
    