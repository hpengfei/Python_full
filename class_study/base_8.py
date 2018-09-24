#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 18:12
# @Author  : hpengfei
# @File    : base_8.py
# @Software: PyCharm


class Foo:

    def f1(self):
        return "f1"

    def f2(self, v):
        print(v)

    def f3(self):
        print('del')

    per = property(fget=f1, fset=f2, fdel=f3, doc="doc")


obj = Foo()
ret = obj.per
print(ret)
obj.per = 11111
del obj.per
