# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/19
Describe:计算黑白围棋周围的空位
"""


def go_cnt(arr):
    black = list(map(int, arr[0]))
    white = list(map(int, arr[1]))

    blacks = []
    for i in range(0, len(black), 2):
        blacks.append((black[i], black[i + 1]))
    whites = []
    for j in range(0, len(white), 2):
        whites.append((white[j], white[j + 1]))
    black_empty = []
    for item in blacks:
        # (x+1, y)
        for x, y in [(item[0] + 1, item[1]), (item[0] - 1, item[1]), (item[0], item[1] + 1), (item[0], item[1] - 1)]:
            if 0 <= x <= 12 and 0 <= y <= 12 and (x, y) not in blacks and (x, y) not in whites and (
            x, y) not in black_empty:
                black_empty.append((x, y))

    white_empty = []
    for item in whites:
        # (x+1, y)
        for x, y in [(item[0] + 1, item[1]), (item[0] - 1, item[1]), (item[0], item[1] + 1), (item[0], item[1] - 1)]:
            if 0 <= x <= 12 and 0 <= y <= 12 and (x, y) not in blacks and (x, y) not in whites and (
            x, y) not in white_empty:
                white_empty.append((x, y))

    return len(black_empty), len(white_empty)


def go_cnt_1(arr):
    blacks = list(map(int, arr[0]))
    whites = list(map(int, arr[1]))

    black_coor = []
    for i in range(0, len(blacks), 2):
        black_coor.append((blacks[i], blacks[i + 1]))
    white_coor = []
    for i in range(0, len(whites), 2):
        white_coor.append((whites[i], whites[i + 1]))

    coordinates = [[0] * 12 for _ in range(12)]
    for i in range(12):
        for j in range(12):
            if (i, j) in black_coor:
                coordinates[i][j] = 1
            elif (i, j) in white_coor:
                coordinates[i][j] = 2

    def check(a, b, temp):
        if 0 <= a <= 12 and 12 >= b >= 0 == coordinates[a][b] and (a, b) not in temp:
            temp.append((a, b))

    black_empty = []
    for item in black_coor:
        for x, y in [(item[0] + 1, item[1]), (item[0] - 1, item[1]), (item[0], item[1] + 1), (item[0], item[1] - 1)]:
            check(x, y, black_empty)

    white_empty = []
    for item in white_coor:
        for x, y in [(item[0] + 1, item[1]), (item[0] - 1, item[1]), (item[0], item[1] + 1), (item[0], item[1] - 1)]:
            check(x, y, white_empty)

    return len(black_empty), len(white_empty)


if __name__ == '__main__':
    arr = [['0', '5', '8', '9', '9', '10'], ['5', '0', '9', '9', '9', '8']]
    print(go_cnt(arr))
    print(go_cnt_1(arr))
