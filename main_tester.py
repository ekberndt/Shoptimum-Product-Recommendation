
import autobuy_code as scalpbot_code
import local_database as database_scalp
beta = open(r"local_saves.txt", "r+")
main = database_scalp.local_database(r"local_saves.txt", "r+")
#main.write_to_json('local_saves.JSON')
#main.json_to_obj('local_saves.json')
main.close()
main.open()

"""gamma = beta.readlines()
print(gamma)
print(gamma[0].split())
gamma = database_scalp.converttoobj(database_scalp.website_dataobj(), gamma)

print(gamma.procedure)
for i in gamma.procedure:
    print(i.name, i.type)"""


"""gamma = beta.readlines()
alp = database_scalp.convertalltoobj(gamma)
print(alp)"""

print(main.get_text())
print(main.get_website_objs())
driver = scalpbot_code.websitedriver(main.get_website_objs()["Amazon2"])
driver.wait(5)
"""print('********')
print(main.get_website_objs()["Amazon"].getprocedure is main.get_website_objs()['Walmart'].getprocedure)
print(main.get_website_objs()['Walmart'].getprocedure())
for i in main.get_website_objs()['Walmart'].getprocedure():
    print(i.name, i.type, i.element)
print('amazons turn')"""
"""for i in main.get_website_objs()["Amazon"].getprocedure():
    print(i.name, i.type, i.element)"""
    
scalpbot_code.show_driver(driver, True)
scalpbot_code.buy(driver, driver.website_obj.getprocedure())
