def checkio(number):
    
    m = 1

	nums = [int(i) for i in str(number) if i != "0"]

	for num in nums :
		m *= num


    return m

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
