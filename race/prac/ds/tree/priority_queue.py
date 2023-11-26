# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/26
Describe: 优先队列
"""
import unittest


class PriorityQueue:
    def __init__(self):
        self.heap_array = [(0, 0)]
        self.current_size = 0
        
    def build_heap(self, nums):
        self.current_size = len(nums)
        self.heap_array = [(0, 0)]
        for i in nums:
            self.heap_array.append(i)
        i = len(nums) // 2
        while i > 0:
            self.perc_down(i)
            i -= 1
    
    def perc_down(self, i):
        while i * 2 <= self.current_size:
            mc = self.min_child(i)
            if self.heap_array[i][0] > self.heap_array[mc][0]:
                self.heap_array[i], self.heap_array[mc] = self.heap_array[mc], self.heap_array[i]
            i = mc
            
    def min_child(self, i):
        if i * 2 > self.current_size:
            return -1
        if i * 2 + 1 > self.current_size or self.heap_array[i*2][0] < self.heap_array[i*2+1][0]:
            return i * 2
        return i * 2 + 1
    
    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_array[i][0] < self.heap_array[i//2][0]:
                self.heap_array[i], self.heap_array[i//2] = self.heap_array[i//2], self.heap_array[i]
            i = i // 2
            
    def add(self, k):
        self.heap_array.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)
    
    def del_min(self):
        root_val = self.heap_array[1][1]
        self.heap_array[1] = self.heap_array[self.current_size]
        self.current_size -= 1
        self.heap_array.pop()
        self.perc_down(1)
        return root_val
    
    def is_empty(self):
        if self.current_size == 0:
            return True
        return False
    
    def decrease_key(self, val, amt):
        done = False
        i = 1
        my_key = 0
        while not done and i <= self.current_size:
            if self.heap_array[i][1] == val:
                done = True
                my_key = i
            else:
                i += 1
        if my_key > 0:
            self.heap_array[my_key] = (amt, self.heap_array[my_key][1])
            self.perc_up(my_key)
    
    def __contains__(self, item):
        for pair in self.heap_array:
            if pair[1] == item:
                return True
        return False


class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.theHeap = PriorityQueue()
        self.theHeap.add((2, 'x'))
        self.theHeap.add((3, 'y'))
        self.theHeap.add((5, 'z'))
        self.theHeap.add((6, 'a'))
        self.theHeap.add((4, 'd'))

    def testInsert(self):
        assert self.theHeap.current_size == 5

    def testdel_min(self):
        assert self.theHeap.del_min() == 'x'
        assert self.theHeap.del_min() == 'y'

    def testDecKey(self):
        self.theHeap.decrease_key('d', 1)
        assert self.theHeap.del_min() == 'd'


if __name__ == '__main__':
    unittest.main()


                

