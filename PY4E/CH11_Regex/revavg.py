# Exercise 11.2
import re

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

revnum = dict()
for line in fhand:
    line = line.rstrip()
    rnum = re.findall('^New Revision: ([0-9]+)', line)
    if len(rnum) < 1 : continue
    rint = int(rnum[0])
    revnum[rint] = revnum.get(rint, 0) + 1
#print(revnum)

revavg = sum(revnum.keys())/sum(revnum.values())
print(int(revavg))
