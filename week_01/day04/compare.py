#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/10 10:51
# @Author  : hpengfei
# @File    : compare.py
# @Software: PyCharm Community Edition

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")


def max_num(i, j, k):
    if i > j:
        max_number = i
    else:
        max_number = j
    if max_number < k:
        max_number = k
    return max_number


print(max_num(a, b, c))


