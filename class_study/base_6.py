#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 17:09
# @Author  : hpengfei
# @File    : base_6.py
# @Software: PyCharm


class Foo:

    def __init__(self):
        self.name = 'Foo'
        self.name_list = ['DF']

    def bar(self):
        print('Foo.bar')

    # 属性 用于执行 obj.per
    @property
    def per(self):
        print('Foo.per')
        return self.name_list[0]

    # 可以进行 obj.per = 111111
    @per.setter
    def per(self, val):
        print(val)

    @per.deleter
    def per(self):
        print('per.deleter')


obj = Foo()
print(obj.name)
r = obj.per
print(r)
# obj.per = 1111
# del obj.per




