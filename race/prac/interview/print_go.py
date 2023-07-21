# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/2
Describe:黑白围棋,5x5的棋盘,打印所有排列结果,使用分号结尾
"""


def combine_go():
    """
    暴力求解方式,有没其他方式
    :return:
    """
    go_list = ["黑", "白"]

    combine_list = []
    for e1 in go_list:
        for e2 in go_list:
            for e3 in go_list:
                for e4 in go_list:
                    for e5 in go_list:
                        combine_list.append(e1+e2+e3+e4+e5+";")
    return combine_list


def print_go():

    com_list = combine_go()

    for line1 in com_list:
        for line2 in com_list:
            for line3 in com_list:
                for line4 in com_list:
                    for line5 in com_list:
                        print(line1)
                        print(line2)
                        print(line3)
                        print(line4)
                        print(line5)
                        print("--------next-----------")


def iter_tools_permu():
    """
    这个方法不行
    :return:
    """
    import itertools
    print(itertools.permutations["黑", "白"], 5)


if __name__ == "__main__":

    print_go()
    # iter_tools_permu()
