# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/9
Describe: 进制转换
"""


def con_num_sys(num, base):
    convert_string = '0123456789ABCDEF'
    if num < base:
        return convert_string[num]
    return con_num_sys(num // base, base) + convert_string[num % base]


if __name__ == '__main__':
    print(con_num_sys(988, 16))

    import sys
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(3000)
    print(sys.getrecursionlimit())

