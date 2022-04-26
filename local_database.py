import json_text_func
import website_obj
import website_element
import json
import os

class local_database():
    """an object that is used in buy codethat holds all the website objects we need"""
    def __init__(self, file_path = "", handler = ""):
        
        # file path of text file
        """CODE HERE"""
        self._file_path = file_path
        # mode to open text file in (a, w, r, r+)
        """CODE HERE""" 
        self._handler = handler
        # reference to text file
        """CODE HERE"""
        self._file = open(self._file_path, self._handler)
        # turns next file into list a strings line by line
        """CODE HERE"""
        self._saves = []
        for line in self._file:
            self._saves.append(line)
        self._file.close()
        # creates dictionary of website objects from _file
        """CODE HERE"""
        self._websites = {}

        #self.assertion()
        
    def get_file(self):
        #self.assertion()
        return self.saves
    def get_file(self):
        return self._text
    
    "loads website objs into dictionary"
    def collect_websites(self):
        """Turns text from text file or json into a dictionary.
        self._websites is then set to equal that dictionary"""
        #CODE HERE
        while self._saves:
            new_website = json_text_func.convert_to_obj(website_obj(), self._saves)
            self._websites[new_website.getwebname()] = new_website
        
    """write my current dictionary of all website objs to a JSON file"""  
    def write_to_json(self, json_file):
        self.assertion()
        with open(json_file, 'w') as f:
            print('[', file = f)
        for i in [self.get_website_objs().get(i) for i in self.get_website_objs()]:
            with open(json_file, 'a') as f:

                json.dump(i.to_json_dict(), f, indent = 4)
                print(",\n", end = '', file = f)
        with open(json_file, 'a') as f:
            #0 is first of char in doc, 2 is end of document
            f.seek(0, 2)
            #f.tell tells where the cursor is currently at
            f.seek(f.tell() - 3, os.SEEK_SET)
            f.truncate()
            print('\n]', file = f)
            
    
    def json_to_obj(self, json_file):
        """Open a json file to load json 
        website objs into my dictionary.
        
        json_file -- path to json file
        x -- json iterable dictionary
        d -- dictionary
        """
        with open(json_file) as f:
            x = json.load(f)
            d = {}
            for i in x:
                temp_website_holder = json_text_func.convert_dict_to_obj(i, json_text_func.website_dataobj())
                d[temp_website_holder.getwebname().name] = temp_website_holder
            self.set_website_objs(d)
        
            
    def close(self):
        """The function that takes the dictionary, 
        self._websites and iterates through the dictionary
        to write each website object into the text file from which
        this local database was created.
        
        self.get_website_objs() -- access the local database's dictionary
        of website objects
        self.saves -- the text file"""
        self.saves = open(os.path.dirname(__file__) + r"/test_saves.txt", 'r+')
        
        for i in self.get_website_objs():
            self.saves.write('#\n')
            self.saves.write('webname=' + i + '\n')
            print('closing')
            print([i.name for i in self.get_website_objs()[i].getprocedure()])
            for y in self.get_website_objs()[i].getprocedure():
                if y.name in self.get_website_objs()[i].track_variables:
                    self.saves.write(y.name + "=" + y.write_self() + '\n')
                elif y.type == 'xpath_sendkey':
                    self.saves.write("send_key" + "=" + y.write_self() + ' ' + y.need_clear_to_str() + '\n')
                else:
                    self.saves.write(y.write_self()+'\n')
        self.saves.close()
        self.saves = None
        self._file = None
        self._websites = None
        
    def open(self):
        """opens the text file associated with
        the local database."""
        self.assertion()
        
    def assertion(self):
        """Asserts that all my necessary variables have been instantiated or not null"""
        if self.saves is None or []:
            #CODE HERE
            for line in self._file:
                self._saves.append(line)
        if self._file == None or []:
            #CODE HERE
            self._file = open(self._file_path, self._handler)
        if self.get_website_objs() is None or []:
            #CODE HERE
            self.collect_websites()
            
    
    def get_website_objs(self):
        """returns the dictionary instance, self._websites"""
        #CODE HERE
        return self._websites
        
    def set_website_objs(self, websites):
        """Sets the dictionary, self._websites to the dictionary
         WEBSITES"""
        #CODE HERE
        self._websites = websites
        
    @property
    def saves(self): 
        return self._saves
    @saves.setter 
    def saves(self, saver):
        self._saves = saver
    
    
    def write(self, website_obj):
        """need to fix write for rewriting file from scratch when 
        saving current websites and how to delete website from txt.
        Will add a website object to the dictionary and then resave 
        all website objects in dictionary to local database object's 
        designated text file
        """
    
        self._handler = "r+"
        self.saves = None
        self.assertion()
        self.get_website_objs()[website_obj.getwebname()] = website_obj
        self.close()
        self.open()