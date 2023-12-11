# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/11
Describe:674. 最长连续递增序列
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，
那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。
输入：nums = [2,2,2,2,2]
输出：1
解释：最长连续递增序列是 [2], 长度为1。
"""


def find_length_of_LCIS(nums: list):
    """
    :param nums:
    :return:
    44ms 击败 82.89%使用 Python3 的用户
    17.04MB 击败 57.08%使用 Python3 的用户
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    max_l = 1
    l = 0
    r = 1
    n = len(nums)
    while r < n:
        if nums[r] > nums[r - 1]:
            r += 1
            cnt = r - l
            max_l = max(max_l, cnt)
        else:
            cnt = r - l
            max_l = max(max_l, cnt)
            l = r
            r += 1
    return max_l


def find_length_of_LCIS_1(nums: list):
    """
    :param nums:
    :return:
    52ms 击败 42.58%使用 Python3 的用户
    17.04MB 击败 58.48%使用 Python3 的用户
    """
    n = len(nums)
    max_l = 0
    s = 0
    for i in range(n):
        if i > 0 and nums[i] <= nums[i - 1]:
            s = i
        max_l = max(max_l, i - s + 1)
    return max_l
