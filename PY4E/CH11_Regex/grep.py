# Exercise 11.1
import re
fhand = open('mbox.txt')
grep = input('Enter a regular expression: ')

count = 0
for line in fhand:
    line = line.rstrip()
    if re.search(grep, line):
        count = count + 1

print('mbox.txt had {} lines that matched {}'.format(count,grep))
