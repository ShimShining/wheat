# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/26
Describe: 通用的深度优先搜索
"""
from race.prac.ds.graph.graph import Graph


class DFSGraph(Graph):
    """
    BFS采用队列存储待访问的顶点
    DFS则是通过递归调用,隐式使用了栈
        1. 一个顶点的发现时间总小于所有子顶点的发现时间
        2. 顶点的结束时间大于所有子顶点的结束时间
        3. O(V+E)
    强连通分支
        kosaraju算法
        Taryan算法
        Gabow算法
    """
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        # 颜色初始化
        for a_vertex in self:
            a_vertex.set_color('white')
            a_vertex.set_pred(-1)
        # 还有未包括的顶点,则建立森林
        for a_vertex in self:
            if a_vertex.get_color() == "white":
                self.dfs_visit(a_vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1   # 算法的步数
        start_vertex.set_discovery(self.time)
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == "white":
                next_vertex.set_pred(start_vertex)
                # 深度优先递归访问
                self.dfs_visit(next_vertex)
        start_vertex.set_color('black')
        self.time += 1
        start_vertex.set_finish(self.time)
