#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/15 22:48
# @Author  : hpengfei
# @File    : base_1.py
# @Software: PyCharm


class Bar:

    def foo(self, name, age, gender, content):
        print(name, age, gender, content)



obj = Bar()
obj.name = 'xiaoming'
obj.age = 10
obj.gender = 'man'
obj.foo()



