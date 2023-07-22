#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2020-01-07
Describe:find a longest substring of a string
"""


class LongestSubstring:

    def find_longest_substring(self, s):
        """
        通过,性能较差
        执行用时 :1368 ms, 在所有 Python3 提交中击败了5.03%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了12.41%的用户
        maxLength = max(maxLength,len(temp)) 去替代if 判断 内存消耗更大?
        :param s:
        :return:
        """

        if s == '':
            return 0,1
        elif len(s) == 1:
            return 1,1

        maxLength = 0
        count = 0
        for i in range(len(s)-1):
            temp = set()
            temp.add(s[i])
            for j in range(i+1,len(s)):
                if s[j] in temp:
                    if maxLength < len(temp):
                        maxLength = len(temp)
                    break
                temp.add(s[j])
                if len(temp) == j-i+1:
                    count += 1
                    if maxLength < len(temp):
                        maxLength = len(temp)
                else:
                    count += 1
                    if maxLength < len(temp):
                        maxLength = len(temp)
                    continue

        return maxLength, count

    def lengthOfLongestSubstring(self,s):
        """
        大佬的代码
        :param s:
        :return:
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans,0




if __name__ == "__main__":

    s1 = 'abc'
    s2 = 'aaaa'
    s3 = ''
    s4 = 'abcdabcbb'
    s5 = 'd'
    s6 = "abcdefghabcdefgabcdeabcdabc"
    s7 = "pwwkew"
    s8 = "abcabcbb"
    s9 = "ckilbkd"
    # strData = [s1,s2,s3,s4,s5,s6]
    strData = [s8]
    findLongestSubstring = LongestSubstring()

    for data in strData:
        # times,count = findLongestSubstring.find_longest_substring(data)
        times,count = findLongestSubstring.lengthOfLongestSubstring(data)
        print("{} 字符串的最大子字符串长度为:{},计算次数为{}.".format(data,times,count))
