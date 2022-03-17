
class WebsiteElement():
    """Glorified xpath, allows us to differentiate between 
    xpaths so our code knows what to do for each given xpath"""
    def __init__(self, element = '', name = '', type = '', need_clear = False):
        # Element is xpath text.
        
        """CODE HERE"""
        # Name of xpath and name can be used by send_key if element is a xpath_sendkey
        
        """CODE HERE"""
        # Type of xpath; is it a send key or a regular xpath
        
        """CODE HERE"""
        # If im an xpath_sendkey do i need to clear text box before inputting text?                      222
        
        """CODE HERE"""
    
    @property
    def element(self):
        """CODE HERE"""
    @element.setter
    def element(self, element):
        """CODE HERE"""
    @property
    def name(self):
        """CODE HERE"""
    @name.setter
    def name(self, name):
        """CODE HERE"""
    @property
    def type(self):
        """CODE HERE"""
    @type.setter
    def type(self, type):
        """CODE HERE"""
    @property
    def need_clear(self):
        """CODE HERE"""
    @need_clear.setter
    def need_clear(self, boolean):
        """CODE HERE"""
    def need_clear_to_str(self):
        """prints need_clear variable to string 
        for hardsaving to json or txt.
        
        variables -- need_clear
        """
        return 'true' if """CODE HERE""" == True else 'false'
    def write_self(self):
        """prints information of self for saving to a json or txt"""
        return ' '.join([self.element, self.name, self.type])