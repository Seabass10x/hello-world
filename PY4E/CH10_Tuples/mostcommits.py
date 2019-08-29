# Exercise 10.1
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

# create sender email histogram
senders = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    key = words[1]
    senders[key] = senders.get(key, 0) + 1

# determine which email sent the most
lst = list()
for k,v in list(senders.items()):
    lst.append((v,k))

lst.sort(reverse=True)

most = lst[0]
print(most[1], most[0])
