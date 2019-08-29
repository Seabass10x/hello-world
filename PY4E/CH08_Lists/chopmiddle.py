# Exercise 8.1
def chop(t):
    del t[len(t) - 1]
    del t[0]

def middle(t):
    return t[1:len(t) - 1]

a = [1, 2, 3, 4, 5]
print('Chop')
print(chop(a))
print(a)

b= [1, 2, 3, 4, 5]
print('Middle')
print(middle(b))
print(b)
