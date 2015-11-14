#coding=utf-8

def fib(i):
    a, b = 0, 1
    while a<i:
        print a,
        a, b = b, a+b


fib(10)
