from flask import  render_template, request, jsonify, redirect, url_for
from application import app
from application.scrape import Scraper, Detector
import operator
from collections import Counter
import itertools

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
    scraper = Scraper()
    detector = Detector()
    results = []

    for page in pages:
        title, word_freq, available_words = scraper.scrape_page(page)
        results.append({'name': title,
                        'words List': word_freq})

    return render_template('results.html', results=results)





