from dotenv import load_dotenv
from flask import Flask, request, redirect, jsonify, render_template, url_for
from flask_cors import CORS, cross_origin
import requests
from random import randint
import json
import os
import sys
import autobuy_code as scalpbot_code
import local_database as database_scalp
from website_element import WebsiteElement as website_element
from website_obj import WebsiteObject as website_dataobj
load_dotenv()
# Set up the app
app = Flask(__name__, static_folder='../client/build/',    static_url_path='/')
# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')



"""sys.path.append('c:/users/chowm/downloads')
import bearycal_diningapi as bc"""



cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

api_key = "wf1-IYsyEoU-CgmrkC0m9RqQpnckeqPaiYG2NNhLzAlH7Nqb6f2WtDvpdD7mir8pm_RL7uVGfI5WUpe1fWl7kuIHlDbIYRTHpqUnoLirhziejFWoNA1JeWnHFvDiXXYx"


@app.route('/yelp', methods = ["GET"] )
def yelp_rec():
    #headers = {'Authorization': 'Bearer %s' % api_key}
    #r = requests.request(
    #    'GET', f"https://api.yelp.com/v3/businesses/search?term=chinese", headers=headers, params=None)
    #print(r.content)
    return "<p>Hello</p>"
    # if request.method == "POST":
    #     price = request.json['price']
    #     rating = int(request.json['rating'])
    #     distance = int(request.json['distance'])
    #     cuisine = request.json['cuisine']
    # # Default Berkeley coordinates
    #     latitude = 37.866948799999996
    #     longitude = -122.2531663

    #     headers = {'Authorization': 'Bearer %s' % api_key}
    #     r = requests.request(
    #         'GET', f"https://api.yelp.com/v3/businesses/search?={cuisine}latitude={latitude}&longitude={longitude}&radius={distance}&categories={cuisine}", headers=headers, params=None)
    #     places = r.json()

    #     places_by_cusine = []
    #     for business in places['businesses']:
    #         for category in business['categories']:
    #             if category['alias'] == cuisine and business['rating'] >= rating and not business['is_closed']:
    #                 places_by_cusine.append(business)

    #     # This randomly chooses one restaurant, but we want something that outputs all restaurants?
    #     # number = len(places_by_cusine)
    #     # pick = randint(0, number - 1)
    #     # choice = places_by_cusine[pick]
    #     return places_by_cusine


#x = bc.apikey()
"""yelp_api_key = os.environ['YELP_TOKEN']
caldining_api_key = os.environ['CALDINING_TOKEN']"""
#caldining_api_key = x.getapi()
caldining_api_key = '7d3f45db83msh3471806ea5421a7p11c24fjsn8955a8c1e20f'

