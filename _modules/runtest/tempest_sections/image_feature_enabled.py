
import base_section

from runtest import conditions

class ImageFeatureEnabled(base_section.BaseSection):

    name = "image-feature-enabled"
    options = [
        'api_v1',
        'api_v2',
        'deactivate_image',
    ]


    @property
    def api_v1(self):
        ge = conditions.BaseRule('*.glance.server.enabled', 'eq', True,
                                 multiple='any').check(self.pillar)
        if not ge:
            return
        c = conditions.BaseRule('glance.server.enabled', 'eq', True)
        gv = self.get_item_when_condition_match(
            'glance.server.version', c)
        # starting from Ocata glance_v1 is disable - hardcoded
        if gv not in ['juno', 'kilo', 'liberty', 'mitaka', 'newton']:
           return True

    @property
    def api_v2(self):
        return True

    @property
    def deactivate_image(self):
        return True
