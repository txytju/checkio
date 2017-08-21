# from string import maketrans

def checkio(time_string):
	s = time_string.split(":")
	return " : ".join([Decimal_to_binary(s[0],2), Decimal_to_binary(s[1],3), Decimal_to_binary(s[2],3)])



def Decimal_to_binary(s,n) :
	if len(s)==1 :
		return n * "." + " " + trans(s,4)
	else :
		return trans(s[0],n) + " " + trans(s[1],4)

def trans(s,n):
	ss = bin(int(s)).split("b")[-1]
	b = (n-len(ss)) * "0" + ss
	# return b.translate(maketrans("01",".-"))
	return b.replace("0",".").replace("1","-")



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

