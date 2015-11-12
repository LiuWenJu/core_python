#coding=utf-8
#中文注释
import sys

class A:

	s1 = 333 #共有属性
	__age = 0 #私有属性

	def __init__(self,age): #构造器 专有函数
		self.__age = age #
		return #

	def __del__(self): #析构 专有函数
		
		return

	def __doSomething(self,s): #私有函数
		print self.__age #类内部访问私有属性 外部不可访问
		return

	def doSomething(self,s): #共有函数
		self.__doSomething(s) #类内部访问私有函数 外部不可访问
		print s

def doSomething(v): #
	vv = v + 1 #
	return vv 

def main(): #
		
	a = A(111) #对象  对类实例化
	a.doSomething('222') #调用对象的共有函数
	print a.s1 #访问对象的共有属性
	print doSomething(444) #函数调用函数 同时被调用函数有返回值



if __name__ == '__main__': # 
	main()
