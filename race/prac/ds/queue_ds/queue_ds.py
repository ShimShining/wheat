# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/8
Describe: 队列
"""


class Queue:
    """
    List 容纳Queue的数据项
    List的末端作为队首
    List的首端作为队尾
    enqueue()复杂度为 O(n)
    dequeue()复杂度为O(1)
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

