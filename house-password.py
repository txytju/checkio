# 字符串的拼写检查
# 要求：
# 至少10个字符
# 至少1个数字
# 至少一个大写一个小写
# 前提条件：输入的字符串只可能由大小写字母和数字组成




def checkio(data):

    #replace this for solution
    import string
    
    l = string.ascii_lowercase
    l_num = 0
    u = string.ascii_uppercase
    u_num = 0 
    d = string.digits
    d_num = 0
    
    if len(data) < 10 :
        return False
    
    for i in data :
        if i in l :
            l_num += 1
        if i in u :
            u_num += 1
        if i in d :
            d_num += 1
            
    if l_num and u_num and d_num :
        return True
    else :
        return False
            


# 一种相当有局限性的写法：字符串中不能包含除数字和大小写字母之外的东西
checkio_1 = lambda s : not(
            len(s)<10
            or s.isdigit()
            or s.isalpha()
            or s.islower()
            or s.isupper()
            )


# 正则表达式的写法

import re
def housepassword(s):
    digit_re = re.compile("\d")
    if not digit_re.search(s):
        return False


#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
