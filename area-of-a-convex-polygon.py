from math import sqrt
def checkio(data):
    # data: [[x1,y1],[x2,y2],[x3,y3],...]
    area = 0

    for i in range(1,len(data)-1):
        l = [data[0]]
        l.append(data[i])
        l.append(data[i+1])
        area += area_triangle(l)

    return round(area,1)


def area_triangle(l):
    # l:[[x1,y1],[x2,y2],[x3,y3]]
    sorted_l = [[l[0],l[1]],[l[1],l[2]],[l[0],l[2]]]

    x = [length(i) for i in sorted_l]
    s = sum(x)/2

    return sqrt(s*(s-x[0])*(s-x[1])*(s-x[2]))



def length(l):
    # l : [[x1,y1],[x2,y2]]
    return sqrt((l[0][0]-l[1][0])**2 + (l[0][1]-l[1][1])**2)

# 上述方法是在已知三角形各个角点坐标的情况下，计算三角形面积的笨方法：点-线长度-三角形面积
# 实际上仅通过坐标就可以直接得到三角形的面积，避免了上述 length 和 area_triangle 两个麻烦的函数

# 体会：优化python syntax 是其次，首先是优化要计算的对象的算法本身。
# 找到更好的算法才是正确的先期优化，而不是先优化 python syntax







if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
