import Product
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def find_products(search_query):
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=" + search_query + "&_sacat=0"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    driver.implicitly_wait(2)
    elements = driver.find_elements(By.XPATH, '//li[contains(@data-view, "mi:")]')
    count = 0
    ebay_product = []
    driver.implicitly_wait(0)

    for element in elements:
        #count
        count += 1

        try:
            name = element.find_element(By.XPATH, './/a//h3[@class="s-item__title"]').text
        except:
            name = ""
                 
        #price
        try: 
            price = element.find_element(By.XPATH, './/span[@class="s-item__price"]').text
        except:
            price = ""
        
        #rating
        try:
            rating = element.find_element(By.XPATH, './/div[@class="x-star-rating"]/span[@class="clipped"]').text
        except:
            rating = "N/A"
        
        #number of ratings
        try:
            numberOfRate = element.find_element(By.XPATH, './/span[@class="s-item__reviews-count"]/span[not(@class="clipped")]').text
        except:
            numberOfRate = 0
        
        #product link
        try:
            link = element.find_element(By.XPATH, '//a[@class="s-item__link"]').get_attribute('href')
        except:
            link = ""
        
        #image link
        try:
            imgLink = element.find_element(By.XPATH, './/img[@class="s-item__image-img"]').get_attribute('src')
        except:
            imgLink = ""

        product = Product.Product(name, price, rating, numberOfRate, count, link, imgLink)
        ebay_product.append(product)

    return ebay_product