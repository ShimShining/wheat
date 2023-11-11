# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/11
Describe: 无序表顺序查找
"""


def unordered_list_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1
    return found


if __name__ == '__main__':
    test_list = [1, 3, 33, 9, 17, 19, 42, 13, 0]
    print(unordered_list_search(test_list, 13))
    print(unordered_list_search(test_list, 18))

