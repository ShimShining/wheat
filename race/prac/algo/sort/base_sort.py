# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2021/9/30
Describe: 基数排序
"""
from collections import deque


class Queue(deque):
    enqueue = deque.appendleft
    dequeue = deque.pop
    is_empty = lambda q: len(q) == 0


def radix_sort(nums):
    cur_digit, digit_limit = 1, max(nums)

    main_queue = Queue()
    for i in nums:
        main_queue.enqueue(i)

    digit_queue = [Queue() for i in range(10)]

    while cur_digit <= digit_limit:
        while not main_queue.is_empty():
            num = main_queue.dequeue()
            digit_queue[(num // cur_digit) % 10].enqueue(num)

        for q in digit_queue:
            while not q.is_empty():
                main_queue.enqueue(q.dequeue())

        cur_digit *= 10

    res = []
    while not main_queue.is_empty():
        res.append(main_queue.dequeue())
    return res


if __name__ == '__main__':
    tmp_list = [1, 9, 34, 5, 12, 7, 9, 8, 1, 0, 13, 33]
    tmp_list2 = [1, 2, 1, 3, 4, 5, 6]
    tmp_list3_sorted = [0, 1, 2, 5, 7, 8, 9, 9, 12, 13, 33, 34]
    print(f"tmp_list sorted = {radix_sort(tmp_list)}")
    print(f"tmp_list2 sorted = {radix_sort(tmp_list2)}")
    print(f"tmp_list2 sorted = {radix_sort(tmp_list3_sorted)}")
