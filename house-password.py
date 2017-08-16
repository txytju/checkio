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
