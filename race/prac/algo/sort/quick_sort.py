# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/13
Describe:快速排序
"""


def quick_sort(nums):
    quick_sort_handler(nums, 0, len(nums) - 1)


def quick_sort_handler(nums, first, last):
    if first < last:
        split_point = partition(nums, first, last)
        quick_sort_handler(nums, first, split_point - 1)
        quick_sort_handler(nums, split_point + 1, last)


def partition(nums, first, last):
    split_value = nums[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and nums[left_mark] <= split_value:
            left_mark += 1
        while nums[right_mark] >= split_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            nums[left_mark], nums[right_mark] = nums[right_mark], nums[left_mark]

    nums[first], nums[right_mark] = nums[right_mark], nums[first]
    return right_mark


if __name__ == '__main__':
    tmp_list = [1, 9, 34, 5, 12, 7, 9, 8, 1, 0, 13, 33]
    tmp_list2 = [1, 2, 1, 3, 4, 5, 6]
    tmp_list3_sorted = [0, 1, 2, 5, 7, 8, 9, 9, 12, 13, 33, 34]
    quick_sort(tmp_list)
    quick_sort(tmp_list2)
    quick_sort(tmp_list3_sorted)
    print(f"tmp_list sorted = {tmp_list}")
    print(f"tmp_list2 sorted = {tmp_list2}")
    print(f"tmp_list2 sorted = {tmp_list3_sorted}")

