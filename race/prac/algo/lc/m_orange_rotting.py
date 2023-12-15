# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/15
Describe:994. 腐烂的橘子
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
"""


def orange_rotting(grid: list):
    """
    BFS
    :param grid:
    :return:
    56ms 击败 26.82%使用 Python3 的用户
    15.98MB击败 67.18%使用 Python3 的用户
    """
    if not grid:
        return -1
    q = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                q.append((i, j, 0))

    def check(g, i, j):
        if 0 <= i < len(g) and 0 <= j < len(g[0]) and g[i][j] == 1:
            return True
        return False
    d = 0
    while q:
        x, y, d = q.pop(0)
        # (x-1, y), (x+1, y), (x, y-1), (x, y+1)
        for s in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if check(grid, s[0], s[1]):
                grid[s[0]][s[1]] = 2
                q.append((s[0], s[1], d + 1))
    if any(1 in row for row in grid):
        return -1
    return d


if __name__ == '__main__':
    g = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(orange_rotting(g))
