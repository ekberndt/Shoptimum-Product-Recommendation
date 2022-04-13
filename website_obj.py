import website_element

class WebsiteObject():
    """An object that hold a website information, has the url, name, and xpath query for shopping process."""
    webname = ""
    weburl = ""
    procedure = []
    
    
    def __init__(self, webname = '', weburl = ''):
        self._track_variables = []
        self._weburl = website_element(weburl, "web_url", "url") 
        self._track_variables.append(self.getweburl().name)
        self._webname = website_element(webname, "webname", "name")
        self._track_variables.append(self.getwebname().name)
        # array to hold query of website elements
        self._procedure = []
        
            
    def custom_command(self, lst_website_elements):
        """for websites that differ from the default, input commands of website elements based on order from lst_website_elements, selenium will then iterate 
        through self.procedure and do a command procedure based on website elements type, be it xpath, url, keys for send_keys, etc"""
        """ 1. iterate through lst_website_elements, a list of website elements
            2. clear current procedure
            3. for each website element in the list"""
        for i in lst_website_elements:
            self._procedure = []
            self._procedure.append(i)

    def append_command(self, website_element):
        """adds a website element to current procedure"""
        self._procedure.append(website_element)
        
    def to_json_dict(self):
        """turns procedure into a dicionary that can be converted to json"""
        data = {}
        data['webname='] = self.getwebname().name
        print('json dict time *******')
        print(self.getprocedure())
        for y in self.getprocedure():
                if y.name in self.track_variables:
                    data[y.name + "="] = y.write_self() + '\n'
                elif y.type == 'xpath_sendkey':
                    data[y.name+'send_key='] = y.write_self() + ' ' + y.need_clear_to_str() + '\n'
                else:
                    data[y.name] = y.write_self()+'\n'
        print(data)
        return data 
    

    def setweburl(self, weburl):
        self._weburl = weburl
          
    def setwebname(self, webname):
        self._webname = webname
    
    def getwebname(self):
        return self._webname
        
    def getweburl(self):
        return self._weburl

    def getprocedure(self):
        return self._procedure
        
    def setprocedure(self, procedure):
        self._procedure = procedure
    @property
    def track_variables(self):
        return self._track_variables
    @track_variables.setter
    def track_variables(self, lst):
        self._track_variables = lst