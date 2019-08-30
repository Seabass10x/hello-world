# Week 6 Assignment 1

#In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://python-data.dr-chuck.net/comments_353540.json (Sum ends with 71)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
elif url == '1':
    url = 'http://python-data.dr-chuck.net/comments_353540.json'

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