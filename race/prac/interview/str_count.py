# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/9
Describe:迅雷网络-高级测试工程师
编程：输入字符串，要求统计字母相邻重复次数，输出格式：a-次数-b-次数。

如输入：awww
输出：a-1-w-3
"""


def str_count(s):

    s_cur = ''
    count = 0
    res = ''
    length = len(s)
    if length == 0:
        return ''
    i = 0
    while i < length:
        s_cur = s[i]
        for j in range(i, length):
            if s[j] == s_cur:
                count += 1
            else:
                res += (s_cur + '-' + str(count) + '-')
                # s_cur = s[j]
                i = i + count
                count = 0
                break
        else:
            res += (s_cur + '-' + str(count))
            break

    return res


if __name__ == "__main__":
    temp_list = ["awww", '', 'a', 'aaaaaaaaaaaaa', 'ababababa', 'aaaabbbbbbbbbbbbbbcccccccccaaaaaaeec',
                 '###hjdfhsasgfksdh']
    for temp in temp_list:
        res = str_count(temp)
        print(res)
