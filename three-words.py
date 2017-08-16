s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def checkio(words):
	
	words = words.split()
	state = []
	
	for word in words :
		x = all([i in s for i in word])
		state.append(x)
    
    return Three_Words(state)


def Three_Words(state):
	if len(state) < 3 :
		return False

	sum = 0
	for i in state :
		if i :
			sum += 1
		else :
			sum = 0

		if sum == 3 :
			return True
	else :
		return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
