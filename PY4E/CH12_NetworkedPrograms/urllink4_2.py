# Using Python to Access Web Data
# Week 4 Graded Exercise 2
# Following Links in HTML Using BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
rpt = input('Enter count: ')
pos = input('Enter position: ')
rpt = int(rpt)
pos = int(pos) - 1
count = 0
while count <= rpt:
    print('Retrieving:',url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos].get('href', None)
    count = count + 1
