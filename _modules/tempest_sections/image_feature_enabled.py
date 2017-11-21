
import base_section

class ImageFeatureEnabled(base_section.BaseSection):

    name = "image-feature-enabled"
    options = [
        'api_v1',
        'api_v2',
        'deactivate_image',
    ]

    
    @property
    def api_v1(self):
        pass
    
    @property
    def api_v2(self):
        pass
    
    @property
    def deactivate_image(self):
        pass
    