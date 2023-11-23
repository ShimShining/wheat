# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/6
Describe: practice
"""
from race.prac.ds.queue_ds.queue_ds import Queue


x = list(range(1000000))


def tst_add():
    l = []
    for i in range(1000):
        l = l + [i]


def tst_append():
    l = []
    for i in range(1000):
        l.append(i)


def tst_list_comprehension():
    l = [i for i in range(1000)]


def tst_list_function():
    l = list(range(1000))


def anagram_sol1(s1, s2):
    """
    逐个比较
    1. s2 存到一个列表
    2. 遍历s1的每个字符
    3. 与s2的列表进行遍历比较
        3.1 找到 列表值置为None
        3.2 没找到 跳出循环
    :param s1:
    :param s2:
    :return:
    """


def anagram_sol2(s1, s2):
    """
    1. 将s1和s2 转换成列表
    2. 对s1和s2进行排序
    3. 遍历对比相同位置是否相等  \\ 比较两个列表是否相等
    :param s1:
    :param s2:
    :return:
    """


def anagram_sol3(s1, s2):
    """
    计数比较
    使用计数器计算两个字符串中每个字母的个数
    再遍历进行比较
    :param s1:
    :param s2:
    :return:
    """

    # count_a = {}
    # count_b = {}
    # for item in s1:
    #     if item in count_a.keys():
    #         count_a[item] += 1
    #     else:
    #         count_a[item] = 1
    #
    # for item in s2:
    #     if item in count_b.keys():
    #         count_b[item] += 1
    #     else:
    #         count_b[item] = 1
    #
    # matches = True
    #k not in count_b.keys() O(N) k not in count_b O(1)
    # for k, v in count_a.items():
    #     if k not in count_b.keys() or count_a[k] != count_b[k]:  # if k not in count_b or count_a[k] != count_b[k]:
    #         matches = False
    #         break


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
    from race.prac.ds.stack_ds.stack import Stack


def pars_checker(symbols):
    """
    跟单括号匹配类似
    1. 做括号之一,入栈
    右括号.进行与顶部比较
    :param symbols:
    :return:
    """
    from race.prac.ds.stack_ds.stack import Stack


def divide_by_n(dec_num, base=2):

    from race.prac.ds.stack_ds.stack import Stack


def infix_to_postfix(infix_expr):
    """
    expr变为list
    遍历token
    数字字母直接加入后缀表达式中
    左括号入栈
    右括号,在栈中弹出左括号之前的操作符,遇到左括号为止
    操作符,比较优先级,优先级高弹出栈内的
    :param infix_expr:
    :return:
    """
    from race.prac.ds.stack_ds.stack import Stack
    p = dict()
    p["*"] = 3
    p["/"] = 3
    p["+"] = 2
    p["-"] = 2
    p["("] = 1

    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token.isalpha() or token.isdigit():
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_op = op_stack.pop()
            while top_op != "(":
                postfix_list.append(top_op)
                top_op = op_stack.pop()
        else:
            while not op_stack.is_empty() and p[op_stack.peek()] >= p[token]:
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


def postfix_eval(expr):
    """
    后缀表达式求值
    :param expr:
    :return:
    """
    from race.prac.ds.stack_ds.stack import Stack
    s = Stack()
    token_list = expr.split()
    for token in token_list:
        if token.isdigit():
            s.push(int(token))
        else:
            op2 = s.pop()
            op1 = s.pop()
            res = cal(token, op1, op2)
            s.push(res)
    return s.pop()


def cal(op, op1, op2):

    if op == "*":
        return op1 * op2
    if op == "/;":
        return op1 / op2
    if op == "+":
        return op1 + op2
    if op == "-":
        return op1 - op2


def hot_potato(name_list, num):
    """
    约瑟夫问题
    :param name_list:
    :param num:
    :return:
    """
    q = Queue()
    for name in name_list:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num-1):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()


def bubble_sort(nums: list):
    """冒泡"""


def selection_sort(nums: list):
    """选择"""



def insertion_sort(nums):
    """插入"""


class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, key):
        self.heap_list.append(key)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_up(self, i):
        """
        插入节点上浮
        :param i:
        :return:
        """
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
            i = i // 2

    def del_min(self):
        """
        删除最小节点, 并返回最小值
        :return:
        """
        root_min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return root_min_val

    def perc_down(self, i):
        """
        下沉
        :param i:
        :return:
        """
        while i * 2 <= self.current_size:
            mc_child = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc_child]:
                self.heap_list[i], self.heap_list[mc_child] = self.heap_list[mc_child], self.heap_list[i]
            i = mc_child

    def min_child(self, i):
        """
        返回最下子树的index
        :param i:
        :return:
        """
        if i * 2 + 1 > self.heap_list or self.heap_list[i * 2] < self.heap_list[i*2+1]:
            return i * 2
        return i * 2 + 1

    def build_heap(self, nums):
        """
        insert建堆 时间复杂度是nlogn
        下沉法建堆 时间复杂度是n
        :param nums:
        :return:
        """
        i = len(nums) // 2
        self.heap_list = [0] + nums[:]
        self.current_size = len(nums)
        while i > 0:
            self.perc_down(i)
            i = i - 1


if __name__ == '__main__':

    from timeit import Timer, timeit
    # t1 = Timer("tst_add()", "from __main__ import tst_add")
    # print(f"concat {t1.timeit(number=1000)} seconds")
    #
    # t2 = Timer("tst_append()", "from __main__ import tst_append")
    # print(f"append {t2.timeit(number=1000)} seconds")
    #
    # t3 = Timer("tst_list_comprehension()", "from __main__ import tst_list_comprehension")
    # print(f"list comprehension {t3.timeit(number=1000)} seconds")
    #
    # t4 = Timer("tst_list_function()", "from __main__ import tst_list_function")
    # print(f"list function {t4.timeit(number=1000)} seconds")
    #
    # popzero = Timer("x.pop(0)", "from __main__ import x")
    # popend = Timer("x.pop()", "from __main__ import x")
    # print(f"popzero={popzero.timeit(number=1000)}; popend={popend.timeit(number=1000)}")

    a = 'abcd'
    b = 'cadb'
    c = 'abcdfgd'
    d = 'casdgdb'
    print(f"{a}和{b}是否变位词: {anagram_sol3(a, b)}")
    print(f"{c}和{d}是否变位词: {anagram_sol3(c, d)}")

    print(par_checker('((()))'))
    print(par_checker("(()"))

    print(pars_checker('{{([][])}()}'))
    print(pars_checker("[{()]"))

    print(divide_by_n(988, 2))

    expr = "14 + 5 * 8 - 9"
    r= infix_to_postfix(expr)
    print(r)

    s = postfix_eval(r)
    print(s)

    names = list(range(40))
    live = hot_potato(names, 7)
    print(live)

    tmp_list = [1, 0, 9, 34, 5, 12, 7, 9, 8, 1, 0, 13, 33]
    tmp_list2 = [1, 2, 1, 3, 4, 5, 6]
    # bubble_sort(tmp_list)
    # bubble_sort(tmp_list2)
    # selection_sort(tmp_list)
    # selection_sort(tmp_list2)
    insertion_sort(tmp_list)
    insertion_sort(tmp_list2)
    print(f"tmp_list sorted = {tmp_list}")
    print(f"tmp_list2 sorted = {tmp_list2}")
