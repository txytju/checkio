from string import *

def translate(phrase):
	AZ = ascii_lowercase
	VOWELS = [i for i in "aeiouy"]
	CONSONANT = [i for i in AZ if i not in VOWELS]

	for i in CONSONANT:
		for j in VOWELS:
			phrase = phrase.replace(i+j,"*"+i+"*")

	for j in VOWELS:
		phrase = phrase.replace(j*3,j)

    return phrase.replace("*","")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
