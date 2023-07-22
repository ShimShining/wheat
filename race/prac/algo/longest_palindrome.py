#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:20-03-17
Describe:给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""

class Solution:

    def longestPalindrome(self,s):
        """
        输入数据为aacdefcaa时存在缺陷
        :param s:
        :return:
        """

        if not s: return ''
        lengthStr = len(s)
        temp = s[::-1]
        print(temp)
        i = 0
        j = lengthStr
        res = ''
        while i <= lengthStr-1:
            j = i+1
            while j <= lengthStr:
                print("s[i:j]:{}".format(s[i:j]))
                # print("s[j:i]:{}".format(temp[i:j]))
                if s[i:j] in temp and s[i:j] != '':
                    if len(s[i:j]) > len(res):
                        res = s[i:j]
                        print(res)
                    j += 1
                else:
                    break
            i += 1
        return res

    def longestPalindromeOptA(self,s):
        """
        时间超过限制
        :param s:
        :return:
        """

        if not s:return ''
        lengthStr = len(s)
        i = 0
        res = ''
        while i <= lengthStr -1:
            j = i + 1
            temp = ''
            while j < lengthStr:
                # if s[j] == s[j-1]:
                #     if len(res) <= len(temp):
                #         res = s[i:j]
                temp = s[i:j]
                # print(s[i:j],temp[::-1])
                if s[i:j] == temp[::-1]:
                    if len(res) < len(temp):
                        res = s[i:j]
                    j += 1
                else:
                    j += 1
                    continue
            i += 1
        return res



if __name__ == "__main__":

    solution = Solution()
    s = "babad"
    s1 = "abcd"
    s2 = 'abb'
    s3 = "aacdefcaa"
    print(s[5:-1:-1])
    print(solution.longestPalindromeOptA(s2))