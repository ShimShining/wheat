# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2024/1/13
Describe: 238. 除自身以外数组的乘积
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
输入: nums = [1,2,3,4]
输出: [24,12,8,6]
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
"""


def product_except_self(nums):
    length = len(nums)
    l, r, ans = [0] * length, [0] * length, [0] * length
    l[0] = 1
    for i in range(1, length):
        l[i] = l[i - 1] * nums[i - 1]
    r[-1] = 1
    for i in range(length - 2, -1, -1):
        r[i] = r[i + 1] * nums[i + 1]
    for i in range(length):
        ans[i] = l[i] * r[i]
    return ans


def product_except_self_1(nums):
    length = len(nums)
    ans, r = [0] * length, 1
    ans[0] = 1
    for i in range(1, length):
        ans[i] = nums[i - 1] * ans[i - 1]

    for i in reversed(range(length)):
        ans[i] = ans[i] * r
        r *= nums[i]

    return ans


def product_except_self_2(nums):
    length = len(nums)
    ans, prev, nxt = [1] * length, 1, 1
    i = 0
    j = length - 1
    while i < length:
        ans[i] *= prev
        ans[j] *= nxt
        prev *= nums[i]
        nxt *= nums[j]
        i += 1
        j -= 1
    return ans
