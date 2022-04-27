class WebsiteElement():
    """A command for website object"""
    def __init__(self, element = '', name = '', type = '', need_clear = False):
        self._element = element
        self._name = name
        self._type = type 
        self._need_clear = need_clear
    
    @property
    def element(self):
        return self._element
    @element.setter
    def element(self, element):
        self._element = element
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, type):
        self._type = type
    @property
    def need_clear(self):
        return self._need_clear
    @need_clear.setter
    def need_clear(self, bool):
        self._need_clear = bool
    def need_clear_to_str(self):
        return 'true' if self.need_clear else 'false'
    def write_self(self):
        return ' '.join([self.element, self.name, self.type])