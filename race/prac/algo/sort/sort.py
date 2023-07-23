# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/6
Describe:排序算法
"""


# 冒泡
def bubble_sort(nums: list):
    for i in range(1, len(nums)):
        for j in range(0, len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# 冒泡优化1 第二次循环只到上次交换的位置
def bubble_sort1(nums: list):
    for i in range(1, len(nums)):
        for j in range(0, len(nums) - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# 冒泡优化2 针对完全有序的做优化
def bubble_sort2(nums: list):
    for i in range(1, len(nums)):
        sort_flag = True
        for j in range(0, len(nums) - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            sort_flag = False
        if sort_flag: break
    return nums


# 冒泡优化3,记录尾部有序数组的位置,下一次循环从该位置开始
def bubble_sort3(nums: list):
    length = len(nums)
    for i in range(1, length):
        sort_index = 1
        for j in range(0, len(nums) - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            sort_index = j
        length = sort_index
    return nums


# 插入排序
def insertion_sort(nums: list):
    for i in range(len(nums)):
        pre_index = i - 1
        cur = nums[i]
        while pre_index >= 0 and nums[pre_index] > cur:
            nums[pre_index + 1] = nums[pre_index]
            pre_index -= 1
        nums[pre_index + 1] = cur

    return nums


if __name__ == "__main__":
    tmp_list = [9, 34, 5, 12, 7, 9, 8, 1, 0, 13]
    print(f"bubble_sort res is: {bubble_sort(tmp_list)}")
    print(f"bubble_sort1 res is: {bubble_sort1(tmp_list)}")
    print(f"bubble_sort2 res is: {bubble_sort2(tmp_list)}")
    print(f"bubble_sort3 res is: {bubble_sort3(tmp_list)}")
    print(f"insertion_sort res is: {insertion_sort(tmp_list)}")
