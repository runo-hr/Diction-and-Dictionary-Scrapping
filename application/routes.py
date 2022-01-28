from flask import  render_template, request, jsonify, redirect, url_for, flash
from application import app
from application.scrape import Scraper, Compare, URL
import json

all_pages = []

@app.route('/', methods=["POST", "GET"])
def home_page():
    """ Returns a list of urls retrieved from html form """
    if len(all_pages) > 0:
        all_pages.clear()
    u = URL()
    if request.method == 'POST':
        #pages = []
        i=1
        while True:
            try:
                page = request.form[f"page_{i}"]
                if u.url_validator(page):
                    #pages.append(page)
                    all_pages.append(page)
                    i+=1
                else:
                    flash(f'Please provide a valid URL', category='danger')
                    break
            except KeyError:
                if len(all_pages) == 1:
                    return results_page(all_pages[0])
                else:
                    return compare_pages(all_pages)
    return render_template('index.html')

def one_page(page):
    """Returns a dictionary of attributes from the Scraper class """
    page_data = {}
    chart_data = {}

    scraper = Scraper(page)

    frequent = scraper.most_freq
    words = list(frequent.keys())
    freq = list(frequent.values())
    chart_data['words'] = words
    chart_data['freq'] = freq
    chart_data = json.dumps(chart_data)

    sorted_count = scraper.sorted_count[::-1]

    page_data['title'] = scraper.title
    page_data['url'] = scraper.url
    page_data['chart'] = chart_data
    page_data['sorted_count'] = sorted_count
    page_data['alphanums'] = scraper.alphanum_words

    return page_data

@app.route('/results', methods=["POST", "GET"])
def results_page(page):
    """ Passes scraping results of one page to results.html"""
    page_data = one_page(page)
    return render_template('results.html', page_data=page_data)

@app.route('/compare', methods=["POST", "GET"])
def compare_pages(pages):
    """ Passes comparison results of different pages to the frontend """
    c = Compare(pages)
    comparison_data = {}

    comparison_data['title'] = c.heading
    comparison_data['in all'] = c.in_all
    comparison_data['combinations'] = c.combinations_of_two

    dynamic_data = []
    for idx,page in enumerate(pages):
        per_page = {}
        s = Scraper(page)
        per_page['title'] = s.title
        per_page['idx'] = idx
        dynamic_data.append(per_page)

    comparison_data['dynamic data'] = dynamic_data

    return render_template('compare.html', comparison_data=comparison_data)

@app.route('/results/<int:n>', methods=["POST", "GET"])
def dynamic_page(n):
    """ Handles routing to different pages from comparison results
        Receives post requests from the different pages of comparison results
    """
    if request.method == 'POST':
        return home_page()
    page = all_pages[n]
    page_results = one_page(page)
    return render_template('results.html', page_data=page_results)

