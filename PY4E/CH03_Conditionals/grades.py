# Exercise 3.3
score = input('Enter score: ')
try:
    score = float(score)
except:
    print('Bad score')
    quit()
if score > 1.0 or score < 0.0:
    print('Bad score')
    quit()
elif score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'
print(grade)
