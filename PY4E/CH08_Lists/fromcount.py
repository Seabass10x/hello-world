# Exercise 8.5
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

senders = list()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From' : continue
    sender = words[1]
    print(sender)
    senders.append(sender)
print('There were %d lines in the file with From as the first word' % len(senders))
