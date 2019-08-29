# Exercise 9.2
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dow = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    key = words[2]
    dow[key] = dow.get(key, 0) + 1
print(dow)
