def isLeapYear(year):
    if (int(year) % 400) == 0:
        return True
    elif (int(year) % 4) == 0 and (int(year) % 100) != 0:
        return True
    else:
        return False

print(isLeapYear(2020))
