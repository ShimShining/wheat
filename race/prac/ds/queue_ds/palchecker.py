# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/8
Describe: 回文词判断
"""
from race.prac.ds.queue_ds.deque import Deque


def palchecker(s):

    char_deque = Deque()
    for c in s:
        char_deque.add_rear(c)

    still_ok = True
    while char_deque.size() > 1 and still_ok:
        front = char_deque.remove_front()
        rear = char_deque.remove_rear()
        if front != rear:
            still_ok = False

    return still_ok


if __name__ == '__main__':
    print(palchecker("hsefsahekflsahef"))
    print(palchecker("radar"))
    print(palchecker("abccba"))
