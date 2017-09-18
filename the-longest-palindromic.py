def longest_palindromic(text):

    s = []
    if len(text)==1 :
        return text

    for i in range(1,len(text)):
        text_a, text_b = text[:i][::-1], text[i:]
        
        # 情形1：无中心对称字符
        s1 = string_match(text_a,text_b)
        s1 = s1[::-1] + s1
        # 情形2：有中心对称字符串
        s2 = string_match(text_a,text_b[1:])
        s2 = s2[::-1] + text_b[0] + s2

        s.append(s1)
        s.append(s2)

    m = max([len(i) for i in s])

    if m==1:
        return text[0]
    else :
        return [i for i in s if len(i)==m][0]






def string_match(string_a, string_b):
	# string_a, string_b 是要匹配的字符串
	# “abba”形式
	s = []
	for i in range(min(len(string_a),len(string_b))):
		if string_a[i]==string_b[i]:
			s.append(string_b[i])
		else :
			break
	return ''.join(s)



if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"