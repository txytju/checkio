def capture(matrix):

    matrix_r = matrix
    for i in range(len(matrix)):
        matrix_r[i][0] = 0
        matrix_r[i][i] = 0

    for i in range(len(matrix)) :
        if matrix[i][0]==1:
            return matrix[i][i]
        else :
            idx = [i for i,item in enumerate(matrix_r[i]) if item==1]
            return min()



def f(x,i):

    if x[0]==1 :
        return x[i]
    else :
        x[0] = 0
        x[i] = 0
        idx = [i for i,item in enumerate(x) if item==1]
        return min(f())




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
