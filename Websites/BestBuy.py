# Used to webscrape for product information
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import Product

def find_products(search_query):
    # Start webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bestbuy.com/site/searchpage.jsp?st=" + search_query + "&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys")

    found_products = []
    num_of_product = 1

    driver.implicitly_wait(2)
    content = driver.find_elements(By.CLASS_NAME, 'sku-item')

    for e in content:
        # product = dict()
        try:
            titleElement = e.find_element(By.CLASS_NAME, 'sku-title')
            product_name = titleElement.text
        except:
            product_name = ""

        try:
            price = e.find_element(By.CLASS_NAME, "priceView-customer-price")
            product_price = price.text.split()[0] #probably need to parse later to get just the number. current: "$69.69"
        except:
            product_price = ""

        try:
            reviewInfo = e.find_element(By.CLASS_NAME, "visually-hidden")
            parsed = [word for word in reviewInfo.text.split()]
            avg_review_score = parsed[2]
            num_of_reviews = parsed[-2]
        except:
            avg_review_score = ""
            num_of_reviews = 0

        try:
            linkElement = titleElement.find_element(By.LINK_TEXT, product['Title'])
            product_url = linkElement.get_attribute('href')
        except:
            product_url = ""

        try:
            imgElement = e.find_element(By.CLASS_NAME, 'product-image')
            img_url = imgElement.get_attribute('src')
        except:
            img_url = ""

        found_products.append(Product.Product(product_name, product_price, avg_review_score, num_of_reviews, num_of_product, product_url, img_url))
        num_of_product += 1
    
    driver.quit()
    
    return found_products