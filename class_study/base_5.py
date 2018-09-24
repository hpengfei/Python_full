#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 12:25
# @Author  : hpengfei
# @File    : base_5.py
# @Software: PyCharm


# class Province:
#
#     country = "中国"
#
#     def __init__(self, name):
#         self.name = name
#
#
# hebei = Province('河北')
# print(Province.country)
# print(hebei.name)
# print(hebei.country)

# 类成员：
#    普通字段：保存在对象中，执行只能通过对象访问。
#    静态字段：保存在类中，  执行通过对象访问，也可以通过类访问。
#
#    普通方法：保存在类中，由对象来调用
#    静态方法：保存在类中，由类直接调用
#      类方法：

class Foo:

    def bar(self):
        # self 是对象
        print('Foo.bar')

    @staticmethod
    def sta():
        print('Foo.sta')

    @classmethod
    def classmd(cls):
        # cls 是类名
        print('Foo.classmd')


obj = Foo()
Foo.bar(obj)
Foo.sta()
Foo.classmd()



