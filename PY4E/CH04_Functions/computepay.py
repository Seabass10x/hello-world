# Exercise 4.6
def computepay(hours,rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    return pay

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

pay = computepay(hours,rate)
print(round(pay, 2))
