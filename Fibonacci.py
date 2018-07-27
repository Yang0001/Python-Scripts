#!/usr/bin/env python
# coding:utf-8

def method_A():
    a=0
    b=1
    while b < 10:
        print(b)
        a, b = b, a+b


def method_B():
    a = 0
    b = 1
    while b < 10:
        print(b, end=',')  # end 可以将print输出到同一行并以 ,号结尾
        a, b = b, a + b

def method_C():
    lis = []
    for i in range(20):
        if i == 0 or i == 1:  # 第1,2项 都为1
            lis.append(1)
        else:
            lis.append(lis[i - 2] + lis[i - 1])  # 从第3项开始每项值为前两项值之和
    print(lis)

# Yield
def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1

def Fibonacci_Yield(n):
    # return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
    return list(Fibonacci_Yield_tool(n))

# 递归
def Fibonacci_Recursion_tool(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)

def Fibonacci_Recursion(n):
    result_list = []
    for i in range(1, n + 1): result_list.append(Fibonacci_Recursion_tool(i))
    return result_list