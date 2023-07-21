# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2021/9/23
Describe:查找输入的词里是否包含敏感词
"""


def find_sensitive_words(s: str, target: list):
    for words in target:
        l = len(words)
        if len(s) <= l and s != words:
            return False
        for i in range(len(s) - l + 1):
            if s[i:i + l] == words:
                res = s.replace(s[i:i + l], "*"*l)
                s = res
                # print(res)
                # return True

    return res


if __name__ == "__main__":
    s = "aadc"
    target = ['a', 'd', 'c']
    res = find_sensitive_words(s, target)
    print(res)
