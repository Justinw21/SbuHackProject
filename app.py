from re import search
from unittest import result
from flask import Flask, render_template, request
from twilio.rest import Client
import os
import db


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def main():
    search = request.form.get("search")
    options = request.form.get("options")
    number = request.form.get("number")

    

    account_sid = "AC24785ce0decacf8e0d2fca5362a64c09"
    auth_token  = "a1430f49bfcb2ace6f183c9a1fbdea18"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+1" + number, 
        from_="++15618162572",
        body="Hello from Python!")

    print(message.sid)
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
