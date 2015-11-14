#coding=utf-8

#直接方法
dict = {'name': 'earth', 'port': '80'}


#工厂方法
items = [('name', 'earth'), ('port', '80')]
dict2 = dict(items)
dict1 = dict((['name', 'earth'], ['port', '80']))


#fromkeys()方法
dict1 = {}.fromkeys(('x', 'y'), -1)
dict={'x': -1,'y': -1}
dict2 = {}.fromkeys(('x', 'y'))
dict2 = {'x':None, 'y': None}


