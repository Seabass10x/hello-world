# Exercise 6.3
def count(inplet,inpword):
    cnt = 0
    for letter in inpword:
        if letter == inplet:
            cnt = cnt + 1
    return str(cnt)

inpword = input('Enter a word: ')
inplet = input('Enter a letter: ')
print('The letter ' + inplet + ' occurs ' + count(inplet,inpword) + ' times in the word ' + inpword + '.')
