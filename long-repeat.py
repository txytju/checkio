def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if line == "":
    	return 0

    n = 0
    s = []
    
    for i in range(len(line)-1):
    	if line[i]==line[i+1]:
    		n+=1
    		s.append(n)
    		print(s)
		else:
			n=0


	if s==[]:
		return 1

	return max(s)+1



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
