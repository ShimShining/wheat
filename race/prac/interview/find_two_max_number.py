# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/31
Describe:找出数组中最大的俩个数
"""


def find_number(arr):

    length = len(arr)
    if length == 0:
        return
    if length == 1:
        return arr[0], None
    for i in range(length):

        for j in range(i, length):

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr[-1], arr[-2]


def find_number_sort(arr):

    length = len(arr)
    if length == 0:
        return
    if length == 1:
        return arr[0], None
    for i in range(length-1, 0):
        if i == length-3:
            break
        for j in (i-1, 0):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr[-1], arr[-2]


def find_two_max(arr):

    max_val = 0
    max_sec = 0
    for item in arr:

        if item > max_val:
            max_val = item
        elif max_sec < item:
            max_sec = item

    return max_val, max_sec


if __name__ == "__main__":
    temp = [3, 6, 9, 3, 8, 7]
    # temp = [0, 0, 0, 0, 0, 7]
    res = find_number(temp)
    print(res)
    # res2 = find_two_max(temp)
    #
    # print(res2)
    temp = [1]
    res3 = find_number_sort(temp)
    print(res3)