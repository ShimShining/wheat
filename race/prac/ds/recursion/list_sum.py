# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/9
Describe: list 求和
"""


def list_sum(num_list):

    s = 0
    for i in num_list:
        s += i
    return s


def list_sum_recursion(num_list):
    if len(num_list) == 1:
        return num_list[0]
    return num_list[0] + list_sum_recursion(num_list[1:])


if __name__ == '__main__':
    tmp = [1, 5, 4, 7, 100]
    print(list_sum(tmp))
    print(list_sum_recursion(tmp))
