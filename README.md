# Diction and Dictionary Scrapping.

## Background Info
I did this project as part of an application for a Junior Developer role at Pesapal.
In this README, I will take you through my approach to the problem, development of the solution and how you can contribute to taking this project past the scope of the problem statement.  

## Problem Statement
Write an application which, when given a web page will download the text on it and output a sorted list of the unique words on the page, with counts of the occurrences.
### Extensions
Consider extending the application to work with a dictionary, or configurable word list, so one can e.g. find the non-English words on the page. Or perhaps provide a way to compare two (or more pages) in terms of words found in both and only in one or the other?

## Possible avenues of application
Where can I use this app? Where will other people want to use it? What possible areas of implementation will guide the development of the solutions?
Whenever I take on a new project, I tend to ask these questions. For this project, the following are my top picks:  
1. Scraping News websites.  
Say you want to find out the similarities of topics covered by all the major news networks. Which are native to the BBC? What is the similarities of content featured by CNN and Aljazeera? Which topics are common to both international and local media houses?  

2. Scraping job sites.  
Which jobs are highly promoted across LinkedIn, Glassdoor, JustRemote, GitHUb Jobs, AngelList, Flex Jobs and other sites?

Currenntly, this project will not answer these questions. However, it serves as a baseline to solving these and similar web scraping questions. How to create this baseline, is what I will discuss in this page.  

## High Level Overview
### What will the application be?  
This will be a web application. The client can provide as many pages as they wish. The pages will be processed and the results displayed for the client.  

### Where can you test the application?  
Click <a href='https://diction-scrape.herokuapp.com/'>here</a> to test the app.  

## Tech Stack
1. Python:  Beautiful soup, Flask 
2. HTML, CSS and JavaScript
3. jinja
4. GIT

### Tech Stack Summary
#### Beautiful Soup
Why Beautiful Soup? Why not Scrapy, Selenium, Splash, Pandas or Requests-HTML?  
1. Familiarity: As at the time of doing this project, I only had experience with Beautiful Soup and Pandas.  
2. Nature of the project   
Data to scrape - To find out all the words used in a page, one needs to scrape the html content of the page. Beautiful Soup is good for parsing HTML and XML.   
If the problem statement required scraping just table data, I would go with Pandas.  
Else if the problem statement required that we automatically test the application while scraping it for both HTML and JavaScript data, Selenium would be a good choice.  
If we needed to scrape huge amounts of data, wanted more control with the scraping, and still have the operation be fast, Scrapy would be the choice.  

#### Flask  
I used Flask to build the backend of the application.  

#### HTML, CSS and JavaScript
This application receives user input. This input is entered through HTML forms.  
CSS provides the styling for the page.  
For the client to provide a custom number of input pages, the input fields need to be dynamically generated. JavaScript is responsible for the functionality of Add/Remove page buttons. 

#### jinja
jinja passes data from Flask backend to HTML tags.  

#### GIT
For pushing changes from local working directory to this repo.

## Concepts that will be covered
1. Web Scraping
2. GET and POST requests
3. Exception Handling
4. Circular imports and Python packages
5. Object Oriented Programming
6. Data Structures and Algorithms
7. Dynamic routing
8. Using one event listener for multiple buttons.
9. Data visualization on the web.

## The Flow of  Data in the Application
### Files of the app
1.  run.py: has the driver code for the application.
2. application directory: the package of the application. Initialized by__init__
3. scrape.py: module with classes to scrape and compare pages.
4. routes.py: serves HTML templates, handles POST and GET requests.
5. templates directory: contains the HTML templates.
6. static directory: contains the css and javaScript files. 

### Receiving Client input
Every page of the app extends base.html. The body of base.html is divided into two columns.  
On the top right column is a form where the client enters page URLs.  
The first field of the form has an id page_1. New fields have unique ids ie. page_2, page_3 and so on.
When the submit button is clicked, a POST request is made to the backend.
#### Factors to consider
1. Invalid page URLs.  
A valid URL folllows the following syntax.  
scheme://netloc/path;params?query#fragment  
    <ul>
    <li>scheme: The protocol name, usually http/https </li>
    <li>netloc: network location</li>
    <li>path: Contains information on how the specified resource needs to be accessed</li>
    <li>params: (optional) adds fine tuning to path. </li>
    <li>query: Another element adding fine grained access to the path in consideration. (optional)</li>
    <li>fragment: Contains bits of information of the resource being accessed within the path. (optional)</li>
    </ul>  
    
    The application needs to check if a provided url is valid and if its not, alert the user and ask to provide a valid url.
    
