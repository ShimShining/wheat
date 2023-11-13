# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/13
Describe: 归并排序
"""


def merge_sort(nums):

    if len(nums) > 1:

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    return nums


def merge_sort_opt(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort_opt(nums[:mid])
    right = merge_sort_opt(nums[mid:])

    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged


if __name__ == '__main__':
    tmp_list = [1, 9, 34, 5, 12, 7, 9, 8, 1, 0, 13, 33]
    tmp_list2 = [1, 2, 1, 3, 4, 5, 6]
    tmp_list3_sorted = [0, 1, 2, 5, 7, 8, 9, 9, 12, 13, 33, 34]
    # print(f"tmp_list sorted = {merge_sort(tmp_list)}")
    # print(f"tmp_list2 sorted = {merge_sort(tmp_list2)}")
    # print(f"tmp_list2 sorted = {merge_sort(tmp_list3_sorted)}")

    print(f"tmp_list sorted = {merge_sort_opt(tmp_list)}")
    print(f"tmp_list2 sorted = {merge_sort_opt(tmp_list2)}")
    print(f"tmp_list2 sorted = {merge_sort_opt(tmp_list3_sorted)}")


