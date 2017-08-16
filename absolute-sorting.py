def checkio(numbers_array):

	s = sorted([abs(i) for i in numbers_array])
	
    ss = []
	for i in s :
		if i in numbers_array :
			ss.append(i)
		else :
			ss.append(-1*i)

	return ss


def checkio_1(numbers_array):
    return sorted(numbers_array, key=abs)


def checkio_2(numbers_array):
    s = sorted([abs(i) for i in numbers_array])
    return [i if i in numbers_array else -1*i for i in s]
    # return [i for i in s if i in numbers_array else -1*i]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio_2((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio_2((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio_2((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
