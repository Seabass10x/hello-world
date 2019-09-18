# Using Python to Access Web Data
# Week 2 Graded Exercise
# Extracting Data With Regular Expressions
import re

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

numsum = 0
for line in fhand:
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    if len(nums) < 1 : continue
    for i in nums:
        num = int(i)
        numsum = numsum + num

print(numsum)
