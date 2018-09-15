#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/10 10:50
# @Author  : hpengfei
# @File    : login.py
# @Software: PyCharm Community Edition
# 输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后锁定



user = 'hello'
password = 'world'

if os.path.isfile('.flag'):
    pass_flag = open('.flag', 'r+', encoding='utf-8')
else:
    pass_flag = open('.flag', 'w+', encoding='utf-8')

if pass_flag.readline().strip() == '':
    flag = 3
else:
    pass_flag.seek(0)
    flag = int(pass_flag.readline())
break_flag = True

while break_flag:
    if 0 < flag <= 3:
        user_name = input("Please input user:")
        user_pass = input("Please input password:")
        if user_name == user and user_pass == password:
            print("登录成功!")
            break_flag = False
        else:
            print("帐号或者密码错误!")
            flag -= 1
            print("你还剩余{}次输入次数!".format(flag))
            pass_flag.seek(0)
            pass_flag.write(str(flag))
            pass_flag.flush()
    else:
        print("输入错误超过三次,已经锁定该帐号!")
        break_flag = False



