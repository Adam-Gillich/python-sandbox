'''
Write a function that takes a sentence, and returns the longest even-length word in the sentence.
Or if it has no even-length words, return "00"
'''


txt = 'to check if a list is empty in Python?'
text2 = "lmdd."


def to_remove(x, addlist):
    if x == "?":
        addlist.remove(x)
    if x == "!":
        addlist.remove(x)
    if x == ".":
        addlist.remove(x)


def counter(text):
    word = []
    longest_word = []
    for i in text:
        word.append(i)
        to_remove(i, word)
        if i == " ":
            word.remove(i)
        if i == " " or i == "?" or i == "!" or i == "." or i == ",":
            if len(longest_word) < len(word) and len(word) % 2 == 0:
                longest_word.clear()
                for i in word:
                    longest_word.append(i)
            word.clear()
    if len(longest_word) == 0:
        return "00"
    else:
        return print('That is the longest even number word: ', longest_word)


print(''.join(counter(input('Give a text: '))))


def splits(text, delimiters):
    d0 = delimiters[0]
    for d in delimiters:
        text = text.replace(d, d0)
    return text.split(d0)
