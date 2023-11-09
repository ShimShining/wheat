# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/9
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
    l = [8, 90, 34, 23, 66, 31, 4, 54, 17]
    print(radix_sort(l))


