# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/6
Describe:请编写一个函数，接收两个参数：一个是数字列表nums，一个是数字n。
返回列表中任意两个数字的差值刚好是n的所有组合的个数。
示例：
输入：(nums=[1, 1, 5, 6, 9, 16, 27], n=4)，输出3。因为组合情况可以是：(1,5), (1,5), (5,9)
"""


def int_diff(nums: list, n: int) -> int:

    count = 0
    for num in nums:
        if num + n in nums:
            count += nums.count(num+n)

    return count


def int_diff_oth(nums, n):

    count = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if abs(nums[i] - nums[j]) == n:
                count += 1

    return count


if __name__ == "__main__":

    assert int_diff([1, 1, 5, 6, 9, 16, 27], 4) == 3
    assert int_diff([1, 1, 3, 3], 2) == 4

    assert int_diff_oth([1, 1, 5, 6, 9, 16, 27], 4) == 3
    assert int_diff_oth([1, 1, 3, 3], 2) == 4
