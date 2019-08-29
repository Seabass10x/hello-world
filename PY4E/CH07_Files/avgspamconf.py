# Exercise 7.2
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

spamtot = 0
count = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        colon = line.find(':')
        spamconf = line[colon + 1:]
        flspamconf = float(spamconf)
        spamtot = spamtot + flspamconf
        count = count + 1

print('Average spam confidence:', spamtot/count)
