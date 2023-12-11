# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/11
Describe: LCR 119. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""


def longest_consecutive(nums: list) -> int:
    """
    :param nums:
    :return:
    68ms 击败 77.12%使用 Python3 的用户
    29.19MB 击败 43.79%使用 Python3 的用户
    """
    t = list(set(nums))
    t.sort()
    n = len(t)
    s = 0
    max_l = 0
    for i in range(n):
        if i > 0 and t[i] - t[i - 1] != 1:
            s = i
        max_l = max(max_l, i - s + 1)
    return max_l


def longest_consecutive_1(nums: list) -> int:
    """超出时间限制"""
    t = set(nums)
    max_l = 0
    for i in t:
        if i - 1 not in t and i + 1 not in t:
            max_l = max(max_l, 1)
        else:
            cur_l = 1
            while i + 1 in t:
                cur_l += 1
                i += 1
            max_l = max(max_l, cur_l)
    return max_l


def longest_consecutive_2(nums: list) -> int:
    """
    :param nums:
    :return:
    64ms 击败 85.62%使用 Python3 的用户
    29.21MB 击败 40.20%使用 Python3 的用户
    """
    t = set(nums)
    max_l = 0

    for num in t:
        if num - 1 not in t:
            cur = num
            cur_l = 1
            while cur + 1 in t:
                cur += 1
                cur_l += 1
            max_l = max(max_l, cur_l)
    return max_l
