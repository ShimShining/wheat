# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/8
Describe: 字母大小写全排列
https://leetcode-cn.com/problems/letter-case-permutation/
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]

来源：力扣（LeetCode）
难度:中等
"""


class Solution:

    def letter_case_permutation(self, S):

        """
        DFS 回溯 看到题目要求组合或者集合，马上想到可以用回溯法：回溯法本来是说对于每个元素都先考虑放它的情况，再考虑不放它的情况；放在这道题的背景里就是，对于每个字母，先考虑放它，再考虑放它的另一种大小写形式。
        用dfs实现回溯，start代表目前从扫描到第几位，
        如果是digit，就直接加进去，然后下一层递归

        如果是alpha，就先加进去，然后下一层递归；再加对立大小写形式， 然后下一层递归。
        :param S:
        :return:
        """
        res = list()
        l = len(S)
        if l == 0:
            return [""]

        def dfs(start, temp):
            if start >= l or len(temp) == l:  # 已经找到了一个答案
                res.append(temp)
                return
            # print(start, temp)
            if S[start].isdigit():  # 数字就直接加
                dfs(start + 1, temp + S[start])

            elif S[start].islower():  # 字母就加本身和对立面
                dfs(start + 1, temp + S[start])
                dfs(start + 1, temp + S[start].upper())

            elif S[start].isupper():
                dfs(start + 1, temp + S[start])
                dfs(start + 1, temp + S[start].lower())

        dfs(0, "")
        return res

    def letter_case_permutation_bfs(self, S):
        """
        除了用DFS回溯实现，我们也可以用BFS来解题， 线性扫描S，
        对于扫描到的每个元素， 都把它的大小写形式分别加到，目前的res里的所有结果里，这样可以得到temp，

        然后用temp覆盖res。

        比如对于S = "a1b2"，

        扫描到a时， res = [a, A]

        扫描到b时， res = [a1, A1], temp = [a1b, a1B, A1b, A1B]
        :param S:
        :return:
        """
        import copy
        res = [""]

        for i, x in enumerate(S):
            # if len(res) == 0:
            #     res.append(x)
            if x.isdigit():  # 数字就每个答案都加进去
                for index, item in enumerate(res):
                    res[index] += (x)
            elif x.isupper():  # 字母就每个答案先放自己再放对立面
                temp = list()
                for index, item in enumerate(res):
                    # print item
                    temp.append(item + (x))
                    temp.append(item + (x.lower()))
                res = copy.deepcopy(temp[:])
            elif x.islower():
                temp = list()
                for index, item in enumerate(res):
                    temp.append(item + (x))
                    temp.append(item + (x.upper()))
                res = copy.deepcopy(temp[:])
        return res

    def letter_case_permutation_bitmap(self, S):
        """
        Bitmap法，字符串S的长度为l， 则总共会有 2** l种结果，换成二进制就是0 ~ 2 **l - 1个数，
        对于每个数，如果某个位上是0， 就放小写；是1， 就放大写
        :param S:
        :return:
        """
        l = len(S)
        n = 2 ** l
        res = list()
        if l == 0:
            res.append("")
        for i in range(0, n):  # 得到0 ~ 2 ** l 的每个数
            temp = ""

            for j in range(0, l):
                if ((2 ** j) & i) == 0:  # 当前位是0， 放小写
                    temp += S[j].lower()
                else:  # 放大写
                    temp += S[j].upper()
            if temp not in res:
                res.append(temp)
        return res


if __name__ == "__main__":

    tmp = ["a1b2", "3z4", "12345"]
    sol = Solution()
    for s in tmp:
        res = sol.letter_case_permutation(s)
        print(res)

        res = sol.letter_case_permutation_bfs(s)
        print(res)
        res = sol.letter_case_permutation_bitmap(s)
        print(res)
