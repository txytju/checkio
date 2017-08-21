from math import acos, pi, degrees

def checkio(a, b, c):

    #replace this for solution
    x = [a, b, c]
    if max(x) >= sum(x)-max(x) :
    	return [0,0,0]

    return sorted([find_angle(a,b,c), find_angle(b,a,c), find_angle(c,a,b)])

def find_angle(a,b,c):
	return int(round(degrees(acos((c**2 + b**2 - a**2)/(2*c*b)))))	
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
