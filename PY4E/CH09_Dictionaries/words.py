# Exercise 9.1
wordfile = open('words.txt')

worddict = dict()
for line in wordfile:
    words = line.split()
    for word in words:
        worddict[word] = worddict.get(word, 0) + 1
lookup = input('Word to lookup: ')
print(lookup in worddict)
