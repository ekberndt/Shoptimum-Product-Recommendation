from json_text_func import *
from website_obj import *
from website_element import *
import json
import os

class local_database():
    def __init__(self, file_path = "", handler = ""):
        
        # file path of text file
        self._file_path = file_path
        # mode to open text file in (a, w, r, r+)
        self._handler = handler 
        self._isJSON = False;
        # reference to text file
        self._saves = open(self._file_path, self._handler)
        if ".txt" in file_path:
            # turns next file into list a strings line by line
            self._text = self.saves.readlines()
            # creates dictionary of website objects from _text
            self.collect_websites()
            #self.assertion()
        elif ".json" in file_path:
            self._isJSON = True;
            self.collect_websites()
        else:
            
            # turns next file into list a strings line by line
            self._text = self.saves.readlines()
            # creates dictionary of website objects from _text
            self.collect_websites()
        
    def get_file(self):
        #self.assertion()
        return self.saves
    def get_text(self):
        
        return self._text
    
    
    def collect_websites(self):
        "loads website objs into dictionary"
        self.set_website_objs(convertalltoobj(self.get_text()))
        
     
    def write_to_json(self, json_file):
        """write my current dictionary of all website objs to a JSON file""" 
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
        """open a json file to load json website objs into my dictionary"""
        with open(json_file) as f:
            x = json.load(f)
            d = {}
            for i in x:
                temp_website_holder = convert_dict_to_obj(i, WebsiteObject())
                d[temp_website_holder.getwebname().name] = temp_website_holder
            self.set_website_objs(d)
            
        
            
    def close(self):
        self.saves = open(os.path.dirname(__file__) + r"/local_saves.txt", 'r+')
        """self._handler = "r+"
        self.saves = None
        self.assertion()
        self.saves.truncate(0)"""
        
        if self._isJSON:
            self.write_to_json(self._file_path)
        else:
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
        self._text = None
        self._websites = None
    def open(self):
        self.assertion()
    def assertion(self):
        if self.saves is None or []:
            self.saves = open(self._file_path, self._handler) 
        if self._text == None or []:
            self._text = self.saves.readlines() if not self._isJSON else None
        if self.get_website_objs() is None or []:
            self.collect_websites() 
    def get_website_objs(self):
        
        return self._websites
    def set_website_objs(self, websites):
        self._websites = websites
    @property
    def saves(self): 
        return self._saves
    @saves.setter 
    def saves(self, saver):
        self._saves = saver
    
    
    def write(self, website_obj):
        """need to fix write for rewriting file from scratch when 
        saving current websites and how to delete website from txt"""
        
        self._handler = "r+"
        self.saves = None
        self.assertion()
        self.get_website_objs()[website_obj.getwebname()] = website_obj
        self.close()
        self.open()
        