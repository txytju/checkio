#Your optional code here
#You can import some modules or create additional functions


def checkio(number):
	if number%3==0 and number%5==0 :
		return "Fizz Buzz"
	elif number%3==0 :
		return "Fizz"
	elif number%5==0 :
		return "Buzz"
	return str(number)
# 为什么最后这个情况可以不使用 else
# 因为在python中，函数执行遇到return就会终止，后续的内容不会执行，
# 因此当执行到最后一种情况时（既不能被3也不能被5整除），其他情况都被排除了，只剩这一种情况了
# else : return str(number)
# 和
# return str(number)
# 两种表述的结果是一致的


# 方法2：巧妙使用 0 和 非0 数字对应的布尔值
# 0:False
# 非0:True

def checkio(n):
	return "Fizz" * (not n%3) + " " * (not n%15) + "Buzz" * (not n%5) 


#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
