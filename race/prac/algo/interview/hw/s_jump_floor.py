# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/5
Describe: NC68 跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

要求：时间复杂度：O(n) ，空间复杂度： O(1)
"""


def jump_floor(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return jump_floor(n-2) + jump_floor(n-1)


def jump_floor_ks(n, ks):
    if n == 1:
        ks[1] = 1
        return 1
    if n == 2:
        ks[2] = 2
        return 2
    if n in ks:
        return ks[n]
    return jump_floor_ks(n-1, ks) + jump_floor_ks(n-2, ks)


def jump_floor_dp(number):
    """dp"""
    if number < 3:
        return number
    a, b = 1, 2
    for i in range(number - 2):
        a, b = b, a + b
    return b


def jump_floor_dp_opt(number):
    """
    dp优化
    :param number:
    :return:
    """
    if number < 3:
        return number
    a, b, s = 1, 1, 2
    for i in range(2, number):
        a, b = b, s
        s = a + b
    return s
