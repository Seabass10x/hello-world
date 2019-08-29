# Exercise 8.6
numlist = list()
while True:
    num = input('Enter a number: ')
    if num == 'done' : break
    try:
        flnum = float(num)
    except:
        print('Entry must be numeric!')
        quit()
    numlist.append(flnum)
print('Maximum:', max(numlist))
print('Minumum:', min(numlist))
