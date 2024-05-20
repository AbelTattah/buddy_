# Importing flask from the flask library
from flask import Flask,render_template,request,jsonify
# Import Json
import json
# Import gevent

from scrapers import book_scraper
from gevent.pywsgi import WSGIServer
from flask_cors import CORS

app  = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/geturl',methods = ['POST'])
def url():
    keyword = request.json
    word = keyword["keywords"]
    titles, links = book_scraper.scrape(book_scraper.format_search_keyword(word))
    return jsonify({"titles":titles,"links":links})

if __name__ == '__main__':
    # Running the server
    server = WSGIServer(('', 3000), app)
    server.serve_forever()
