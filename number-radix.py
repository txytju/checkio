import string

def checkio(str_number, radix):
	# can not use string.lowercase here
	s = string.digits + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

	if s.find(max(str_number)) >= radix :
		return -1

	times = 0
	sum = 0
    
    ss = [s.find(i) for i in str_number]
    ss.reverse()
    
	for i in ss :
		sum += i * radix**times
		times += 1

	return sum

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
