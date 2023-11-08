# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/8
Describe:热土豆,土豆传递问题
"""
from race.prac.ds.queue_ds.queue_ds import Queue


def hot_potato(name_list, num):
    """
    约瑟夫问题
    :param name_list:
    :param num:
    :return:
    """
    q = Queue()
    for name in name_list:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num - 1):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


if __name__ == '__main__':

    names = list(range(40))
    live = hot_potato(names, 7)
    print(live)

