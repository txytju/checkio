def checkio(matrix):
    for i in range(-180,181):
        for j in range(-180,181):
            for k in range(-180,181):
                if (matrix[0][0]*i + matrix[1][0]*j + matrix[2][0]*k)%360 == 0 and (matrix[0][1]*i + matrix[1][1]*j + matrix[2][1]*k)%360 == 225 and (matrix[0][2]*i + matrix[1][2]*j + matrix[2][2]*k)%360 == 315 :
                   return [i, j, k]




# fractions:gcd(x,y)
# 求两个数的最大公约数

# functools:reduce
# 将一个二元函数从头到尾应用于一个可遍历对象
# list = [x1,x2,x3,...]
# fun(fun(fun(x1,x2),x3),x4)....

# reduce(gcd,list) : 找一个长度大于2的list的最大公约数

# itertools:product(a,b,repeat=0)
# 多个可迭代对象的连缀





#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    def check_it(func, matrix):
        result = func(matrix)
        if not all(-180 <= el <= 180 for el in result):
            print("The angles must be in range from -180 to 180 inclusively.")
            return False
        f, s, t = result
        temp = [0, 0, 0]
        temp[0] += f
        temp[1] += matrix[0][1] * f
        temp[2] += matrix[0][2] * f

        temp[0] += matrix[1][0] * s
        temp[1] += s
        temp[2] += matrix[1][2] * s

        temp[0] += matrix[2][0] * t
        temp[1] += matrix[2][1] * t
        temp[2] += t
        temp = [n % 360 for n in temp]
        if temp == [0, 225, 315]:
            return True
        else:
            print("This is the wrong final position {0}.".format(temp))
            return False

    assert check_it(checkio,
                    [[1, 2, 3],
                     [3, 1, 2],
                     [2, 3, 1]]), "1st example"
    assert check_it(checkio,
                    [[1, 4, 2],
                     [2, 1, 2],
                     [2, 2, 1]]), "2nd example"
    assert check_it(checkio,
                    [[1, 2, 5],
                     [2, 1, 1],
                     [2, 5, 1]]), "3rd example"
