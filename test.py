# import website_element2 as website_element
from website_element import WebsiteElement
# import website_obj
from website_obj import WebsiteObject
# import local_database
from local_database import local_database
import sys, os
database1 = local_database(r"test.txt", "r+");
obj1 = WebsiteObject('Ebay', 'https://www.ebay.com/')
obj1.append_command(WebsiteElement('.//a//h3[@class="s-item__title"]', 'name', 'xpath_select_value', False))
obj1.append_command(WebsiteElement('.//span[@class="s-item__price"]', 'price', 'xpath_select_value', False))
obj1.append_command(WebsiteElement('.//div[@class="x-star-rating"]/span[@class="clipped"]', 'rating', 'xpath_select_value', False))

obj2 = WebsiteObject('Etsy', 'https://www.etsy.com/')
obj2.append_command(WebsiteElement('.//h3[contains(@class, "wt-text-caption")]', 'name', 'XPATH', False))
obj2.append_command(WebsiteElement('.//span[@class="currency-value"]', 'price', 'xpath_button', False))
obj2.append_command(WebsiteElement('.//input[contains(@name, "rating")]', 'rating', 'XPATH', False))

dict = {}
dict[obj1.getwebname().name] = obj1
dict[obj2.getwebname().name] = obj2
database1.set_website_objs(dict)
print("checking dict")
for i in database1.get_website_objs():
    print(i)
database1.write_to_json(os.path.dirname(__file__) + r"/database.json")
# print("hi")