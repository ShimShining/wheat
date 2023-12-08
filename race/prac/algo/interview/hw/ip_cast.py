# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/8
Describe: HJ33 整数与IP地址间的转换
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

输入
1 输入IP地址
2 输入10进制型的IP地址
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址

输入：
10.0.3.193
167969729
输出：
167773121
10.3.3.193
"""


def cast_ip(ip):
    res = None
    if type(ip) == str:
        res = ip_to_int(ip)
    elif type(ip) == int:
        res = int_to_ip(ip)
    return res


def ip_to_int(ip):
    res = "0b"
    ip_list = ip.split(".")
    for i in ip_list:
        b = bin(int(i))
        if len(b) < 10:
            s = (10 - len(b)) * "0" + b[2:]
            res += s
        else:
            res += b[2:]
    return int(res, 2)


def int_to_ip(n):
    bin_s = bin(n)
    s = bin_s[2:]
    n = len(s)
    if n < 32:
        s = (32 - n) * "0" + s
    res = []
    i = 0
    while i > -n:
        pre = '0b'
        tmp = s[i - 8:][:8]
        num = int(pre + tmp, 2)
        res.insert(0, str(num))
        i -= 8
    print(res)
    return ".".join(res)


if __name__ == '__main__':
    ip = "10.0.3.193"
    n = 167969729
    # print(ip_to_int(ip))
    print(int_to_ip(n))
