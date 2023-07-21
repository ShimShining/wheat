# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2021/9/30
Describe: 分割列表的偶数和奇数
"""


def split_odd_even(nums: list):
    for num in nums:
        if num % 2 != 0:
            nums.remove(num)
            nums.insert(0, num)

    return nums


def split_odd_even_opt(nums: list):
    if len(nums) <= 1: return nums
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] % 2 == 0 and nums[r] % 2 > 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        elif nums[l] % 2 == 0 and nums[r] % 2 == 0:
            r -= 1
        elif nums[l] % 2 > 0 and nums[r] % 2 == 0:
            l += 1
            r -= 1
        elif nums[l] % 2 > 0 and nums[r] % 2 > 0:
            l += 1
    return nums


if __name__ == "__main__":
    tmp = [2, 3, 4, 5, 6, 7, 8, 8]
    tmp2 = [2, 3, 4, 5, 6, 7, 8, 8]
    tmp3 = [2, 2, 2, 2, 22, 2]
    res = split_odd_even(tmp)
    print(res)
    res1 = split_odd_even_opt(tmp3)
    print(res1)
