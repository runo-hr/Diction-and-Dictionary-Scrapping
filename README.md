# Diction and Dictionary Scrapping.

## Background Info
I did this project as part of an application for a Junior Developer role at Pesapal.
IN this README, I will take you through my approach to the problem, development of the solution and how you can contribute to taking this project past the scope of the problem statement.

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
This will be a web application. The client can provide as many pages as they wish. The pages will be processed and the results displayed to the user.  

### Where can you test the application?  
I have hosted the application <a href='http://dictionscrape.pythonanywhere.com/'>here</a>.  
#### Errors with testing.  
Locally, the project works fine. When hosted, I run into the following error. 

requests.exceptions.ProxyError: HTTPSConnectionPool(host='www.geeksforgeeks.org', port=443): Max retries exceeded with url: /python-find-words-with-both-alphabets-and-numbers/ (Caused by ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 403 Forbidden')))

I searched for why I get this error and according to <a href='https://stackoverflow.com/questions/70788406/requests-exceptions-proxyerror-httpsconnectionpoolhost-zillow-com-port-443'>this</a>, it is because I am on the free plan. Apparently, when hosting your applications at <a href='https://www.pythonanywhere.com/'>pythonanywhere</a>, if your web app involves scraping, they have to add the pages you want to scrape on the white list. The application should work on a paid plan.   
