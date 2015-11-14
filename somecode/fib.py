#coding=utf-8

#一只青蛙一次可以跳上1级台阶,也可以跳上2级,求青蛙跳上一个n级台阶总共有多少种跳法
#fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)

#
#一只青蛙一次可以跳上1级台阶,也可以跳上2级.....也可以跳上n级.求青蛙跳上一个n级台阶总共有多少种跳法
#fib = lambda n: 1 if n < 2 else 2 * fib(n-1)


#一只青蛙一次可以跳上1级台阶,也可以跳上2级,求青蛙跳上一个n级台阶总共有多少种跳法


#我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
#请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

f = lambda n: 1 if n < 2 else f(n - 1) + f(n - 2)

def fib(i):
    if i<=2:
        return 1
    return fib(i-1) + fib(i - 2)


n = int(raw_input("Please input your number>"))
print fib(n)
