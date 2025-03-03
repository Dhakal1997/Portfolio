from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup 


app = Flask(__name__)

# Landing page route
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route('/scraping', methods=['GET', 'POST'])
def scraping():
    titles = []
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            titles = [title.get_text() for title in soup.find_all('h2')]
        except Exception as e:
            titles = [f"An error occurred: {str(e)}"]
    return render_template('scraping.html', titles=titles)


if __name__ == "__main__":
    app.run(debug=True)
