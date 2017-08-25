#!/usr/bin/env python

from os.path import basename
import sys
import csv

from bs4 import BeautifulSoup as bs
import requests

url = 'http://ifpartners.com/cut-the-wire/'

data = requests.get(url)
try:                          #ensure the link was fetched without errors
    data.raise_for_status()
except:
    print 'Error getting URL'
    sys.exit(1)

soup = bs(data.content, 'lxml')  #setting parser as 'lxml' for BS

articles = soup.findAll('article')
image = soup.find('div', {'role': 'main'}).img['src']

#exit the script if there are less than 6 articles to print
if len(articles) < 6:
    print 'Less than 6 articles present.'
    sys.exit(1)

with open('data.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter = '\n')
    
    for article in articles[:6]:
        time = article.time.text.encode('utf-8')[10:]
        title = article.h2.a.text.encode('utf-8')
        href = article.h2.a['href']
        content = article.div.text.encode('utf-8').strip()
        author = article.p.a.text.encode('utf-8')
        if author:
            text = time, title, author, href, content
        else:
            author = None
            text = time, title, author, href, content

        writer.writerow(text)
        writer.writerow('')
        

#Extra Credit: download the first image in content body to disk
with open(basename(image), 'wb') as f:
    f.write(requests.get(image).content)

