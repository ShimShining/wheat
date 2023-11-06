# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/6
Describe: 十进制转换二进制
"""
from race.prac.ds.stack_ds.stack import Stack


def divide_by2(dec_num):
    rem_stack = Stack()
    while dec_num > 0:
        rem = dec_num % 2
        rem_stack.push(rem)
        dec_num = dec_num // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())

    return bin_string


def divide_by_n(dec_num, base=2):

    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    while dec_num > 0:
        rem = dec_num % base
        rem_stack.push(rem)
        dec_num = dec_num // base

    res = ""
    while not rem_stack.is_empty():
        res = res + digits[rem_stack.pop()]

    return res


if __name__ == '__main__':
    print(divide_by2(988))
    print(divide_by_n(988, 16))

