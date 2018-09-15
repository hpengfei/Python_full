#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 14:07
# @Author  : hpengfei
# @File    : practice_1.py
# @Software: PyCharm

# even = []
# odd = []
#
# for i in range(1, 101):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# print(even)
# print(odd)


number_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
number_dict = {}


for i in number_list:
    if i > 66:
        number_dict.setdefault('k1', []).append(i)
    if i < 66:
        number_dict.setdefault('k2', []).append(i)


print(number_dict)
