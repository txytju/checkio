# 版本1
# Expression(num,i) ：使用类似于1-9这样的规则将不同数位的不同数值的表达形式描述出来
# checkio(data)：将数据切成不同数位，调用Expression函数将不同数位的值表达出来并相连

# 待改进：没有洞察罗马数字的表示形式的最简便形式，因此使用了1-3,4-5,6-8,9四种形式来表示一个数位上的可能结果

def checkio(data):

    data = [int(i) for i in str(data)][::-1]
    
    if len(data)==4 :
		return "".join(([Expression(data[i-1],i) for i in range(1,len(data))] + [data[3] * "M"])[::-1])
	else :
		return "".join([Expression(data[i-1],i) for i in range(1,len(data)+1)][::-1])


def Expression(num,i):
	# num : 某个数位上的具体数值
	# i : 哪个数位，个位i=1, 十位i=2, 百位i=3

	# a list of Roman Uint
	RU = [["M","D","C"], ["C","L","X"], ["X","V","I"]]
	Units = RU[-i]

	if num<4 :
		return num * Units[2]
	elif num<6 :
		return (5-num)*Units[2]+Units[1]
	elif num<9 :
		return Units[1]+(num-5)*Units[2]
	else :
		return Units[2]+Units[0]





# 改进方式1：使用枚举的方式，同时使用对不同情况的更好的代表

from enum import Enum 

class Roman(Enum) :

	# 以下方式是对罗马数字的规律的更好的表达
    M  = 1000
    CM = 900
    D  = 500
    CD = 400
    C  = 100
    XC = 90
    L  = 50
    XL = 40
    X  = 10
    IX = 9
    V  = 5
    IV = 4
    I  = 1

    # 使用类方法生成一个 generator
    @classmethod
    def encode(cls,n):
    	for i in cls :
    		rep, n = divmod(n, i.value)
    		yield i.name * rep


checkio = lambda n : ''.join(Roman.encode(n))


# 注意上述 yield 的使用
# Roman.encode(n)实际上生成的是一个 generator，generator是一个可迭代对象
# 因此在使用 str.join()的时候可以遍历这个generator，并将其中的内容连接起来
# 如果在这里不使用 generator，使用list也可以实现相同的目标，只是不像yield这么优雅
# We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.
# [Improve Your Python: 'yield' and Generators Explained](https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)
@classmethod
def encode(cls,n) :
	s = []
	for i in cls :
		rep, n = divmod(n, i.value)
		s.append(rep * i.name)
	return s

checkio = lambda n : ''.join(Roman.encode(n))























if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'






# 扩展
from enum import Enum 

# 对枚举的定义
class Roman(Enum) :

    M  = 1000
    CM = 900
    D  = 500
    CD = 400
    C  = 100

# 对枚举的遍历，可以使用name和value属性
for i in Roman :
	print(i, i.name, i.value)

# output :
# Roman.M, M, 1000

# 此外，还有一个和枚举有关的函数 enumerate

l = ['a','b','c']
for index, value in enumerate(l):
	print(index,value)