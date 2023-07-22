# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/3
Describe:翻转单词顺序
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串"I am a student. “，则输出"student. a am I”。

输入: "the sky is blue"
输出: "blue is sky the"

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
"""


class Solution:

    def reverse_words(self, s: str):
        """
        25 / 25 个通过测试用例
        状态：通过
        执行用时: 20 ms
        内存消耗: 14.2 MB
        :param s:
        :return:
        """
        s = s.strip()
        temp = s.split(" ")
        res = " ".join(temp[::-1])
        return res
        # return " ".join(s.split()[::-1])

    def reverse_words_oth(self, s: str):
        """
        25 / 25 个通过测试用例
        状态：通过
        执行用时: 28 ms
        内存消耗: 14.1 MB
        :param s:
        :return:
        """

        s = s.strip()
        l, r ,res = len(s) - 1, len(s) - 1, []

        while l >= 0:

            while l >=0 and s[l] != " ": l -= 1
            res.append(s[l+1: r+1])
            while s[l] == " ": l -= 1
            r = l

        return " ".join(res)


if __name__ == "__main__":

    temp_str = ["the sky is blue", "  hello world!  "]
    expect = ["blue is sky the", "world! hello"]
    sol = Solution()
    for i, s in enumerate(temp_str):
        res = sol.reverse_words_oth(s)
        print(f"res = {res}")
        assert res == expect[i]
    print("pass")

