#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 22:43
# @Author  : hpengfei
# @File    : base_2.py
# @Software: PyCharm


class F:

    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f2')


class S(F):

    def s1(self):
        print('S.s1')

    def f1(self):
        print('S.f1')

    def f2(self):
        # super(S, self).f2()  # 执行父类中的f2 方法
        F.f2(self)             # 执行父类中的f2 方法
        print('S.f2')


obj = S()
# obj.s1() # s1中的self是形参，此时代指obj
# obj.f1() # self用于指调用方法的调用者
obj.f2()


