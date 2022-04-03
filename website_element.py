
class WebsiteElement():
    """Glorified xpath, allows us to differentiate between 
    xpaths so our code knows what to do for each given xpath"""
    def __init__(self, element = '', name = '', type = '', need_clear = False):
        # Element is xpath text. 
        
        self._element = element
        # Name of xpath and name can be used by send_key if element is a xpath_sendkey
        
        self._name = name
        # Type of xpath; is it a send key or a regular xpath
        
        self._type = type
        # If im an xpath_sendkey do i need to clear text box before inputting text?
        
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
    def need_clear(self, boolean):
        self._need_clear = boolean
    def need_clear_to_str(self):
        """prints need_clear variable to string 
        for hardsaving to json or txt.
        
        variables -- need_clear
        """
        return 'true' if self._need_clear == True else 'false'
    def write_self(self):
        """prints information of self for saving to a json or txt"""
        return ' '.join([self.element, self.name, self.type])