import string
import re


VOWELS = set("AEIOUY")
CONSONANTS = set("BCDFGHJKLMNPQRSTVWXZ")

def is_striped(word):

    word = [letter for letter in word.upper()]

    even = set(word[::2])
    odd = set(word[1::2])

    if even <= VOWELS and odd <= CONSONANTS:
        return True
    elif odd <= VOWELS and even <= CONSONANTS:
        return True
    else:
        return False


def checkio(text):
    p = re.compile(r'\w+')
    words = p.findall(text)
    words = [word for word in words if len(word)>1 and word.isalpha()]
    return len([word for word in words if is_striped(word)])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"


# 不要重复造轮子
# def has_digits(word):
# 	for digit in string.digits:
# 		if digit in word:
# 			return True
# 	return False