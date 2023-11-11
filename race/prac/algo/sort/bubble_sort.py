# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/3
Describe: 冒泡排序回顾
1. 0 -> 1 谁最大谁往右,1 -> 2 谁最大谁往右 ... N-2 -> N-1 谁最大谁往右
2. 0 -> 1 谁最大谁往右,1 -> 2 谁最大谁往右 ... N-3 -> N-2 谁最大谁往右
...
"""


def bubble_sort(nums: list):

    if not nums or len(nums) < 2:
        return nums
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def bubble_sort_opt(nums: list):

    is_sorted = True
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_sorted = False

        if is_sorted:
            print(f"i={i}, j= {j}  -> is_sorted")
            return nums
    return nums


if __name__ == '__main__':
    tmp_list = [1, 9, 34, 5, 12, 7, 9, 8, 1, 0, 13, 33]
    tmp_list2 = [1, 2, 1, 3, 4, 5, 6]
    tmp_list3_sorted = [0, 1, 2, 5, 7, 8, 9, 9, 12, 13, 33, 34]
    print(f"tmp_list sorted = {bubble_sort(tmp_list)}")
    print(f"tmp_list2 sorted = {bubble_sort(tmp_list2)}")
    print(f"tmp_list sorted = {bubble_sort_opt(tmp_list)}")
    print(f"tmp_list2 sorted = {bubble_sort_opt(tmp_list2)}")
    print(f"tmp_list2 sorted = {bubble_sort_opt(tmp_list3_sorted)}")

