#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 19:36
# @Author  : hpengfei
# @File    : base_9.py
# @Software: PyCharm


class Foo:

    __v = 1111

    def __init__(self, name, age):
        self.name = name
        # self.age = age
        self.__age = age

    def show(self):
        return self.__age

    @staticmethod
    def stat():
        return Foo.__v

    def __f1(self):
        return "Foo.__f1"

    def f2(self):
        r = self.__f1()
        return r


obj = Foo('DF', 22)
# print(obj.name)
# print(obj.age)
# print(obj.__age)
# print(obj.show())
# ret = obj.stat()
# print(ret)
ret = obj.f2()
print(ret)
