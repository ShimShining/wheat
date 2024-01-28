# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2024/1/28
Describe: 135. 分发糖果
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
"""


def h_candy(ratings):
    n = len(ratings)
    left = [0] * n
    for i in range(n):
        if i > 0 and ratings[i - 1] < ratings[i]:
            left[i] = left[i - 1] + 1
        else:
            left[i] = 1

    right, res = 0, 0
    for i in range(n - 1, -1, -1):
        if i < n - 1 and ratings[i] > ratings[i + 1]:
            right += 1
        else:
            right = 1
        res += max(left[i], right)
    return res


def h_candy_1(ratings):
    n = len(ratings)
    res = 1
    inc, dec, pre = 1, 0, 1
    for i in range(1, n):
        if ratings[i] >= ratings[i - 1]:
            dec = 0
            pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
            res += pre
            inc = pre
        else:
            dec += 1
            if dec == inc:
                dec += 1
            res += dec
            pre = 1
    return res
