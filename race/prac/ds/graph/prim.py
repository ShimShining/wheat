# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/26
Describe: 最小生成树
贪心算法: 网络消息路由传播
"""
import sys
from race.prac.ds.tree.priority_queue import PriorityQueue


def prim(g, start):
    pq = PriorityQueue()
    for v in g:
        v.set_dictance(sys.maxsize)
        v.set_pred = None
    start.set_distance(0)
    pq.build_heap([(v.get_distance(), v) for v in g])
    while not pq.is_empty():
        cur_vert = pq.del_min()
        for next_vert in cur_vert.get_connections():
            new_cost = cur_vert.get_weight(next_vert)
            if next_vert in pq and new_cost < next_vert.get_distance():
                next_vert.set_pred(cur_vert)
                next_vert.set_distance(new_cost)
                pq.decrease_key(next_vert, new_cost)
