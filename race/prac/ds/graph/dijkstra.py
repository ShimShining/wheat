# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/26
Describe: 最短路径问题
"""
from race.prac.ds.tree.priority_queue import PriorityQueue


def dijkstra(a_graph, start):
    """
    路由采用的是距离向量路由算法,而非dijkstra算法
    O((V+E)logV)
    :param a_graph:
    :param start:
    :return:
    """
    pq = PriorityQueue()
    start.set_distance(0)
    pq.build_heap([(v.get_distance(), v) for v in a_graph])
    while not pq.is_empty():
        cur_vertex = pq.del_min()
        for next_vert in cur_vertex.get_connections():
            new_distance = cur_vertex.get_distance() + cur_vertex.get_weight(next_vert)
            if new_distance < next_vert.get_distance():
                next_vert.set_distance(new_distance)
                next_vert.set_pred(cur_vertex)
                pq.decrease_key(next_vert, new_distance)
