# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/3
Describe: 选择排序
1. 从0 -> N -1 位置找最小的数,将其放在0位置上
2. 从1 -> N-1 位置找最小的数,将其放在1位置上
...
"""


def selection_sort(nums: list):

    if not nums or len(nums) < 2:
        return
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            min_index = j if nums[min_index] > nums[j] else min_index

        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


if __name__ == '__main__':
    tmp_list = [1, 9, 34, 5, 12, 7, 9, 8, 1, 0, 13, 33]
    tmp_list2 = [1, 2, 1, 3, 4, 5, 6]
    print(f"tmp_list sorted = {selection_sort(tmp_list)}")
    print(f"tmp_list2 sorted = {selection_sort(tmp_list2)}")

