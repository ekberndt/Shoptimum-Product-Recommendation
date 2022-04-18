import json

class Product:
    def __init__(self, product_name, price, avg_review_score, num_of_reviews, num_of_product, product_url, img_url):
        self.product_name = product_name
        self.price = price
        self.avg_review_score = avg_review_score
        self.num_of_reviews =  num_of_reviews
        self.num_of_product = num_of_product
        self.product_url = product_url
        self.img_url = img_url

    def print_product_to_json(self):
        data = {"Name": self.product_name, "Price": self.price, "avg Review": self.avg_review_score,
        "num of Reviews": self.num_of_reviews, "num of Product": self.num_of_product, "Location of Product": self.product_url,
        "Image Url": self.img_url}
        # Write JSON data to file
        with open("product_info.json", "a") as f:
            json.dump(data, f, indent=4)
            print(",", file=f)
