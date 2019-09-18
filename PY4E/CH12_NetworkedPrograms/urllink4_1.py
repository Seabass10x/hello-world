# Using Python to Access Web Data
# Week 4 Graded Exercise 1
# Scraping HTML Data with BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup)

# Retrieve all of the span tags
tags = soup('span')
count = 0
numsum = 0
for tag in tags:
    num = int(tag.contents[0])
    numsum = numsum + num
    count = count + 1

print('Count', count)
print('Sum', numsum)
