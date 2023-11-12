# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/12
Describe: 希尔排序
"""


def shell_sort(nums):

    sub_list_cnt = len(nums) // 2
    while sub_list_cnt > 0:
        for start_pos in range(sub_list_cnt):
            gap_insertion_sort(nums, start_pos, sub_list_cnt)

        sub_list_cnt = sub_list_cnt // 2
    return nums


def gap_insertion_sort(nums, start, gap):
    for i in range(start + gap, len(nums), gap):
        cur_val = nums[i]
        pos = i
        while pos >= gap and nums[pos - gap] > cur_val:
            nums[pos] = nums[pos - gap]
            pos = pos - gap
        nums[pos] = cur_val


if __name__ == '__main__':
    tmp_list = [1, 9, 34, 5, 12, 7, 9, 8, 1, 0, 13, 33]
    tmp_list2 = [1, 2, 1, 3, 4, 5, 6]
    tmp_list3_sorted = [0, 1, 2, 5, 7, 8, 9, 9, 12, 13, 33, 34]
    print(f"tmp_list sorted = {shell_sort(tmp_list)}")
    print(f"tmp_list2 sorted = {shell_sort(tmp_list2)}")
    print(f"tmp_list2 sorted = {shell_sort(tmp_list3_sorted)}")


