#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2025/3/25 18:39
# @Author : hpf
# @Site : 
# @File : os_module.py
# @Software : PyCharm
import os
import shutil

# 获取当前脚本的绝对路径
abs_path = os.path.abspath(__file__)
print(abs_path)

# 获取当前文件的上上级目录 ls ../../
base_path = os.path.dirname( os.path.dirname(abs_path) )
print(base_path)

# 路径拼接
p1 = os.path.join(base_path, 'xx')
print(p1)

p2 = os.path.join(base_path, 'xx', 'oo', '1.png')
print(p2)

# 判断路径是否存在
path1_exists = os.path.exists(p1)
path2_exists = os.path.exists(p2)
print(path1_exists)
print(path2_exists)

# 创建文件夹
path_make = os.path.join(base_path, 'xx', 'oo')
print(path_make)
# if not os.path.exists(path_make):
#     os.makedirs(path_make)
# print(path_make)

# 是否是文件夹
file_path = os.path.join(base_path, 'xx', 'oo', '1.png')
is_dir = os.path.isdir(file_path)
print(is_dir)

# folder_path = os.path.join(base_path, 'xx', 'oo')
# is_dir = os.path.isdir(folder_path)
# print(is_dir)
# 是否是文件 os.path.isfile(xx)

# 删除文件或文件夹 没有文件报错
# path_remove = os.path.join(base_path, 'xx')
# shutil.rmtree(path_remove)

# 查看目录下所有文件
path_list = os.listdir(base_path)
print(path_list)









