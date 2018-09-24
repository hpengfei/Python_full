#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 0:12
# @Author  : hpengfei
# @File    : base_10.py
# @Software: PyCharm


class F:
    def __init__(self):
        self.ge = 123
        self.__gene = 123


class S(F):

    def __init__(self, name):
        self.name = name
        self.__age = 18
        super(S, self).__init__()

    def show(self):
        print(self.name)
        print(self.__age)
        print(self.ge)
    #     print(self.__gene)  # 无法访问父类的私有字段，只能在父类定义一个方法才能访问父类的私有字段


obj = S('AM')
obj.show()

