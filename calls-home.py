


def total_cost(calls):
  dict = {}
  for call in calls:
    date, _, length = call.split(" ")
    dict[date] = dict.get(date,0) + ceil(int(length)/60)

  return ...






# 第一种做法反思
# 使用Counter是非常优雅的写法
# 除此之外，普通的字典dict也可以达到相同的作用

# 原理：dict类型赋值的几种情况
# 情况1：key已经存在，则以下两种方式都可行
# dict[key] = 1
# dict[key] += 1
# 情况2：key不存在，则第一种方式可行，第二种方式不可行，会报 keyerror
# dict[key] = 1
# dict[key] += 1

# 有没有一种方法让普通的dict 实现和Counter一样的功能呢？即即便key不存在也可以使用增量赋值或者相似的赋值
# 答案是 dict.get
# dict.get(key, default=None) :
# key : 要查找的键
# 如果指定键的值不存在，就返回该默认值。（注意函数的返回值是这个默认值，而不是字典）
# 因此，实现Counter功能的语句是
# dict[key] = dict.get(key,0) + value


from math import ceil
from collections import Counter

def total_cost(calls):
  db = Counter()
  for call in calls:
    date, time, length = call.split(" ")
    db[date] += ceil(length/60)

  return sum([(i-100)*2+100 if i>100 or i for i in db.values()])



# 原始做法反思

# 总想把全部对象呈现出来，所以才会做 info,date,length 这些list
# 实际上可以在动态的过程中全部完成

# 代码的关键是使用 set 得到不重复的日期，然后用它创建空白字典
# 最后用列表中的值对应地去修改空白字典
# 这样做的麻烦之处在于，对于一个字典来讲，dict[key not happen before] 是会报错的
# 因此才需要使用 set 事先将所有的 key都准备好
# 使用 Counter 可以避免这个问题

# def total_cost(calls):
#  info = [i.split(" ") for i in calls]
#  date, length = [i[0] for i in info], [ceil(int(i[2])/60) for i in info]
#
#  date_set = set(date)
#  dict = {i:0 for i in date_set}
#
#  for i in range(len(date)):
#    dict[date[i]] += length[i]
#
#  return sum([(mins-100)*2+100 if mins>100 else mins for mins in dict.values()])






if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
