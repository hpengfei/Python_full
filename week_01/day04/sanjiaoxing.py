#!/usr/bin/env python

height = int(input("Height:"))
# width = int(input("Width:"))

# 正序
# for i in range(1, height+1):
#     for j in range(i):
#         print("#", end="")
#     print()

# 倒序
for i in range(height, 0, -1):
    for j in range(i):
        print("#", end="")
    print()

