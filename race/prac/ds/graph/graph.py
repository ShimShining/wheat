# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/26
Describe: 图
1. 广度优先搜索算法BFS,解决无权图的最短路径问题(词梯问题)
2. 带权图最短路径的dijkstra算法
3. 图的深度优先搜索算法DFS(骑士周游问题)
4. 用于简化图的强连通分支算法
5. 用于关联任务排序的拓扑排序算法
6. 用于广播消息的最小生成树算法
"""
import sys


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def add_neighbor(self, nbr_obj, weight=0):
        self.connected_to[nbr_obj] = weight

    def set_color(self, color):
        self.color = color

    def set_distance(self, d):
        self.dist = d

    def set_pred(self, p):
        self.pred = p

    def set_discovery(self, dtime):
        self.disc = dtime

    def set_finish(self, ftime):
        self.fin = ftime

    def get_finish(self):
        return self.fin

    def get_discovery(self):
        return self.disc

    def get_pred(self):
        return self.pred

    def get_distance(self):
        return self.dist

    def get_color(self):
        return self.color

    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(
            self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred) + "]\n"

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr_obj):
        return self.connected_to[nbr_obj]


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.vertices_num = 0

    def add_vertex(self, key):
        """添加顶点"""
        self.vertices_num += 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        """通过key查找"""
        if key in self.vertex_list:
            return self.vertex_list[key]
        return None

    def __contains__(self, item):
        return item in self.vertex_list

    def add_edge(self, from_v, to_v, cost=0):
        """添加边"""
        # 不存在的顶点先添加
        if from_v not in self.vertex_list:
            self.add_vertex(from_v)
        if to_v not in self.vertex_list:
            self.add_vertex(to_v)
        # 起始顶点添加邻接边信息
        self.vertex_list[from_v].add_neighbor(self.vertex_list[to_v], cost)

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())

    def __str__(self):
        return "Graph numbers: " + str(self.vertices_num) + '\n' \
               + str({k: str(v) for k, v in self.vertex_list.items()})


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        for w in v.get_connections():
            print(f"o_key={v.get_id()}; c_key={w.get_id()}")

    print(g.vertex_list[1])
    print(g)

