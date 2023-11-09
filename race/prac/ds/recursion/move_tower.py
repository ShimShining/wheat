# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/9
Describe: 汉诺塔
"""


def move_tower(height, from_pole, mid_pole, to_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, to_pole, mid_pole)
        move_disk(height, from_pole, to_pole)
        move_tower(height - 1, mid_pole, from_pole, to_pole)


def move_disk(disk, from_pole, to_pole):

    print(f"disk[{disk}] from {from_pole} to  {to_pole}")


if __name__ == '__main__':
    move_tower(3, "#1", "#2", "#3")

