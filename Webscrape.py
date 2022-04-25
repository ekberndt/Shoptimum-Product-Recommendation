from importlib.resources import Package
import Product
import Websites.Amazon
import os

def webscrape(search_query):
    all_products = []
    Amazon_thread = Websites.Amazon.find_products(search_query)
    all_products.extend(Amazon_thread)
    all_products = rank(all_products)
    print_ranked_Products_to_JSON(all_products)

def print_ranked_Products_to_JSON(all_products):
    # To reset json file and open square bracket
    with open("product_info.json", "w") as f:
        print('[', file=f)

    for i in range(len(all_products)):
        all_products[i].print_product_to_json()

    with open("product_info.json", "a") as f:
        # Remove last unnessecary comma added in json by print_product_to_json
        # Seek to the end of the file
        f.seek(0, os.SEEK_END)
        # Go back three characters
        f.seek(f.tell() - 3, os.SEEK_SET)
        
        f.truncate()
        # To close bracket on json file
        print("\n]", file=f)

def rank(all_products):
    # TODO: add ranking algorithm here
    return all_products
