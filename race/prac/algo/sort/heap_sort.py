# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/23
Describe:堆排序
"""
from race.prac.ds.tree.bin_heap import BinHeap, MaxBinHeap


def min_heap_sort(nums):

    mh = BinHeap()
    mh.build_heap(nums)
    res = []
    for i in range(len(nums)):
        res.append(mh.del_min())

    return res
    # 有问题  BinHeap的del_min需要改 pop的时候带参数 self.heap_list.pop(self.current_size) 先pop 再size减一
    # for i in range(len(nums)):
    #     mh.heap_list.append(mh.del_min())
    #
    # return mh.heap_list


def max_heap_sort(nums):
    mbh = MaxBinHeap()
    mbh.build_heap(nums)
    length = len(nums)
    for i in range(length):
        mbh.heap_list.insert(length - i, mbh.del_max())
    mbh.heap_list.pop(0)
    return mbh.heap_list


if __name__ == '__main__':
    tmp_list = [1, 9, 34, 5, 12, 7, 9, 8, 1, 0, 13, 33]
    tmp_list2 = [1, 2, 1, 3, 4, 5, 6]
    tmp_list3_sorted = [0, 1, 2, 5, 7, 8, 9, 9, 12, 13, 33, 34]
    # print(f"tmp_list sorted = {min_heap_sort(tmp_list)}")
    # print(f"tmp_list2 sorted = {min_heap_sort(tmp_list2)}")
    # print(f"tmp_list2 sorted = {min_heap_sort(tmp_list3_sorted)}")

    print(f"tmp_list sorted = {max_heap_sort(tmp_list)}")
    print(f"tmp_list2 sorted = {max_heap_sort(tmp_list2)}")
    print(f"tmp_list2 sorted = {max_heap_sort(tmp_list3_sorted)}")


