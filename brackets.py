def checkio_2(expression):

	brack = "{}[]()"
	brackes = ["{}","[]","()"]

	expression_brackes = "".join([i for i in expression if i in brack])

	while True :
		old_len = len(expression_brackes)

		for i in brackes:
			expression_brackes = expression_brackes.replace(i, "")

		new_len = len(expression_brackes)

		if old_len==new_len:
			break

	# if len(expression_brackes)==0 :
	if not expression_brackes :
		return True
	else :
		return False


# 另外一种思路接近但是更简洁的方式
# 使用 string 本身来对 while 进行判断
# 使用 a, b = c, d 来进行赋值

# 使用 a, b = c, d 的形式避免了上述对处理前后的字符串长度进行比较

def checkio_1(expression):

	expression_brackes = "".join([i for i in expression if i in "(){}[]"])

	# 如果 expression_brackes 的长度不是0，那么会始终在循环里
	# 这时有两种情况：
	# 1. 现有的符号对还没有被消干净
	# 2. 有不匹配的情况出现
	while expression_brackes : 
		s0, s = expression_brackes, expression_brackes.replace("{}","").replace("()","").replace("[]","")
		if s == s0 :
			return False

	# 当上述 while 为 False 时（即 expression_brackes 为空时），跳出上述 while 循环，这样省去了对 长度的判断
	return True


# 巧用 dic : dic.items(), dic.values(), dic.keys()

def checkio(expression):
	stack = [""]
	brackes = {"{":"}", "(":")", "[":"]"}
	for c in expression :
		if c in brackes :
			stack.append(brackes[c])
		elif c in brackes.values() and c!=stack.pop() :
			return False
	# 为什么这里是 stack ==[""] 而不是return True，因为应对可能出现的前边多一个左边括号的情况
	return stack==[""]



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
