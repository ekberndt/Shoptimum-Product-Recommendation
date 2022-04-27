from website_element import WebsiteElement

class WebsiteObject():
  
    def __init__(self, webname = '', weburl = ''):
        self._track_variables = ['web_url', 'addcart', 'gocart', 'webname', 'checkout']
        
        # added in below
        #self.append_command(self._weburl)
       
        self._webname = WebsiteElement("webname", webname, "name")
        # added in below
        # self.append_command(self._webname)

        self._addcart = WebsiteElement("", "addcart", "xpath")
        self._track_variables.append(self.getaddcart().name)
        self._checkout = WebsiteElement("", "checkout", "xpath")
        self._track_variables.append(self.getcheckout().name)
        self._gocart = WebsiteElement("", "gocart", "xpath")
        self._track_variables.append(self.getgocart().name)
        self._procedure = []
        



    def custom_command(self, lst_website_elements):
        """for websites that differ from the default, input commands of website elements based on order from lst_website_elements, selenium will then iterate 
        through self.procedure and do a comman procedure based on website elements type, be it xpath, url, keys for send_keys, etc"""
        self.getprocedure().clear()
        for i in lst_website_elements:
            self.getprocedure()[i] = lst_website_elements[i]
    def append_command(self, website_element):
        self._procedure.append(website_element)
    def to_json_dict(self):
        data = {}
        data['webname='] = self.getwebname().name
        print('json dict time ***')
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
    def setaddcart(self, addcart):
        self._addcart = addcart
    def setcheckout(self, checkout):
        self._checkout = checkout
    def setwebname(self, webname):
        self._webname = webname
    def setgotocart(self, gocart):
        self._gocart = gocart

    def getaddcart(self):
        return self._addcart
    def getcheckout(self):
        return self._checkout
    def getwebname(self):
        return self._webname
    def getweburl(self):
        return self._weburl
    def getgocart(self):
        return self._gocart
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