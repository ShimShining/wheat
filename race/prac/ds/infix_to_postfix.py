# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/7
Describe: 算术表达式: 中缀表达式转后缀表达式
"""
from race.prac.ds.stack_ds.stack import Stack


def infix_to_postfix(infix_expr):
    """

    :param infix_expr:
    :return:
    """

    prec = dict()
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = list(infix_expr)
    for token in token_list:
        if token.isdigit() or token.isalpha():
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while not op_stack.is_empty() and prec[op_stack.peek()] >= prec[token]:
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)


if __name__ == '__main__':

    expr = "A*B*C"
    print(infix_to_postfix(expr))

