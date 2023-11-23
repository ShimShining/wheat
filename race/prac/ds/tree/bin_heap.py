# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/23
Describe: 二叉堆
"""


class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, key):
        self.heap_list.append(key)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_up(self, i):
        """
        插入节点上浮
        :param i:
        :return:
        """
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
            i = i // 2

    def del_min(self):
        retval = self.heap_list[1]   # 移走堆顶
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def perc_down(self, i):
        while i * 2 <= self.current_size:
            mc_index = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc_index]:
                self.heap_list[i], self.heap_list[mc_index] = self.heap_list[mc_index], self.heap_list[i]
            i = mc_index  # 沿路径下沉

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2   # 唯一子节点
        # 返回较小的节点index
        if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def build_heap(self, nums):
        """
        insert建堆 时间复杂度是nlogn
        下沉法建堆 时间复杂度是n
        :param nums:
        :return:
        """
        i = len(nums) // 2
        self.current_size = len(nums)
        self.heap_list = [0] + nums[:]
        print(len(self.heap_list), i)
        while i > 0:
            print(self.heap_list, i)
            self.perc_down(i)
            i = i - 1
        print(self.heap_list, i)


if __name__ == '__main__':
    tmp = [1, 6, 5, 4, 7, 8, 9, 2, 0]
    bh = BinHeap()
    bh.build_heap(tmp)

