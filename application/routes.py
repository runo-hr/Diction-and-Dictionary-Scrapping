from flask import  render_template, request, jsonify, redirect, url_for
from application import app
from application.scrape import Scraper
import operator
from collections import Counter
import itertools
import json

@app.route('/', methods=["POST", "GET"])
def home_page():
    if request.method == 'POST':
        pages = []
        i=1
        while True:
            try:
                page = request.form[f"page_{i}"]
                pages.append(page)
                i+=1
            except KeyError:
                return results_page(pages)
    else:
        return render_template('index.html')

@app.route('/results')
def results_page(pages):
    results = []

    for page in pages:
        scraper = Scraper(page)
        title = scraper.title
        frequent = scraper.most_freq
        words = list(frequent.keys())
        freq = list(frequent.values())
        results.append({'name': title,
                        'most frequent': frequent})

    return render_template('results.html', results=results, frequent_words=json.dumps(words),
                           frequency=json.dumps(freq))





