# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/22
Describe: 中缀表达式,建立表达式解析树
"""
import operator

from race.prac.ds.stack_ds.stack import Stack
from race.prac.ds.tree.binary_tree_linklist import BinaryTree


def build_parse_tree(expr: str):
    fp_list = expr.split()
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for s in fp_list:
        if s == '(':
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif s not in ["+", "-", "*", "/", ")"]:
            current_tree.set_root_val(int(s))
            parent = p_stack.pop()
            current_tree = parent
        elif s in ["+", "-", "*", "/"]:
            current_tree.set_root_val(s)
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif s == ")":
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree


def evaluate(parse_tree):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    left_tree = parse_tree.get_left_child()
    right_tree = parse_tree.get_right_child()

    if left_tree and right_tree:
        fn = ops[parse_tree.get_root_val()]
        return fn(evaluate(left_tree), evaluate(right_tree))
    else:
        return parse_tree.get_root_val()


if __name__ == '__main__':
    expr = "( ( 3 + 4 ) * ( 5 + 6 ) )"

    p_tree = build_parse_tree(expr)
    # print(p_tree)
    # print(p_tree.get_left_child().get_left_child().get_left_child().get_root_val())
    #
    s = evaluate(p_tree)
    print(s)


