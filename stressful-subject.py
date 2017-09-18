# 待改进：正则表达式
# 如何匹配 "whatever string whatever"
# 改进方式1 : 使用 search 而不是使用 match
# match : 默认从字符串的开头进行匹配
# search : 对字符串的子串进行匹配


import re

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    # 1.所有字母都是大写

    # if subj.isupper():
    #     return True
    
    # 2. 3个感叹号结尾    
    # if subj.endswith("!!!"):
    #     return True

    # 3. 包含3个词：“help”,“asap”,“urgent”，且可以是任意的形式
    # 非空白字符： \S 
    # 匹配前一个字符0次或无限次： *
    
    Bool = False


#   l = [r"\S*h\S*e\S*l\S*p\S*", r"\S*a\S*s\S*a\S*p\S*", r"\S*u\S*r\S*g\S*e\S*n\S*t\S*"]

#     for i in l :
#         pattern = re.compile(i)
#         for j in subj.lower().split(" "):
#             match = pattern.match(j)
#             if match :
#                Bool =  True
    


    # l = [r"h\S*e\S*l\S*p", r"a\S*s\S*a\S*p", r"u\S*r\S*g\S*e\S*n\S*t"]
    l = ["\S*".join(word) for word in ["help", "asap", "urgent"]]

    for i in l :
        pattern = re.compile(i)
        match = pattern.search(subj.lower())
        if match :
            Bool =  True

    
    # 整合
    return subj.isupper() or subj.endswith("!!!") or Bool


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
