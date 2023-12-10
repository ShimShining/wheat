# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/10
Describe:NC52 有效括号序列
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

要求：空间复杂度 O(n)，时间复杂度 O(n)
输入：
"["
返回值：
false
输入：
"[]"
返回值：
true
"""


def is_valid(s):
    res = []
    n = len(s)
    i = 0
    while i < n:
        if s[i] in "([{":
            res.append(s[i])
        else:
            if not res:
                return False
            left = res.pop()
            if not match(left, s[i]):
                return False
        i += 1
    if res:
        return False
    return True


def match(l, r):
    pre = "([{"
    post = ')]}'
    return pre.index(l) == post.index(r)


if __name__ == '__main__':
    s = "()"
    print(is_valid(s))

