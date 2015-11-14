#coding=utf-8

#fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)


def fib(i):
    if i<=2:
        return 1
    return fib(i-1) + fib(i - 2)


n = int(raw_input("Please input your number>"))
print fib(n)
