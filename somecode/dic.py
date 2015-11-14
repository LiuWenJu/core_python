#coding=utf-8

"""
去除列表中的重复元素

"""


#用集合
l = ['b','c','d','b','c','a','a']
list(set(l))



#用字典
l1 = ['b', 'c', 'd', 'b', 'c', 'a']
l2 = {}.fromkeys(l1).keys()
print l2


#用字典并保持顺序
l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print l2


#列表推导式
l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = []
[l2.append(i) for i in l1 if not i in l2]
print l2


#
