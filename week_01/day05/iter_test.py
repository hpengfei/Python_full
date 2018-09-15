#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 10:37
# @Author  : hpengfei
# @File    : function.py
# @Software: PyCharm

import sys


# list_a = [1, 2, 3, 4, 5]
# iter_a = iter(list_a)
# print(next(iter_a))

# for i in iter_a:
#     print(i, end=" ")

# while True:
#     try:
#         print(next(iter_a), end=" ")
#     except StopIteration:
#         sys.exit()

# def fib(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a+b
#         counter += 1
#
#
# f = fib(1000)
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()


def cash_out(amount):
    while amount > 0:
        amount -= 1
        yield 1
        print(amount)
        print("擦，又来取钱了。。。败家子！")
        print()


ATM = cash_out(5)

print("取到钱 {} 万".format(next(ATM)))
print("取到钱 {} 万".format(next(ATM)))
print("取到钱 {} 万".format(next(ATM)))
print("取到钱 {} 万".format(next(ATM)))
print("取到钱 {} 万".format(next(ATM)))
# print("取到钱 {} 万".format(next(ATM)))


