# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/26
Describe: 骑士周游问题
深度优先搜索
"""
from race.prac.ds.graph.graph import Graph


def gen_legal_moves(x, y, bd_size):
    new_moves = []
    move_offsets = [(-1, -2), (-1, 2), (-2, 1), (-2, -1),
                    (1, -2), (1, 2), (2, -1), (2, 1)]

    for i in move_offsets:
        new_x = x + i[0]
        new_y = y + i[1]
        if legal_coord(new_x, bd_size) and legal_coord(new_y, bd_size):
            new_moves.append((new_x, new_y))
    return new_moves


def legal_coord(x, bd_size):
    if 0 <= x < bd_size:
        return True
    return False


def knight_graph(bd_size):
    kt_g = Graph()
    # 遍历给个棋格
    for row in range(bd_size):
        for col in range(bd_size):
            cur_node_id = gen_node_id(row, col, bd_size)
            new_positions = gen_legal_moves(row, col, bd_size)  # 单步合法走棋
            for e in new_positions:
                next_node_id = gen_node_id(e[0], e[1], bd_size)
                # 添加边和顶点
                kt_g.add_edge(cur_node_id, next_node_id)
    return kt_g


def gen_node_id(row, col, bd_size):
    return row * bd_size + col


def knight_tour(step, path, cur_vertex, limit):
    """
    DFS
    :param step: 层次
    :param path: 路径
    :param cur_vertex: 当前顶点
    :param limit: 搜索总深度
    :return:
    """
    cur_vertex.set_color('gray')
    # 当前顶点加入路径
    path.append(cur_vertex)
    if step < limit:
        # 对所有合法移动逐一深入
        nbr_list = list(cur_vertex.get_connections())
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            # 选择白色未经过的顶点深入
            if nbr_list[i].get_color() == 'white':
                done = knight_tour(step+1, path, nbr_list[i], limit)  # step+1 层次加1,递归深入
            i = i + 1
        # 都无法完成总深度,回溯,进行当前层次的下一个节点探索
        if not done:
            path.pop()
            cur_vertex.set_color('white')
    else:
        done = True
    return done


def order_by_avail(n):
    res_list = []
    for v in n.get_connections():
        if v.get_color() == "white":
            c = 0
            for w in v.get_connections():
                if w.get_color() == "white":
                    c += 1
            res_list.append((c, v))
    res_list.sort(key=lambda x: x[0])
    return [y[1] for y in res_list]

