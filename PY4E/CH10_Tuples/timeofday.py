# Exercise 10.2
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

# create hour of day histogram
hours = dict()
for line in fhand:
    words = line.split()
    if len(words) < 6 or words[0] != 'From':
        continue
    time = words[5]
    timeparts = time.split(':')
    hour = timeparts[0]
    hours[hour] = hours.get(hour, 0) + 1

# print list sorted by hour
lst = sorted([(k,v) for k,v in hours.items()])
for k,v in lst:
    print(k,v)
