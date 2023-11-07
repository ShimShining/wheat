# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/7
Describe: 后缀表达式求值
"""
from race.prac.ds.stack_ds.stack import Stack


def postfix_eval(expr):
    """
    后缀表达式求值
    :param expr:
    :return:
    """

    operand_stack = Stack()
    token_list = expr.split(" ")

    for token in token_list:
        if token.isdigit():
            operand_stack.push(int(token))
        else:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = calculate(token, op1, op2)
            operand_stack.push(res)
    return operand_stack.pop()


def calculate(op, op1, op2):
    if op == "*":
        return op1 * op2
    if op == "/":
        return op1 / op2
    if op == "+":
        return op1 + op2
    if op == "-":
        return op1 - op2


if __name__ == '__main__':

    postfix = "14 5 * 8 +"
    print(postfix_eval(postfix))

