# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/1
Describe:给定两个正整数m和n，任务是生成一组由有序的，包含2个元素的元组(a,b) 构成的列表。
规则是m<=a<=b<=n 。

示例：
输入：(m=2, n=4) ，输出：[(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

题目难度：简单
"""


def generate_pairs(m: int, n: int) -> list:
    return [(i, j) for i in range(m, n + 1) for j in range(i, n + 1)]


if __name__ == "__main__":
    assert generate_pairs(2, 4) == [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
    assert generate_pairs(0, 1) == [(0, 0), (0, 1), (1, 1)]
    assert generate_pairs(0, 0) == [(0, 0)]
