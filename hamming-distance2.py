def checkio(n, m):

# 1. 2进制转换
# 2. 长度补齐
# 3. 比较求和


	l = [bin(n)[2:],bin(m)[2:]]

	length = max(len(i) for i in l)

	for i in range(2):
		if len(l[i]) < length :
			l[i] = (length-len(l[i]))*"0" + l[i]

	sum = 0
	for i in range(length):
		if l[0][i] != l[1][i] :
			sum += 1

	return sum


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
