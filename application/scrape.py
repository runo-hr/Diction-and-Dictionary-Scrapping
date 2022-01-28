import requests
from bs4 import BeautifulSoup
from collections import Counter
import itertools
from urllib.parse import urlparse

class URL:
    def url_validator(self, url):
        """Returns True if url is valid and False otherwise"""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc, result.path])
        except:
            return False

class Scraper:
    def __init__(self, url):
        self.url = url
        self.title = ""
        self.count_dict = {}
        self.sorted_count = []
        self.alphanum_words = []
        self.unique_words = set()
        self.scrape_page(self.url)
        self.most_freq = self.most_frequent() #dict

    def scrape_page(self, url):
        """ Calls the clean_words method with a list of all words on a page"""
        words_list = []
        source_code = requests.get(url).text
        soup = BeautifulSoup(source_code, 'html.parser')
        self.title = soup.find('title').text
        content = soup.find('body')
        for item in content:
            sentence = item.text
            words = sentence.lower().split()
            for word in words:
                words_list.append(word)
        return self.clean_words(words_list)

    def clean_words(self, words_list):
        """ Removes symbols from all words of the page
            Appends all words with numbers to self.alphanum_words
            Calls self.word_frequency with a list of cleaned words
        """
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
        clean_lst = []
        for word in words_list:
            word = word.strip()
            for i in range(len(symbols)):
                word = word.replace(symbols[i], '')
            if len(word) > 0 and not self.has_digit(word) and word not in symbols :
                clean_lst.append(word)
            elif self.has_alphanum(word):
                self.alphanum_words.append(word)
        return self.word_frequency(clean_lst)

    def has_digit(self, word):
        """Returns True if word has a number or is a number, else False"""
        # next() checking for each element, reaches end, if no element found as digit
        res = True if next((chr for chr in word if chr.isdigit()), None) else False
        return res

    def has_alphanum(self, word):
        """ Returns True if word has noth letters and numbers, else False"""
        if any(chr.isalpha() for chr in word) and any(chr.isdigit() for chr in word):
            return True
        else:
            return False

    def word_frequency(self, clean_lst):
        """Creates a dictionary of words and their count of occurrence
           Creates a set of all words on the page
        """
        for word in clean_lst:
            self.count_dict[word] = self.count_dict.get(word, 0) + 1
        self.sorted_count = sorted(self.count_dict.items(), key=lambda kv: kv[1])
        self.unique_words = set(self.count_dict.keys())

    def most_frequent(self, n=10):
        """Returns a dictionary of the top ten most frequent words"""
        c = Counter(self.count_dict)
        top = c.most_common(n)
        return dict(top)

class Compare(Scraper):
    def __init__(self, urls):
        self.word_sets = []
        self.titles_n_sets = []
        self.heading = ''

        for url in urls:
            super().__init__(url)
            new_line = '\n'
            if urls.index(url) != len(urls) - 1:
                self.heading += f"{self.title} {new_line} vs  "
            else:
                self.heading += f"{new_line} {self.title}"
            self.word_sets.append(self.unique_words)
            self.titles_n_sets.append((self.title, self.unique_words))

        self.in_all = self.common_in_all(self.titles_n_sets) #set
        self.only_in_first = self.only_in_one(self.titles_n_sets)
        self.combinations_of_two = self.two_combinations(self.titles_n_sets)

    def common_in_all(self, titles_n_sets):
        """Uses set intersection to find words present in all pages
            Each set in titles_n_sets belongs to a page
        """
        temp = titles_n_sets[0][1]
        i = 1
        while i < len(titles_n_sets):
            temp = temp & titles_n_sets[i][1]
            i += 1
        return temp

    def only_in_one(self, titles_n_sets):
        """Uses set difference to find words only present in the first page"""
        output = {}
        temp = titles_n_sets[0][1]
        i = 1
        while i < len(titles_n_sets):
            temp = temp - titles_n_sets[i][1]
            i += 1
        output[f"Only in {titles_n_sets[0][0]}"] = temp
        return output

    def two_combinations(self, titles_n_sets):
        """Compares each page with every other using set intersection and difference operations"""
        all_combs = []
        for x,y in itertools.combinations(titles_n_sets, 2):
            combs = {}
            combs['Heading'] = f"{x[0]} vs {y[0]}"
            combs[f"Common in Both"] = x[1] & y[1]
            combs[f"Only in {x[0]}"] = x[1] - y[1]
            combs[f"Only in {y[0]}"] = y[1] - x[1]
            all_combs.append(combs)
        return all_combs


