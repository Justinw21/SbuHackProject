from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def main():
    search = request.form.get("search")
    options = request.form.get("options")
    number = request.form.get("number")
    return search + " " + options + " " + number

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)