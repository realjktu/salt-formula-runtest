
import base_section

class ServiceAvailable(base_section.BaseSection):

    name = "service_available"
    options = [
        'cinder',
        'designate',
        'glance',
        'heat',
        'neutron',
        'nova',
        'swift',
    ]


    
    def _is_service_enabled(self, service):
        """Check if service is enabled in specific environment.

        We assume service is enabled when API for this serivce is
        enabled at least on one node in the cloud.

        :param service:
        :param pillars: 
        """

        for node, p in self.pillar.items():
            p_service = p.get(service)
            if p_service:
                p_api = p_service.get('api') or p_service.get('controller')
                if p_api:
                    if p_api.get('enabled'):
                        return True
        return False
    
    @property
    def cinder(self):
        pass
    
    @property
    def designate(self):
        return self._is_service_enabled('designate')
    
    @property
    def glance(self):
        return self._is_service_enabled('glance')
    
    @property
    def heat(self):
        return self._is_service_enabled('heat')
    
    @property
    def neutron(self):
        return self._is_service_enabled('neutron')
    
    @property
    def nova(self):
        return self._is_service_enabled('nova')
    
    @property
    def swift(self):
        return self._is_service_enabled('swift')
    
