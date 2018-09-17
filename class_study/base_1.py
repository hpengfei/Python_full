#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/15 22:48
# @Author  : hpengfei
# @File    : base_1.py
# @Software: PyCharm


# class Bar:
#
#     def foo(self, content):
#         print(self, self.name, self.age, self.gender, content)
#
#
# obj_1 = Bar()
# obj_1.name = '小明'
# obj_1.age = 10
# obj_1.gender = '男'
#
# obj_1.foo('吃饭')
# obj_1.foo('睡觉')
# obj_1.foo('打dota')


class Person:

    def __init__(self, name, age):

        self.n = name
        self.a = age

    def show(self):
        print("{} - {}".format(self.n, self.a))
        print("%s - %s" %(self.n, self.a))


pa = Person('PA', 24)
pa.show()
ta = Person('TA', 21)
ta.show()




