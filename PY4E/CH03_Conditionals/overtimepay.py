# Exercise 3.1
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
if float(hours) <= 40:
    pay = float(hours) * float(rate)
else:
    pay = (40 * float(rate)) + ((float(hours) - 40) * (float(rate) * 1.5))
print('Pay:', round(pay, 2))
