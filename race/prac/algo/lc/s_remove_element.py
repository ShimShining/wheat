# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/28
Describe:27. 移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。
例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,3,0,4]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素
"""


def remove_element(nums, val):
    """
    :param nums:
    :param val:
    :return:
    16ms 击败 78.23%使用 Python 的用户
    13.18MB 击败 5.12%使用 Python 的用户
    """
    # while val in nums:
    #     nums.remove(val)
    # return len(nums)
    tmp = []
    for i, elem in enumerate(nums):
        if elem == val:
            tmp.append(i)
    for i, index in enumerate(tmp):
        nums.pop(index - i)


def remove_element_1(nums, val):
    """
    :param nums:
    :param val:
    :return:
    20ms 击败 49.10%使用 Python 的用户
    13.11MB 击败 12.03%使用 Python 的用户
    """
    nums[:] = [num for num in nums if num != val]
    return len(nums)


def remove_element_2(nums, val):
    """
    双指针
    :param nums:
    :param val:
    :return:
    16ms 击败 78.23%使用 Python 的用户
    13.07MB 击败 18.56%使用 Python 的用户
    """
    l, r = 0, len(nums) - 1
    while l <= r:   # 要等于 不然边界条件会有问题 nums2 = [1] val=1
        if nums[r] == val:
            r -= 1
            continue
        if nums[l] == val:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        else:
            l += 1
    for i in range(len(nums) - r - 1):
        nums.pop()
    return r + 1


def remove_element_3(nums, val):
    """
    也是双指针
    从数组头开始
    :param nums:
    :param val:
    :return:
    """
    a = 0
    b = 0
    while a < len(nums):
        if nums[a] != val:
            nums[b] = nums[a]
            b += 1
        a += 1

    return b


if __name__ == '__main__':

    nums = [0,1,2,2,3,0,4,2]
    nums2 = [1]
    print(remove_element_3(nums, 2))
    print(nums)