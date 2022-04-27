from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import local_database as database_scalp
import os 
"""
    1. load and create all website objects from database_scalpy and text file 
    2. open driver windows for each website data obj, possibly using a class file that can manage all driver windows or assign as a new class variable for a website obj 
    3. run through queue of xpath elements or sen_key or url links, or any other necessary elements
    4. run process on loop for each obj, once done ask user again for reloop, and have mothods for adding or removing website objects
"""
    
class websitedriver():
    """A class that control a selenium window as well 
    as all website objects and database object at run time.
    
    """
    
    def __init__(self, website_obj):
        # A path location to the chromium webdriver
        #self.path = os.path.dirname(__file__) +"/chromedriver.exe"
        
        # A Selemium webdriver object created from self.path
        self._driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        # A website object associated with the website driver
        self._website_obj = website_obj
    def wait(self, time):
        self.Driver.implicitly_wait(time)
    @property
    def website_obj(self):
        return self._website_obj
    @website_obj.setter
    def website_obj(self, website_obj):
        self._website_obj = website_obj
    @property
    def Driver(self):
        return self._driver
    @Driver.setter
    def Driver(self, driver):
        self._driver = driver
        
        
def buy(websitedriver, website_obj_procedure):
    """Function for checking out a product with a given WEBSITEDRIVER
    and a WEBSITE OBJECT's PROCEDURE.
    
    This function will use a webdriver, and parse through a websiteobject.procedure,
    which is a queue of WEBSITE ELEMENTS.
    
    The types of WEBSITE ELEMENTS that exist in our code so far:
    
    1. xpath_button:
        A clickable button that one should use the selenium click function on.
    2. url:
        A url of a destination we want our webdriver to load, 
        Use the selenium function that loads urls
    3. xpath_sendkey:
        A WEBBITE ELEMENT with an xpath to a text box, This is a 
        special website element where one checks if WEBSITE_ELEMENT needs 
        to clear default text out of the text box. After clearing text if needed,
        use the selenium function to send the WEBSITE_ELEMENT name property 
        to the text box.
    4. xpath_select_value:
        A WEBSITE_ELEMENT that is a drop down list and an element needs to be 
        selected from it. An example is when one is selecting a state from a drop 
        down list of different states when a user is selecting
        shipping.
    5. timer:
        If a WEBSITE_ELEMENT type is timer. It is a designated time for the
        selenium webdriver to wait implemented by the user. Use the time.sleep
        feature with time contained by WEBSITE_ELEMENT element property"""
    random.seed()
    for i in website_obj_procedure:
        if i.type == 'xpath_button':
            try:
                button = websitedriver.Driver.find_element_by_xpath(i.element)
                button.click()
                time.sleep(random.uniform(1.0, 13.5))
            except:
                raise Exception(i.type + ' ' + i.name +' did not work from ' + i.element)
                pass
        elif i.type == 'url':
            print('url ran')
            try:
                websitedriver.Driver.get(i.element)
                time.sleep(random.uniform(3.0, 13.5))
            except:
                raise Exception(i.type + ' ' + i.name +' did not work')
                pass
        elif i.type == 'xpath_sendkey':
            try:
                text_box = websitedriver.Driver.find_element_by_xpath(i.element)
                if i.need_clear:
                    text_box.clear()
                    time.sleep(random.uniform(1.0, 13.5))
                
                    
                text_box.send_keys(i.name)
                time.sleep(random.uniform(1.0, 13.5))
            except:
                raise Exception(i.type + ' ' + i.name +' did not work')
                pass
        elif i.type == 'xpath_select_value':
            try:
                sel = Select(websitedriver.Driver.find_element_by_xpath(i.element))
                sel.select_by_value(i.name)
                time.sleep(random.uniform(1.0, 13.5))
            except:
                raise Exception(i.type + ' ' + i.name +' did not work')
                pass
        elif i.type == 'timer':
            try:
                
                time.sleep(float(i.element))
            except:
                raise Exception(i.type + ' ' + i.name +' did not work')
                pass
        else:
            raise Exception(i.type + ' ' + i.name +' did not meet any of the criteria')
            pass
def show_driver(websitedriver, bool):
    """Function to fullscreen the selenium driver 
    on the users screen."""
    if bool:
        websitedriver.Driver.maximize_window()