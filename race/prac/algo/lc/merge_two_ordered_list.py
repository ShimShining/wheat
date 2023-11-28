# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/28
Describe: 88. 合并两个有序数组
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
"""


def merge(nums1, m, nums2, n):
    """
    合并nums2 到nums1中
    对nums1 进行排序
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """
    # nums1[m:] = nums2
    # nums1.sort()
    for i in range(n):
        nums1[m + i] = nums2[i]
    nums1.sort()


def merge_primer(nums1, m, nums2, n):
    """
    双指针
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    16ms
    击败 78.99%使用 Python 的用户
    13.09MB
    击败 19.33%使用 Python 的用户
    """
    i, j = 0, 0
    tmp = []
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            tmp.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            tmp.append(nums2[j])
            j += 1
        else:
            tmp.append(nums1[i])
            i += 1
            tmp.append(nums2[j])
            j += 1
    while i < m:
        tmp.append(nums1[i])
        i += 1
    while j < n:
        tmp.append(nums2[j])
        j += 1
    nums1[:] = tmp


def merge_primer_local(nums1, m, nums2, n):
    """
    双指针本地版本 逆向双指针
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    12ms 击败 94.90%使用 Python 的用户
    13.12MB 击败 12.80%使用 Python 的用户
    """
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        elif nums1[m - 1] < nums2[n - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    while n > 0:
        nums1[n - 1] = nums2[n - 1]
        n -= 1


if __name__ == '__main__':
    nums1 = [0, 0, 3, 0, 0, 0, 0, 0, 0]
    m = 3
    nums2 = [-1, 1, 1, 1, 2, 3]
    n = 6
    merge_primer_local(nums1, m, nums2, n)
