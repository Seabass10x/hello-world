# Exercise 5.2
min = None
max = None

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break

    try:
        num = int(num)
    except:
        print('Invalid input')
        continue

    if min is None:
        min = num
    elif num < min:
        min = num

    if max is None:
        max = num
    elif num > max:
        max = num

print('Maximum is',max)
print('Minimum is',min)
