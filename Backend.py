from flask import Flask, jsonify, render_template, request
import json
import Webscrape

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/webscrape", methods=["POST"])
def webscrape():
    message = request.get_json(force=True)
    Webscrape.webscrape(message['search'])
    response = json.load(open('product_info.json', 'r'))
    return jsonify(response)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True)
