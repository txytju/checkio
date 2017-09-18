# 方法1：传统的方法，使用列表，新元素添加到列表的末尾

def largest_histogram_1(histogram):

	length = len(histogram)

	s = []

	for i in range(length):
		for j in range(length-i):
			if histogram[j:j+i+1]:
				h = min(histogram[j:j+i+1]) * (i+1)
				s.append(h)

	return max(s)



# 方法2：yield返回一个可迭代对象，再使用一个lambda函数取这个可迭代对象的最大值
def histogram_1(histogram):

	length = len(histogram)

	for i in range(length):
		for j in range(length-i):
			if histogram[j:j+i+1]:
				yield min(histogram[j:j+i+1]) * (i+1)

# histogram_1(x) 返回一个可迭代对象
largest_histogram_2 = lambda x : max(histogram_1(x))



# 方法3
def largest_histogram(histogram):

	length = len(histogram)

	return max(min(histogram[j:j+i+1])*(i+1) for i in range(length) for j in range(length-i))










if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
