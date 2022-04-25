from socket import AddressFamily
from selenium import webdriver
from selenium.webdriver.common.by import By
import Product
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""Takes in a search key and prints out product info for each search result"""
def find_products(search_key):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.etsy.com/search?q=" + search_key)
    """
    content: product search result section as one element
    sub_contents: list of product elements
    product_lst: list of Product objects containing product info
    """
    content = driver.find_element(By.XPATH, '//ul[contains(@class,"wt-grid wt-grid--block wt-pl-xs-0 tab-reorder-container")]')
    sub_contents = content.find_elements(By.XPATH, './/li[contains(@class, "")]')
    product_lst = []
    
    for i in range(len(sub_contents)):
        # Name
        try:
            name = sub_contents[i].find_element(By.XPATH, './/h3[contains(@class, "wt-text-caption")]').text
        except:
            name = "N/A"
        else:
            name = sub_contents[i].find_element(By.XPATH, './/h3[contains(@class, "wt-text-caption")]').text

        # Price
        try:
            price = sub_contents[i].find_element(By.XPATH, './/span[@class="currency-value"]').text
        except:
            price = "N/A"
        else:
            price = sub_contents[i].find_element(By.XPATH, './/span[@class="currency-value"]').text

        # Rating
        try:
            rating = sub_contents[i].find_element(By.XPATH, './/input[contains(@name, "rating")]').get_attribute('value')
        except:
            rating = "N/A"
        else:
            rating = sub_contents[i].find_element(By.XPATH, './/input[contains(@name, "rating")]').get_attribute('value')
        
        # Number of Ratings
        try:
            num_ratings = sub_contents[i].find_element(By.XPATH, './/span[contains(@class, "wt-text-gray wt-display-inline-block")]').text[1:-1]
        except:
            num_ratings = "N/A"
        else:
            num_ratings = sub_contents[i].find_element(By.XPATH, './/span[contains(@class, "wt-text-gray wt-display-inline-block")]').text[1:-1]

        # Product URL
        try:
            prod_url = sub_contents[i].find_element(By.XPATH, './/a[contains(@class,"listing-link")]').get_attribute('href')
        except:
            prod_url = "N/A"
        else:
            prod_url = sub_contents[i].find_element(By.XPATH, './/a[contains(@class,"listing-link")]').get_attribute('href')

        # Image URL
        try:
            img_url = sub_contents[i].find_element(By.XPATH, './/div[contains(@class,"height-placeholder")]//img').get_attribute('src')
        except:
            img_url = "N/A"
        else:
            img_url = sub_contents[i].find_element(By.XPATH, './/div[contains(@class,"height-placeholder")]//img').get_attribute('src')

        product_lst.append(Product.Product(name, price, rating, num_ratings, i + 1, prod_url, img_url))
    
    return product_lst