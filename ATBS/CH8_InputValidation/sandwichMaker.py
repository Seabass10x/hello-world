#! python3
# Take user's order and provide a price.

import pyinputplus as pyip

prices = {'wheat': 0.75,
          'white': 0.7,
          'sourdough': 0.8,
          'chicken': 2.5,
          'turkey': 2.65,
          'ham': 2.65,
          'tofu': 2.75,
          'cheddar': 0.9,
          'Swiss': 1,
          'mozzarella': 0.95,
          'mayo': 0.2,
          'mustard': 0.05,
          'lettuce': 0.05,
          'tomato': 0.1}

subtotal = 0

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
subtotal += prices[bread]

protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
subtotal += prices[protein]

wantCheese = pyip.inputYesNo(prompt='Would you like cheese? ')
if wantCheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
    subtotal += prices[cheese]

wantMayo = pyip.inputYesNo(prompt='Do you want mayo? ')
if wantMayo == 'yes':
    subtotal += prices['mayo']

wantMustard = pyip.inputYesNo(prompt='Do you want mustard? ')
if wantMustard == 'yes':
    subtotal += prices['mustard']

wantLettuce = pyip.inputYesNo(prompt='Do you want lettuce? ')
if wantLettuce == 'yes':
    subtotal += prices['lettuce']

wantTomato = pyip.inputYesNo(prompt='Do you want tomato? ')
if wantTomato == 'yes':
    subtotal += prices['tomato']

quantity = pyip.inputInt(prompt='How many sandwiches would you like?\n', min=1)
total = subtotal * quantity
'${:,.2f}'.format(total)

print('The total for your order is $%s' % (total))
