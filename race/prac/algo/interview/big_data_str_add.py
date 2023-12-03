# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/8
Describe:腾讯音乐一面题,两个大数相加,只能按位相加,直接使用加法会溢出
'99999999999999999999999999999999999999999999999999' + '9999999999999999999999999999999999999999999999999999999'
"""


def big_data_str_add(add_a, add_b):
    len_a = len(add_a)
    len_b = len(add_b)
    res = []
    carry = 0
    if not len_a and not len_b:
        return None

    while len_a and len_b:
        added = int(add_a[len_a - 1]) + int(add_b[len_b - 1]) + carry
        if added >= 10:
            added %= 10
            carry = 1
        else:
            carry = 0
        len_a -= 1
        len_b -= 1
        res.insert(0, str(added))

    while len_a:
        added = int(add_a[len_a - 1]) + 0 + carry
        if added >= 10:
            added %= 10
            carry = 1
        else:
            carry = 0
        len_a -= 1
        res.insert(0, str(added))

    while len_b:
        added = int(add_a[len_b - 1]) + 0 + carry
        if added >= 10:
            added %= 10
            carry = 1
        else:
            carry = 0
        len_b -= 1
        res.insert(0, str(added))

    if carry:
        res.insert(0, str(carry))

    return "".join(res)


if __name__ == "__main__":

    stra = '99999999999999999999999999999999999999999999999999'
    strb = '9999999999999999999999999999999999999999999999999999999999'
    res = big_data_str_add(stra, strb)
    print(res)
    assert str(10000000099999999999999999999999999999999999999999999999998) == res
