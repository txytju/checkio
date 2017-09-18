def reverse_roman(roman_string):

	Units = [["M","D","C"], ["C","L","X"], ["X","V","I"]]

	X = [[i[2]+i[0], i[1]+i[2]*3, i[1]+i[2]*2, i[1]+i[2], i[1], i[2]+i[1], i[2]*3, i[2]*2, i[2]] for i in Units]

	To_count_R = ["MMM","MM","M"]
	To_count_D = [3000, 2000, 1000]

	for i in range(3):
		To_count_R.extend(X[i])

	for i in range(2,-1,-1):
		To_count_D.extend([j*10**i for j in range(9,0,-1)])

	sum = 0

	for i,j in zip(To_count_R, To_count_D):
		if roman_string.startswith(i):
			roman_string = roman_string.replace(i,"",1)
			sum += j

    return sum

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');