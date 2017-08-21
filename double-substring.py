def double_substring(line):

    s = []
    for i in range(len(line)-1) :
        for j in range(i+1,len(line)+1) :
            if line[i:j] in line[j:] :
                s.append(len(line[i:j]))
    
    if len(s)>0 :
        return max(s)
    else :
        return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
