# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/26
Describe: 词梯问题
"""
from race.prac.ds.graph.graph import Graph
from race.prac.ds.queue_ds.queue_ds import Queue


def build_graph(word_file):
    d = dict()
    g = Graph()
    w_file = open(word_file, 'r')
    # 按单词长度建立桶 POLE ==> 建立四个桶, bucket分别为_OLE, P_LE, PO_E, POL_
    for line in w_file:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # 同一个桶单词之间建立边的关系
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g


def bfs(g, start):
    start.set_distance(0)
    start.set_pred(None)
    vert_queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        cur_vert = vert_queue.dequeue()
        for nbr in cur_vert.get_connections():
            if nbr.get_color() == 'white':
                nbr.set_color("gray")
                nbr.set_distance(cur_vert.get_distance() + 1)
                nbr.set_pred(cur_vert)
                vert_queue.enqueue(nbr)
        cur_vert.set_color('black')


def traverse(y):
    x = y
    while x.get_pred():
        print(x.get_id())
        x = x.get_pred()
    print(x.get_id())


if __name__ == '__main__':
    word_g = build_graph('word.txt')
    # print("FOOL" in word_g.vertex_list)
    s = word_g.get_vertex("FOOL")
    bfs(word_g, word_g.get_vertex("FOOL"))
    traverse(word_g.get_vertex("SAGE"))

