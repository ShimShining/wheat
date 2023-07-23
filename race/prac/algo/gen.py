# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/8
Describe:生成器
"""

def gen():

    print("第一次调用")
    yield 1
    print("第2次调用")
    yield 2


if __name__ == "__main__":

    ret = gen()
    print("ret前")
    print(next(ret))
    print("第2次")
    print(next(ret))

