# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/7
Describe:请编写一个函数，接收一个正整数n，返回一个由其子列表组成的列表。子列表按长度升序排列。

示例：
输入：2，返回： [[1], [1, 1]]
"""


def pyramid(n: int) -> list:
    return [[1] * i for i in range(1, n + 1)]


if __name__ == "__main__":
    assert pyramid(0) == []
    assert pyramid(2) == [[1], [1, 1]]
    assert pyramid(3) == [[1], [1, 1], [1, 1, 1]]
