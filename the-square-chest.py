def checkio(lines_list):
    
    num = 0

    for i in range(3):
        for j in range(3):
            for n in range(1,4) :
                l = lines(i,j,n)
                if all([i in lines_list or i[::-1] in lines_list for i in l]) :
                    num += 1

    return num


def lines(i,j,n):
    # n is length of the square
    l = []
    for k in range(n):
        l.append([j*4+(i+1)+k, j*4+(i+2)+k]) # top
        l.append([(j+n)*4+(i+1)+k, (j+n)*4+(i+2)+k]) # bottom
        l.append([(j+k)*4+(i+1), (j+k+1)*4+(i+1)]) # left
        l.append([(j+k)*4+(i+n+1), (j+k+1)*4+(i+n+1)]) # right

    return l





if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"