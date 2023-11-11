# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/11
Describe: 有序表查找
"""


def ordered_list_search(a_list, item):

    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    return found


def ordered_list_binary_search(nums, item):
    """
    有序表 二分查找
    :param nums:
    :param item:
    :return:
    """
    first = 0
    last = len(nums) - 1
    found = False

    while first <= last and not found:
        mid_pos = (first + last) // 2
        if nums[mid_pos] == item:
            found = True
        else:
            if item < nums[mid_pos]:
                last = mid_pos - 1
            else:
                first = mid_pos + 1

    return found


def binary_search_recursion(nums, item):

    if len(nums) == 0:
        return False
    mid_pos = len(nums) // 2
    if nums[mid_pos] == item:
        return True
    if nums[mid_pos] > item:
        return binary_search_recursion(nums[:mid_pos], item)
    if nums[mid_pos] < item:
        return binary_search_recursion(nums[mid_pos + 1:], item)


if __name__ == '__main__':
    test_list = [0, 1, 3, 9, 13,  17, 19, 33, 42]
    print(ordered_list_search(test_list, 13))
    print(ordered_list_search(test_list, 18))

    print(ordered_list_binary_search(test_list, 13))
    print(ordered_list_binary_search(test_list, 18))
    print(binary_search_recursion(test_list, 13))
    print(binary_search_recursion(test_list, 18))


