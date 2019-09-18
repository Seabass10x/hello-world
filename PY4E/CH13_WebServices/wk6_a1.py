# Week 6 Assignment 1

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
elif url == '1':
    url = 'http://python-data.dr-chuck.net/comments_284533.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

try:
    js = json.loads(data)
except:
    js = None

if not js:
    print('==== Failure To Retrieve ====')
    print(data)

comments = js['comments']
print('Count: ', len(comments))

sum = 0
for item in comments:
    sum = sum + item['count']

print('Sum: ', sum)
