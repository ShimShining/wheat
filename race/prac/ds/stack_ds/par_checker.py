# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/6
Describe: 栈应用之括号匹配
"""
from race.prac.ds.stack_ds.stack import Stack


def par_checker(symbol_str):
    """
    遍历字符串
    左括号入栈
    右括号
        匹配,弹出栈顶左括号
        不匹配,返回False
    判断匹配标志和栈是否为空
        匹配且栈为空, 则匹配
        否则,不匹配
    :param symbol_str:
    :return:
    """
    matches = True
    s = Stack()
    index = 0
    while index < len(symbol_str) and matches:
        if symbol_str[index] == "(":
            s.push(symbol_str[index])
        else:
            if s.is_empty():
                matches = False
            else:
                s.pop()
        index += 1

    if matches and s.is_empty():
        return True
    else:
        return False


def pars_checker(symbols):
    """
    跟单括号匹配类似
    1. 做括号之一,入栈
    右括号.进行与顶部比较
    :param symbols:
    :return:
    """
    s = Stack()
    index = 0
    matches = True
    while index < len(symbols) and matches:
        if symbols[index] in "([{":
            s.push(symbols[index])
        else:
            if s.is_empty():
                matches = False
            else:
                top = s.pop()
                if not par_match(top, symbols[index]):
                    matches = False
        index += 1

    if matches and s.is_empty():
        return True
    return False


def par_match(lf, rt):
    opens = "([{"
    closers = ")]}"
    return opens.index(lf) == closers.index(rt)


if __name__ == '__main__':
    print(par_checker('((()))'))
    print(par_checker("(()"))

    print(pars_checker('{{([][])}()}'))
    print(pars_checker("[{()]"))

