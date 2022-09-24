from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def main():
    search = request.form.get("search")
    options = request.form.get("options")
    return options

if __name__ == "__main__":
    is_prod = os.environ.get('IS_HEROKU', None)
    if is_prod:
        app.run()
    else:
        app.run(host='0.0.0.0', port=81, debug=True)
