# Importing flask from the flask library
from flask import Flask,render_template,request,jsonify
# Import Json
import json
# Import gevent

from scrapers import book_scraper
from gevent.pywsgi import WSGIServer
from flask_cors import CORS

app  = Flask(__name__)

book = book_scraper.Scrape()

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
    titles, links, images = book.scrape(book.format_search_keyword(word))
    return jsonify({"titles":titles,"links":links,"images":images})

if __name__ == '__main__':
    # Running the server
    print("server is live...")
    server = WSGIServer(('', 3400), app)
    server.serve_forever()
