def checkio(matrix):
    l = []

    # 横向的
    for i in matrix :
        l.append(i)

    length = len(matrix[0])

    # 纵向的
    for i in range(length) :
        l_v = []
        for j in range(length) :
            l_v.append(matrix[j][i])
        l.append(l_v)

    # 斜向的（左下斜向）

    for k in range((length-1)*2) :
        l_x = []    
        for i in range(length) :
            for j in range(length) :
                if i+j==k :
                    l_x.append(matrix[j][i])
        l.append(l_x)

    # 斜向的（右下斜向）
    start = []
    for i in range(length) :
        start.append([0,i])
        start.append([i,0])

    for x,y in start :
        l_x = [matrix[x][y]]
        while True :
            x += 1
            y += 1
            if x >= length or y >= length :
                break
            else :
                l_x.append(matrix[x][y])
        l.append(l_x)


    # 判断
    for i in l :
        if is_a_sequence(i) and len(l)>=4 :
            return True
    else :
        return False


def is_a_sequence(L):
    for i in range(len(L)-3):
        l = L[i:i+4]
        if len(set(l))==1 :
            return True
    else :
        return False
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"




# 0,0 0,1 0,2 0,3
# 1,0 1,1 1,2 1,3
# 2,0 2,1 2,2 2,3
# 3,0 3,1 3,2 3,3