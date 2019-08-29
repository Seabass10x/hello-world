# Exercise 9.5
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

# create school histogram
schools = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    email = words[1]
    emailcomponents = email.split('@')
    school = emailcomponents[1]
    schools[school] = schools.get(school, 0) + 1
print(schools)

# determine which school sent the most
sch = None
max = None
for k,v in schools.items():
    if max is None or v > max:
        sch = k
        max = v

print(sch, max)
