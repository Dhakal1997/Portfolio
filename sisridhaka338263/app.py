import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    with open('static/data.json') as f:
        data = json.load(f)
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)