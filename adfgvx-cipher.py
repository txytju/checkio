from math import ceil
from itertools import zip_longest

def encode(message, secret_alphabet, keyword):

  # 翻译表
  alphabat = [["d","h","x","m","u","4"],
              ["p","3","j","6","a","o"],
              ["i","b","z","v","9","w"],
              ["1","n","7","0","q","k"],
              ["f","s","l","y","c","8"],
              ["t","r","5","e","2","g"]]

  item = "ADFGVX"
  dict_translate = {}

  for i in range(len(alphabat)):
    for j in range(len(alphabat)):
      dict_translate[alphabat[i][j]] = item[i]+item[j]

  # 原始字符串处理
  message = "".join([i for i in message.lower() if i.isalpha() or i.isdigit()])
  message = "".join([dict_translate[i] for i in message])

  # 将原始字符串切分，转置
  n = len(keyword)
  m = ceil(len(message)/len(keyword))
  l = []

  for i in range(m):
    l.append(message[i*n:(i+1)*n])

  l = ["".join(i) for i in zip_longest(*l, fillvalue="")]

  # 按照字母表的顺序重新排列l中的字符串
  dict = {}

  for i in range(n):
    dict[keyword[i]] = l[i]

  l = sorted(dict.items(), key=lambda x:x[0])

  return "".join([i[1] for i in l])



















def decode(message, secret_alphabet, keyword):

  m = len(message)
  n = len(keyword)

  a = m//n
  b = m%n

  dict = {}

  for i in range(n):
    if i < b:
      dict[keyword[i]] = a+1
    else:
      dict[keyword[i]] = a

  # l：与字母表相对应的不同字母对应的字符数量
  l = [i[1] for i in sorted(dict.items(), key=lambda x:x[0])]

  # new_l：将原始的message按照正确的数量且分开
  new_l = []
  ind_s, ind_e = 0,0
  for i in l:
    ind_e += i
    new_l.append(message[ind_s:ind_e])
    ind_s += i

  sorted_keyword = sorted(keyword)

  # 将message中的字母与new_l对应
  dict_new = {}
  for i,j in zip(sorted_keyword,new_l):
    dict_new[i] = j

  s = ""
  for i in zip_longest(*[dict_new[i] for i in keyword], fillvalue=""):
    s += "".join(i)

  l = []
  for i in range(int(m/2)):
    l.append(s[2*i:2*i+2])


  alphabat = [["d","h","x","m","u","4"],
              ["p","3","j","6","a","o"],
              ["i","b","z","v","9","w"],
              ["1","n","7","0","q","k"],
              ["f","s","l","y","c","8"],
              ["t","r","5","e","2","g"]]

  dict = {}

  item = "ADFGVX"

  for i in range(len(alphabat)):
    for j in range(len(alphabat)):
      dict[item[i]+item[j]] = alphabat[i][j]



  return "".join([dict[i] for i in l])


    





if __name__ == '__main__':
    assert encode("I am going",
                   "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                   "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                 "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"



    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"