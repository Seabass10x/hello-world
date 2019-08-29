# Exercise 12.3
import urllib.request, urllib.parse, urllib.error

url = input('Enter URL: ')
if url == '':
    url = 'http://data.pr4e.org/romeo-full.txt'
try:
    fhand = urllib.request.urlopen(url)
except:
    print('Enter a proper URL')
    quit()

file = fhand.read().decode()
count = len(file)
print(file[:3001])
print(count)
