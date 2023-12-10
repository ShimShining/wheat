# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/10
Describe:1614.括号的最大嵌套深度
字符串是一个空字符串 ""，或者是一个不为 "(" 或 ")" 的单字符。
字符串可以写为 AB（A 与 B 字符串连接），其中 A 和 B 都是 有效括号字符串 。
字符串可以写为 (A)，其中 A 是一个 有效括号字符串 。
类似地，可以定义任何有效括号字符串 S 的 嵌套深度 depth(S)：

depth("") = 0
depth(C) = 0，其中 C 是单个字符的字符串，且该字符不是 "(" 或者 ")"
depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是 有效括号字符串
depth("(" + A + ")") = 1 + depth(A)，其中 A 是一个 有效括号字符串
例如：""、"()()"、"()(()())" 都是 有效括号字符串（嵌套深度分别为 0、1、2），而 ")(" 、"(()" 都不是 有效括号字符串 。

给你一个 有效括号字符串 s，返回该字符串的 s 嵌套深度
输入：s = "(1+(2*3)+((8)/4))+1"
输出：3
解释：数字 8 在嵌套的 3 层括号中。
输入：s = "(1)+((2))+(((3)))"
输出：3
"""



def max_depth(s: str) -> int:
    max_d = 0
    n = len(s)
    i = 0
    res = []
    while i < n:
        if s[i] == "(":
            res.append(s[i])
        else:
            if s[i] == ")":
                d = len(res)
                max_d = max(max_d, d)
                res.pop()
        i += 1
    return max_d


def max_depth_1(s):
    ans, count = 0, 0
    for c in s:
        if c == "(":
            count += 1
            ans = max(ans, count)
        elif c == ")":
            count -= 1
    return ans
