#! python3
# dateDetection.py - Finds and validates dates in the DD/MM/YYYY format
# on the clipboard.

import pyperclip, re

def isLeapYear(year):
    if (int(year) % 400) == 0:
        return True
    elif (int(year) % 4) == 0 and (int(year) % 100) != 0:
        return True
    else:
        return False

def dateValidation(day, month, year):
    if int(day) not in range(1, 32) or int(month) not in range(1, 13):
        return False

    elif int(day) == 31 and int(month) in {2, 4, 6, 9, 11}:
        return False

    elif int(day) == 30 and int(month) == 2:
        return False

    elif int(day) == 29 and int(month) == 2:
        return isLeapYear(year)

    else:
        return True


dateRegex = re.compile(r'''(
    (\d{2})                     # DD
    /                         # separator
    (\d{2})                     # MM
    /                         # separator
    (\d{4})                     # YYYY
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in dateRegex.findall(text):
    month = groups[2]
    day = groups [1]
    year = groups[3]
    if dateValidation(day, month, year):
        matches.append(groups[0])


# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates found.')
