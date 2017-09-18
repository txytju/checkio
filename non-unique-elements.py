#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  

    # 
    data_new = []
    for i in data :
        num = data.count(i)
        if num == 1 :
            pass
        else :
            data_new.append(i)

    
    return data_new


# 同样的思路，使用 list compresion
# 相当于返回原始 list 的子集，因此使用 list compresion 最好

def checkio(data):
    return [x for x in data if data.count(x)>1]


from collections import Counter
def non_unique(l):
    c = Counter(l)
    unique_l = [i for i in c if c[i]==1]
    return [i for i in l if i not in unique_l] 

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")