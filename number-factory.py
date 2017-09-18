def checkio(number):


	l = []

	while True:

		number1 = number

		for i in range(9,1,-1) :
			a, b = divmod(number,i)
			if b==0:
				l.append(i)
				number = a
				break
		
		if number1==number:
			return 0
		if number==1:
			break

	return int(''.join([str(i) for i in sorted(l)]))





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"


# def is_prime(a):
#s    return a > 1 and all(a % i for i in range(2, int(a**0.5) + 1))