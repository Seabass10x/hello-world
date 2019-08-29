# Exercise 9.3
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

senders = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    key = words[1]
    senders[key] = senders.get(key, 0) + 1
print(senders)
