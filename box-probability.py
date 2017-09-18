def checkio(marbles, step):

	l = [(marbles, 1)]

	for i in range(step-1):
		l = children(l)

	p_list = []
	for marble,p in l:
		b = marble.count("b")
		w = marble.count("w")
		p = p*w/(w+b)
		p_list.append(p)

	return round(sum(p_list),2)


def children(l_in):
	# 根据上一级的一个 list，生成下一级的list
	# 上一级：[(marble, p),(marble, p),(marble, p) ...]
	l_out = []
	for i in l_in :
		r = fun(i)
		for j in r :
			l_out.append(j)

	return l_out


def fun(item):
	# item is a tuple
	marble, p = item
	b = marble.count("b")
	w = marble.count("w")
	return [(x,y) for (x,y) in [(marble.replace("b", "w", 1), p*b/(b+w)), (marble.replace("w", "b", 1), p*w/(b+w))] if y!=0]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("yes")
