
import abc

class BaseSection(object):

    def __init__(self, pillar):
        super(BaseSection, self).__init__()
        self.pillar = pillar

    @abc.abstractproperty
    def name(self):
        """"""

    @abc.abstractproperty
    def options():
        """"""

