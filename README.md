# Diction and Dictionary Scrapping.

## Background Info
I did this project as part of an application for a Junior Developer role at Pesapal.
In this README, I will take you through my approach to the problem, development of the solution and how you can contribute to taking this project past the scope of the problem statement.  
<blockquote>
*** I have not yet completed writing the README.
</blockquote>

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

Currenntly, this project will not answer these questions. However, it serves as a baseline or blueprint to solving these and similar web scraping questions. How to create this baseline, is what I will be answering in this page.  

## High Level Overview
### What will the application be?  
This will be a web application. The client can provide as many pages as they wish. The pages will be processed and the results displayed for the client.  

### Where can you test the application?  
I have hosted the application <a href='http://dictionscrape.pythonanywhere.com/'>here</a>.  
#### Errors with testing.  
Locally, the project works fine. When hosted, I run into the following error. 
<blockquote>
requests.exceptions.ProxyError: HTTPSConnectionPool(host='www.geeksforgeeks.org', port=443): Max retries exceeded with url: /python-find-words-with-both-alphabets-and-numbers/ (Caused by ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 403 Forbidden')))
</blockquote>
I searched for why I get this error and according to <a href='https://stackoverflow.com/questions/70788406/requests-exceptions-proxyerror-httpsconnectionpoolhost-zillow-com-port-443'>this</a>, it is because I am on the free plan. Apparently, when hosting your applications at <a href='https://www.pythonanywhere.com/'>pythonanywhere</a>, if your web app involves scraping, they have to add the pages you want to scrape on the white list. The application should work on a paid plan.   

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
For pushing changes from local working directory to this GitHub repo.

## Concepts that will be covered
1. Web Scraping
2. Creating Flask backends
3. GET and POST requests
4. Exception Handling
5. Packaging the Application
6. Working with classes and class inheritance
7. Data Structures and Algorithms
8. Secret keys for applications
9. Dynamic routing
10. Creating front ends to web applications.

## Development
### Files of the app
1.  run.py: has the driver code for the application.
2. application directory: the package of the application. Initialized by__init__
3. scrape.py: module with classes to scrape and compare pages.
4. routes.py: serves HTML templates, handles POST and GET requests.
5. templates directory: contains the HTML templates.
6. static directory: contains the css and javaScript files. 

### Web Scraping
To scrape data from from HTML documents, we need to know where the data exists within the page. Words can be contained in paragraph tags, span, tables, block quotes, headings, anchor and a couple more HTML tags.  
These tags can then be within div tags which can in turn be siblings of other div tags. To access specific text on a page, we need to know the class of the div tags parent to it. These classes are different on different sites.  
The common property of HTML pages on different sites is the head and body tags. The head holds metadata on the page. The body holds the content displayed on the page.  
For the application to work on different HTML pages, we need to specify to the application that we are looking for text within the body tags.