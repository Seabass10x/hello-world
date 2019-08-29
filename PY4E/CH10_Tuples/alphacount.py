# Exercise 10.3
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

# create letter histogram
letters = dict()
for line in fhand:
    line = line.rstrip()
    if len(line) < 1:
        continue
    line = line.lower()
    for a in line:
        if a.isalpha():
            letters[a] = letters.get(a, 0) + 1
#print(letters)
# print list sorted by frequency
lst = sorted([(v,k) for k,v in letters.items()],reverse=True)
for k,v in lst:
    print(k,v)
