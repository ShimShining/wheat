# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2021/9/16
Describe:给定一个文本字符串words和注释符号列表markers，请
编写函数，将其中注释标记后的文本都去除，包括字符串末尾的空格。
示例：

输入：("apples, pears # and bananas", ["#"])
输出："apples, pears"

输入："bananas !apples"
输出："bananas"

题目难度：中等
题目来源：codewars
"""
import re


def strip_comments(words: str, markers: list) -> str:
    if "\n" not in words:
        for s in words:
            if s in markers:
                return words.split(s)[0].strip()
    tmp = words.split("\n")
    res = []
    for item in tmp:
        for s in item:
            if s in markers:
                tmp_s = item.split(s)[0].strip()
                if tmp_s:
                    res.append(tmp_s)
                break
        else:
            if item.strip():
                res.append(item.strip())
    print(res)
    return "\n".join(res)


def strip_comments_re(words, markers: list):
    for i in markers:
        if words.find(i) != -1:
            li1 = re.findall("\\" + i + '.*', words)
            for j in li1:
                words = words.replace(j, '')
        else:
            continue
    print(repr(words))
    tmp = words.split("\n")
    res = []
    for s in tmp:
        res.append(s.strip())
    print(repr("\n".join(res)))
    return "\n".join(res)


if __name__ == "__main__":
    assert strip_comments("apples, pears # and bananas", ["#"]) == "apples, pears"
    assert strip_comments("bananas !apples", ["!"]) == "bananas"
    assert strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples",
                          ["#", "!"]) == "apples, pears\ngrapes\nbananas"
    assert strip_comments("a #b\nc\nd $e f g", ["#", "$"]) == "a\nc\nd"

    assert strip_comments_re("apples, pears # and bananas", ["#"]) == "apples, pears"
    assert strip_comments_re("bananas !apples", ["!"]) == "bananas"
    assert strip_comments_re("apples, pears # and bananas\ngrapes\nbananas !apples",
                          ["#", "!"]) == "apples, pears\ngrapes\nbananas"
    assert strip_comments_re("a #b\nc\nd $e f g", ["#", "$"]) == "a\nc\nd"
