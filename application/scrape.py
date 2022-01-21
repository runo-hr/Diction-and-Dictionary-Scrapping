import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import itertools

class Scraper:
    def __init__(self, url):
        self.url = url
        self.title = ""
        self.count_dict = {}
        self.sorted_count = []
        self.unique_words = set()
        self.scrape_page(self.url)
        self.most_freq = self.most_frequent() #dict

    def scrape_page(self, url):
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
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
        clean_lst = []
        for word in words_list:
            for i in range(len(symbols)):
                word = word.replace(symbols[i], '')
            if len(word) > 0:
                clean_lst.append(word)
        return self.word_frequency(clean_lst)

    def word_frequency(self, clean_lst):
        for word in clean_lst:
            self.count_dict[word] = self.count_dict.get(word, 0) + 1
        self.sorted_count = sorted(self.count_dict.items(), key=lambda kv: kv[1])
        self.unique_words = set(self.count_dict.keys())
        return self.most_frequent()

    def most_frequent(self, n=10):
        c = Counter(self.count_dict)
        top = c.most_common(n)
        return dict(top)

class Compare(Scraper):
    def __init__(self, *urls):
        self.word_sets = []
        self.titles_n_sets = []
        self.heading = ''

        for url in urls:
            super().__init__(url)
            if urls.index(url) != len(urls) - 1:
                self.heading += f"{self.title} | "
            else:
                self.heading += f"{self.title}"
            self.word_sets.append(self.unique_words)
            self.titles_n_sets.append((self.title, self.unique_words))

        self.in_all = self.common_in_all(self.titles_n_sets)
        self.only_in_first = self.only_in_one(self.titles_n_sets)
        self.combinations_of_two = self.two_combinations(self.titles_n_sets)

    def common_in_all(self, titles_n_sets):
        output = {}
        temp = titles_n_sets[0][1]
        i = 1
        while i < len(titles_n_sets):
            temp = temp & titles_n_sets[i][1]
            i += 1
        output['Common in all pages'] = temp
        return output

    def only_in_one(self, titles_n_sets):
        output = {}
        temp = titles_n_sets[0][1]
        i = 1
        while i < len(titles_n_sets):
            temp = temp - titles_n_sets[i][1]
            i += 1
        output[f"Only in {titles_n_sets[0][0]}"] = temp
        return output

    def two_combinations(self, titles_n_sets):
        all_combs = []
        for x,y in itertools.combinations(titles_n_sets, 2):
            combs = {}
            combs['Heading'] = f"{x[0]} vs {y[0]}"
            combs[f"Common in Both"] = x[1] & y[1]
            combs[f"Only in {x[0]}"] = x[1] - y[1]
            combs[f"Only in {y[0]}"] = y[1] - x[1]
            all_combs.append(combs)
        return all_combs


