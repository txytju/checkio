def safe_pawns(pawns):

    num = 0
    s = "abcdefgh"

    for pawn in pawns:       

    	p = pawn[0]    
    	n = int(pawn[1])

        if n != 1 :
        	n -= 1
        n = str(n)

        ind = s.find(p)

        if ind == 0 :
        	p2 = s[1]
        	pawn_2 = p2 + n
        	pawn_1 = None

    	elif ind == 7 :
    		p1 = s[6]
    		pawn_1 = p1 + n
    		pawn_2 = None
    		
    	else :
    		p1 = ind - 1
    		p2 = ind + 1
    		pawn_1 = s[p1] + n
    		pawn_2 = s[p2] + n
        
    	if pawn_1 in pawns or pawn_2 in pawns :
    		num += 1
    return num


# 方法1
# 使用 chr() ord()
def safe_pawns_1(pawns):
	num = 0
	for pawn in pawns :
		if chr(ord(pawn[0])-1) + str(int(pawn[1])-1) in pawns or chr(ord(pawn[0])+1) + str(int(pawn[1])-1) in pawns : num += 1
	return num


# 方法2
# 基于上述 chr() ord()，将部分功能封装成函数
def neighbor(pawn):
	a, b  = map(ord, pawn)
	return chr(a-1) + chr(b-1), chr(a+1) + chr(b-1)

def safe_pawn_2(pawns):
	return len([pawn for pawn in pawns if any(p in pawns for p in neighbor(pawn))])




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawn_2({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawn_2({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
