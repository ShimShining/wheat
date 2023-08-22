# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2021/11/10
Describe:给定一个英文单词和空格组成的字符串words，请编写一个函数，按照每个单词最后一个字母在字母表中的顺序排列，
返回重新排列后的列表。如果两个单词拥有相同的字母，则在返回结果中按照给定的原字符串中的位置进行排列。
示例：
输入：take me to semynak，输出：["take", "me", "semynak", "to"]。
"""


def sort_by_last_char(words: str) -> list:

    return sorted(words.split(), key=lambda x: x[-1])


if __name__ == "__main__":

    assert sort_by_last_char("man i need a taxi up to ubupd") == ["a", "need", "ubupd", "i", "taxi", "man", "to", "up"]
    assert sort_by_last_char("take me to semynak") == ["take", "me", "semynak", "to"]
    assert sort_by_last_char("massage yes massage yes massage") == ["massage", "massage", "massage", "yes", "yes"]
    print("DONE")




