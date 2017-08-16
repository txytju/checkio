import math
import numpy as np

def checkio(data):

    #replace this for solution
    data = [float(num) for num in data.replace(",","").replace("(","").replace(")","")]

    x1 = data[0]
    y1 = data[1]
    x2 = data[2]
    y2 = data[3]
    x3 = data[4]
    y3 = data[5]

    A = np.array([2*(x1-x2), 2*(y1-y2)], [2*(x1-x3), 2*(y1-y3)])
    b = np.array([x1**2-x2**2+y1**2-y2**2, x1**2-x3**2+y1**2-y3**2])

    x, y = np.linalg.solve(A, b)

    r = math.sqrt((x-x1)**2 + (y-y1)**2)

    return "({}-4)^2+({}-4)^2={}^2".format(x,y,r)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
