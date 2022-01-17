import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import itertools

class Scraper:
    def scrape_page(self, url):
        words_list = []
        source_code = requests.get(url).text
        soup = BeautifulSoup(source_code, 'html.parser')
        title = soup.find('title').text
        content = soup.find('body')
        for item in content:
            sentence = item.text
            words = sentence.lower().split()
            for word in words:
                words_list.append(word)
        return self.clean_words(words_list, title)

    def clean_words(self, words_list, title):
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
        clean_lst = []
        for word in words_list:
            for i in range(len(symbols)):
                word = word.replace(symbols[i], '')
            if len(word) > 0:
                clean_lst.append(word)
        return self.word_frequency(clean_lst, title)

    def word_frequency(self, clean_lst, title):
        word_count = {}
        for word in clean_lst:
            word_count[word] = word_count.get(word, 0) + 1
        word_freq = sorted(word_count.items(), key=lambda kv: kv[1])
        available_words = set(word_count.keys())
        return title, word_freq, available_words

class Detector:
    def present_in_both(self, x, y):
        return x & y
    def present_in_one(self, x, y):
        return x - y
