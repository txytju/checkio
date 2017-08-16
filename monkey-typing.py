def count_words(text, words):

	num = 0;
	text = text.lower();

	for word in words :
		if word in text :
			num += 1
    return num

# 重构
def count_words_1(text, words):

	return sum([x in text.lower() for x in words])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words_1("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words_1("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words_1("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
