# Exercise 6.5
str = 'X-DSPAM-Confidence: 0.8475 '
colon = str.find(':')
value = str[colon + 1:]
flval = float(value)
print(flval)
