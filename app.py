from re import search
from unittest import result
from flask import Flask, render_template, request
import os
import db


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert')
def insert_page():
    return render_template('insert.html')

@app.route('/insert', methods=['POST'])
def add_from_page():
    url = request.form.get("url")
    price = request.form.get("price")
    rating = request.form.get("rating")
    review_count = request.form.get("review_count")
    arrival_date = request.form.get("arrival_date")
    db.insert(url, price, rating, review_count, arrival_date)
    return [url, price, rating, review_count, arrival_date]

@app.route('/', methods=['POST'])
def main():
    search = request.form.get("search")
    options = request.form.get("options")
    number = request.form.get("number")
    return search + " " + options + " " + number

@app.route('/db')
def shopping():
    return db.showall()

if __name__ == "__main__":
    is_prod = os.environ.get('IS_HEROKU', None)
    if is_prod:
        app.run()
    else:
        app.run(host='0.0.0.0', port=81, debug=True)
