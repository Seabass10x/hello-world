# Exercise 3.2
hours = input('Enter Hours: ')
try:
    hours = float(hours)
except:
    print('Error, please enter numeric input')
    quit()
rate = input('Enter Rate: ')
try:
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
if float(hours) <= 40:
    pay = hours * rate
else:
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
print('Pay:', round(pay, 2))
