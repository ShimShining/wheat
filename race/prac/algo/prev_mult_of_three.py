# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/8/30
Describe:关于数字3的游戏，规则是输入一个数字n ，
如果n能被3整除则直接返回n 。如果不能，
那么尝试每次剔除掉一个末尾数字并检查剩下的数字能否被3整除，
如果可以就返回剩下的数字，否则返回None 。请编写一个python3函数来实现它吧。
"""


def prev_mult_of_three(num):

    if num % 3 == 0:
        return num
    s = str(num)[:-1]
    for i in range(0, len(s)):

        if int(s[:len(s)-i]) % 3 == 0:

            return int(s[:len(s)-i])
    return None


if __name__ == "__main__":

    assert prev_mult_of_three(36) == 36
    assert prev_mult_of_three(1) is None
    assert prev_mult_of_three(1244) == 12
    assert prev_mult_of_three(952406) == 9
    print("pass")


