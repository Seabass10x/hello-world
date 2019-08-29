# Exercise 8.4
romeo = open('romeo.txt')

wordlist = list()
for line in romeo:
    words = line.split()
    if len(words) == 0 : continue
    for word in words:
        if word not in wordlist:
            wordlist.append(word)

wordlist.sort()
print(wordlist)
