# Week 5 Assignment
# The program will prompt for a URL, read the XML data from that URL
# using urllib and then parse and extract the comment counts from the
# XML data, compute the sum of the numbers in the file and enter the sum,
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter URL: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

comments = tree.findall('comments/comment')
print('Count: ', len(comments))

sum = 0
for block in comments:
    comcnt = block.find('count').text
    intcnt = int(comcnt)
    sum = sum + intcnt

print('Sum: ', sum)