@app.route("/dining_hall", methods=["GET", "POST"])
def dining_hall_rec():
    """url = "https://caldining.p.rapidapi.com/menu"
    headers = {
        'x-rapidapi-key': caldining_api_key,
        'x-rapidapi-host': "caldining.p.rapidapi.com"
    }    
    response = requests.request("GET", url, headers=headers)
    result = json.loads(json.loads(response.text))"""
    
    headers = {'x-rapidapi-host': 'caldining.p.rapidapi.com',
    'x-rapidapi-key': caldining_api_key }
    r = requests.request('GET', f"https://caldining.p.rapidapi.com/menu", headers=headers, params=None)
    dining_halls = r.json()
    dining = json.loads(dining_halls)
    dict = {}
    for i in range(len(dining)):
        dict[i] = dining[i]
    return dict
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/add_website_JSON', methods=['POST'])
def add_website_JSON():
    if request.method == 'POST':
        r = request.get_json(force=True)
        #temp = json.loads(r)
        re = r
        #re = {}
        """for i in range(len(temp)):
            re[i] = temp[i]"""
        
        main = database_scalp.local_database(os.path.dirname(__file__) + r"/local_saves.txt", "r+")
        new_website = database_scalp.website_dataobj()
        new_website.setwebname(database_scalp.website_element(re["webname"].split()[0], re["webname"].split()[0], "webname"))        
        new_website.setweburl(database_scalp.website_element(re["web_url"].split()[0], "web_url", "url") ) 
        new_website.append_command(new_website.getweburl())
        
        i = 0
        countoferror = 0
        while(True):
            try:
                if "xpath_sendkey" in re["xpath" + str(i)]:
                    
                    line_of_words = "send_key=" + re["xpath" + str(i)]
                    array = ['#\n', line_of_words, '#\n']
                else:
                    line_of_words = re["xpath" + str(i)]
                    array = ['#\n', line_of_words, '#\n'] #dont need to add hastag at the end as coverttoobj quits after no lines are left
                    #^^^ basically recreating a substitution of the readlines() function from txt file to work with converttoobj
                    print('adding website')
                    print(array)
                var = database_scalp.converttoobj(new_website, array)
                i += 1
            except:
                if countoferror > 5:
                    break
                else:
                    countoferror += 1
                    i += 1
                    pass
        main.get_website_objs()[new_website.getwebname().element] = new_website
        main.close()
    return jsonify({'msg' : 'Successfully added Website!'})

@app.route('/addProduct', methods=["POST"])
def addProduct():
    if request.method == 'POST':
        r = request.get_json(force=True)
        
        with open("container.json", "a") as f:
            print('[', file=f)
            json.dump(r, f, indent=4)
            print(",", file=f)
            f.seek(0, 2)
            #f.tell tells where the cursor is currently at
            f.seek(f.tell() - 3, os.SEEK_SET)
            f.truncate()
            print('\n]', file = f)
            
@app.route('/getProduct', methods=["GET"])
def getProduct():
        if request.method == 'GET':
            f = open(os.path.dirname(__file__) + r"/container.json")
            link = json.loads(f.read())
            #d = [i for i in link.keys()]
            d = []
            for i in link:
                d.extend([y for y in i.keys()])
            return jsonify(d)
@app.route('/getWebObj', methods=["GET"])
def getWebObj():
    if request.method == "GET":
        main = database_scalp.local_database(os.path.dirname(__file__) + r"/local_saves.txt", "r+")
        d = {}
        
        d = main.get_website_objs()
        d = [i for i in d.keys()]
        return jsonify(d)
@app.route('/implement', methods=["POST"])
def implement():
    if request.method == "POST":
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
        return "done"
        
@app.route("/add_website", methods=["POST"])
def add_website():
    if request.method == "POST":
        main = database_scalp.local_database(os.path.dirname(__file__) + r"/local_saves.txt", "r+")
        new_website = database_scalp.WebsiteObject()
        new_website.setwebname(database_scalp.website_element(request.form.get("webname").split()[0], request.form.get("webname").split()[0], "webname"))        
        new_website.setweburl(database_scalp.website_element(request.form.get("web_url").split()[0], "web_url", "url") ) 
        new_website.append_command(new_website.getweburl())
        
        i = 0
        countoferror = 0
        while(True):
            try:
                if "xpath_sendkey" in request.form.get("xpath" + str(i)):
                    
                    line_of_words = "send_key=" + request.form.get("xpath" + str(i))
                    array = ['#\n', line_of_words]
                else:
                    line_of_words = request.form.get("xpath" + str(i))
                    array = ['#\n', line_of_words]
                    print('adding website')
                    print(array)
                var = database_scalp.converttoobj(new_website, array)
                i += 1
            except:
                if countoferror > 5:
                    break
                else:
                    countoferror += 1
                    i += 1
                    pass
        main.get_website_objs()[new_website.getwebname().element] = new_website
        main.close()
        response = {
           'Animal': "Dog"}
        try:
            return jsonify(response)
        except:
            return "did not work"
    
                

if __name__ == '__main__':
    app.run(port=5000, debug = True)