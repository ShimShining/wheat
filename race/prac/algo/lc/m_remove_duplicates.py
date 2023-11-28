# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/28
Describe: 删除有序数组中的重复项 II
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，
返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。
不需要考虑数组中超出新长度后面的元素。

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7,
并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。
"""


def remove_duplicates(nums):
    """
    统计频率
    :param nums:
    :return:
    16ms 击败 91.29%使用 Python 的用户
    13.18MB 击败 9.55%使用 Python 的用户
    """
    d = dict()
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    for k, v in d.items():
        while v > 2:
            nums.remove(k)
            v -= 1
    return len(nums)


def remove_duplicates_1(nums):
    """
    双指针
    :param nums:
    :return:
    16ms 击败 91.29%使用 Python 的用户
    12.99MB 击败 61.13%使用 Python 的用户
    """
    slow = 2
    fast = 2
    while fast < len(nums):
        if nums[slow - 2] != nums[fast]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    print(remove_duplicates_1(nums))
