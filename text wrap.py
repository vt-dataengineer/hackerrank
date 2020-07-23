# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
#
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

# string, max_width = input(), int(input())
string = input()
max_width = int(input())
# y = 0
# while 1:
#     for x in range(y,max_width):
#         print(string[x])
#         y = max_width
#         max_width = max_width+max_width
#
# print(len(string))
# for x in range(0,len(string),max_width):
#     print(string[x:x+max_width])

import textwrap

print(textwrap.fill(string,max_width))