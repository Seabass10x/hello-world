# Exercise 7.3
fname = input('Enter the file name: ')

# Easter Egg
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0

for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1

print('There were %d subject lines in %s' % (count, fname))