2. No scheme provided
What happens when a user provides <em>google.com</em> or <em>www.google.com</em>? These have no scheme. How does the app handle such situations?

### Request handling
Whenever a POST request is made, the home_page function in routes.py retrieves the data from the HTML forms. 
The function does the following.  
<ul>
    <li>Creates an instance of the URL class from scrape.py</li>
    <li>Checks if the url is valid using the URL object</li>
    <li>If valid, appends the url to a pages list</li>
    <li>If not valid, flashes an alert to base.html and renders the home page </li>
    <li>Passes on the pages list to othr functions for further processing</li>
</ul>  

### Processing the page(s)
Processing the pages requires creating instances of Scraper and Compare from scrape.py  
Just pass the url to either class when creating the class objects.  
Once the objects are created, they will hold information on various categories that will then be rendered on HTML templates.  

#### Factors to consider - request handling through processing
1. Cyclic imports  
This app has a few files and doesnt face cyclic imports. However, as the needs of an application grow, so do the files needed to run the application. In such situations, its possible to have two files importing from each other. These are cyclic imports and result to some missing components.

    To avoid cyclic imports, Python uses packages; folders with__init__ file.  
    The package for this app is the directory application.  

    The driver code is located outside the package. It imports the Flask object app from the package. 

    When the driver code is run, every line of__init__ is executed.  
    The last line imports routes.py   
        <code><em> from application import routes </em> </code>  
        
    As observed earlier, routes requires the URL, Scraper and Compare classes of the scrape module. Instead of importing directly from scrape, routes uses the following line  
        <code><em>from application.scrape import Scraper</em></code>  
        
    As such if we had cyclic imports, packaging the application would solve this since class instances like app(Flask instance), db(incase we have a database instance) will always be initialized in the__init__ file and imports will be from the package. Adiitionally, the config file will be imported in the__init__     
    <code><em>from package.file import class</em></code>  
    <code><em>from package import object</em></code>   

### Receiving processed data
Data from routes.py is passed to HTML and javascript using jinja syntax.  
## The scrape module
### Class URL  
This class has only one method; url_validator that uses class urlparse from the parse module of the Python package urllib to check for url validity.  
The function checks for the presence of scheme, netloc and path in the url.  
### CLass Scrape
Whenever this class is called, the following class attributes can be accessed.  

<ul>
    <li><code>self.url </code>: url of the page</li>
    <li><code>self.title  </code>: title of the page</li>
    <li><code>self.count_dict </code>: dictionary of all words and their frequency</li>
    <li><code>self.sorted_count</code> : sorted  list of all words and their frequency of occurrence - sorted by the frequency </li>
    <li><code>self.alphanum_words </code>: all words with numbers in them </li>
    <li><code>self.unique_words  </code>: set of all words </li>
    <li><code>self.most_freq   </code>: dictionary of 10 most frequent words with frequency being the frequency</li>
    </ul>  
These attributes are passed to HTML templates in routes.py  
For these attributes to be created, the following happens,

#### 1. Get all text from HTML   
To scrape data from from HTML documents, we need to know where the data exists within the page. Words can be contained in paragraph tags, span, tables, block quotes, headings, anchor and a couple more HTML tags.  

These tags can then be within div tags which can in turn be siblings of other div tags. To access specific text on a page, we need to know the class of the div tags parent to it. These classes are different on different sites.  

The common property of HTML pages on different sites is the head and body tags. The head holds metadata on the page. The body holds the content displayed on the page.  

For the application to work on different HTML pages, we need to specify to the application that we are looking for text within the body tags.  
After  getting the text content of the page, we create a list of all words

#### 2. Clean the words  
The list of words is  cleaned by removing symbols from all words and removing words that have numbers in them.  

#### 3. Creating a counts dictionary  

### CLass Compare
This class inherits(single inheritance) from the Scraper class.  
The methods of the class use set operations to define the following attributes.

<ul>
    <li><code>self.in_all </code>: words present in all the pages</li>
    <li><code>self.only_in_first  </code>: </li>
    <li><code>self.combinations_of_two </code>: comparison of each page with every other.     
    This is a list of dictionary each of which  has the following keys: Heading ie. page 1 vs page 2, common in both, only in page 1 and  only in page 2.  
</li>   
</ul>  

## Data Visualization
The 10 most frequent words are displayed on the results page of each url using Chart.js, an open source JavaScript library for data visualization.
