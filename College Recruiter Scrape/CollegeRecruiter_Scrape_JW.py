# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 19:21:57 2016

@author: WibowoJ
"""

import urllib2
import bs4
import numpy as np
import pandas as pd
import time
import matplotlib
import matplotlib.pyplot as plt
import pickle
import re
import socket

# Fixed url for job postings containing data scientist
url = 'https://www.collegerecruiter.com/job-search?keyword=Analyst&location=San+Jose' \
      '%2C+CA%2C+United+States&locMatches=1&lat=37.3382082&lng=-121.88632860000001&page=2'
# get HTML using urllib2 read()
source = urllib2.urlopen(url).read()
# Use BS4 to parse code
bs_tree = bs4.BeautifulSoup(source, "lxml") #lxml given from warnings
#print bs_tree

#get total # of hits listed so we know what to loop to
job_count_string = bs_tree.find("div",class_= 'pull-left').contents[0]
print job_count_string #.contents returns a list of all children of the found tag, hence why you need [0] to access the list
job_count_string = job_count_string.split()[-1] #-1 is given because the wanted string is the last object in array from split
print job_count_string
digits = []
for i in job_count_string: #slow and ugly way to get all the ints in a list
    if i.isdigit():
        digits.append(int(i))
print digits #now convert the array to a number
job_count = np.sum([digit*(10**exponent) for digit, exponent in #taken from the lecture, pretty complicated, but the overview is
                    #that it pairs each digit with it's "exponent" (digit place using range()) using zip, then multiplies the digit
                    #by it's exponent. ex: 142 = (2*(10^0))+(4*(10^1))+(1*(10^2))
                    zip(digits[::-1], range(len(digits)))])
print job_count
# The website is only listing 10 results per page, 
# so we need to scrape them page after page
num_pages = int(np.ceil(job_count/10.0))

job_links = []
for i in range(1, job_count/10): #since pages have 10 jobs each, we will go from 1 - job_count/10 to get all job links
    if i%10==0:
        print num_pages-i
    a = str(i)
    url = "https://www.collegerecruiter.com/job-search?keyword=Analyst&location=San+Jose" \
          "%2C+CA%2C+United+States&locMatches=1&lat=37.3382082&lng=-121.88632860000001&page=" + a
    #use loop to go through each url needed
    html_page = urllib2.urlopen(url).read() 
    bs_tree = bs4.BeautifulSoup(html_page)
    job_link_area = bs_tree.find_all("form", method="POST")[1] #list containing all form tags, only want 2nd one
    job_postings = job_link_area.find_all(class_="jobTitle") #jobTitle contains the link
    for i in job_postings:
        job_links.append(i.find("a")['href']) #within the a tag in jobTitle, use href tag to access just the link

    time.sleep(1) #delay between each scrape
#print job_links    
print "We found a lot of jobs: ", len(job_links)

#pickle job_links
with open('joblinks.pickle','wb') as handle:
    pickle.dump(job_links, handle)
#with open('joblinks.pickle','rb') as handle:
    #job_links = pickle.load(job_links, handle)    

cities =  {"sunnyvale":0, "san jose": 0, "campbell":0, "san francisco": 0, "santa clara": 0,  "mountain view":0}
for link in job_links:
    try:
        html_page = urllib2.urlopen(link).read()
    except urllib2.HTTPError:
        print "HTTPError:"
        continue
    except urllib2.URLError:
        print "URLError:"
        continue
    except socket.error as error:
        print "Connection closed"
        continue
    #Distribution of industry
    
    html_text = re.sub("[^a-z.+3]"," ", html_page.lower()) #regex rule is replace any char that is not a-z with space
    #caret means "anything but" 
    for key in cities.keys():
        if key in html_text:
            cities[key]+=1
            
print cities
pseries = pd.Series(cities) #create pandas series from dict
pseries.sort(ascending=False)

pseries.plot(kind = 'bar') #simple histogram using pandas
plt.title('Bay Area Cities Distribution')
plt.xlabel('City')
plt.ylabel('Count')
plt.show()