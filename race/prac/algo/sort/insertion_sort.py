# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/11
Describe: 插入排序
"""


def insertion_sort(nums):
    for index in range(1, len(nums)):
        cur_val = nums[index]
        pos = index
        while pos > 0 and nums[pos - 1] > cur_val:
            nums[pos] = nums[pos - 1]
            pos -= 1

        nums[pos] = cur_val
    return nums


if __name__ == '__main__':
    tmp_list = [1, 9, 34, 5, 12, 7, 9, 8, 1, 0, 13, 33]
    tmp_list2 = [1, 2, 1, 3, 4, 5, 6]
    tmp_list3_sorted = [0, 1, 2, 5, 7, 8, 9, 9, 12, 13, 33, 34]
    print(f"tmp_list sorted = {insertion_sort(tmp_list)}")
    # print(f"tmp_list2 sorted = {insertion_sort(tmp_list2)}")
    # print(f"tmp_list2 sorted = {insertion_sort(tmp_list3_sorted)}")
