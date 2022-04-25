# Used to webscrape for product information
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import Product

def find_products(search_query):
    # Start webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    found_products = []

    num_of_product = 1
    # Driver searches through several pages of search results
    for page_num in range(1, 2):
        driver.get("https://www.amazon.com/s?k="+ search_query + "&page=" + str(page_num))
        
        # To prevent the driver from searching for an element before the element has loaded on the webpage,
        # the driver will now wait 5 seconds for the element to load
        driver.implicitly_wait(5)

        # Searches for div tag with data-cel-widget attribute that has "search_result_(num here)"
        # to find location of every product on the page
        # We use find_elements to find every product on that page, not just one
        search_results = driver.find_elements(By.XPATH, '//div[contains(@data-cel-widget, "search_result_")]')
        print("num of products on page: ", len(search_results))

        # Since the webpage is already loaded and some elements aren't located on the page (ex: Product has no
        # ratings or price is not listed) the driver doesn't wait 5 seconds everytime it can't find an element
        driver.implicitly_wait(0)

        # The last four "search_result" items in search_results are not products but other elements on the page, so
        # the elements are removed
        search_results = search_results[:-4]
        
        # For each result found, locate its repective data
        for search_result in search_results:
            try:
                try:
                    # Adding a dot in front of the xpath makes selenium search just within "search_result", rather than the whole page
                    product_name = search_result.find_element(By.XPATH, './/span[@class="a-size-base-plus a-color-base a-text-normal"]').text
                except:
                    # If an element is not found, variable is set to empty string so code does not crash
                    product_name = ""
                
                try:
                    whole_num_price = search_result.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
                except:
                    whole_num_price = ""

                try:
                    decimal_price = search_result.find_element(By.XPATH, './/span[@class="a-price-fraction"]').text
                except:
                    decimal_price = ""

                try:
                    price = int(whole_num_price) + int(decimal_price) / 100
                except:
                    price = ""

                try:
                    avg_review_score = search_result.find_element(By.XPATH, './/span[contains(@aria-label, " out of ")]').get_attribute("aria-label")
                except:
                    avg_review_score = "N/A"
                
                try:
                    num_of_reviews = search_result.find_element(By.XPATH, './/span[@class="a-size-base s-underline-text"]').text
                except:
                    num_of_reviews = 0

                try:
                    product_url = search_result.find_element(By.XPATH, './/div//h2//a[contains(@href, "")]').get_attribute("href")
                except:
                    product_url = ""

                try:
                    img_url = search_result.find_element(By.XPATH, './/img').get_attribute('src')
                except:
                    img_url = ""
                
                item = Product.Product(product_name, price, avg_review_score, num_of_reviews, num_of_product, product_url, img_url)
                found_products.append(item)
                num_of_product += 1
            except Exception as e:
                print(e)

    driver.quit()
    
    return found_products
