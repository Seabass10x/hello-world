from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    a_lines = set(a.split("\n"))
    b_lines = set(b.split("\n"))

    return list(a_lines & b_lines)


def sentences(a, b):
    """Return sentences in both a and b"""

    # http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.sent_tokenize
    a_sentences = set(sent_tokenize(a))
    b_sentences = set(sent_tokenize(b))

    return list(a_sentences & b_sentences)


def substr_list(a, n):

    # https://stackoverflow.com/questions/13298907/remove-all-newlines-from-inside-a-string
    a = a.replace('\n', "")
    substr = []
    for i in range(len(a) - n + 1):
        substr.append(a[i:i + n])
    return substr


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    a_substr = set(substr_list(a, n))
    b_substr = set(substr_list(b, n))

    return list(a_substr & b_substr)
