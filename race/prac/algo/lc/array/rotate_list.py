# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/6
Describe: 189. 轮转数组
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""
import math


def rotate(nums, k):
    """
    :param nums:
    :param k:
    :return:
    44ms 击败 91.61%使用 Python3 的用户
    24.08MB 击败 16.80%使用 Python3 的用户
    """
    if not nums or len(nums) == 1:
        return nums
    n = len(nums)
    res = [0] * n
    for i in range(n):
        new_index = (i + k) % n
        res[new_index] = nums[i]
    nums[:] = res


def rotate_1(nums, k):
    """
    :param nums:
    :param k:
    :return:
    40ms 击败 96.70%使用 Python3 的用户
    23.78MB 击败 81.48%使用 Python3 的用户
    """
    if not nums or len(nums) == 1:
        return
    n = len(nums)
    k = k % n
    nums[:] = nums[n - k:] + nums[:n - k]


def rotate_2(nums, k):
    """
    在nums内计算出新index进行交换
    外圈交换次数=k,n的最小公约数次
    内圈需交换到目标index等于当前index
    :param nums:
    :param k:
    :return:
    56ms 击败 53.99%使用 Python3 的用户
    23.96MB 击败 38.72%使用 Python3 的用户
    """
    if not nums or len(nums) == 1:
        return
    n = len(nums)
    k = k % n
    count = math.gcd(k, n)
    start = 0
    while start < count:
        cur = start
        pre = nums[start]
        while True:
            nxt = (cur + k) % n
            pre, nums[nxt] = nums[nxt], pre
            cur = nxt
            if start == cur:
                break
        start += 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(rotate_2(nums, 3))
    print(nums)
