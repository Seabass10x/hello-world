# Exercise 9.4
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
email = None
most = None
for k,v in senders.items():
    if most is None or v > most:
        email = k
        most = v

print(email, most)
