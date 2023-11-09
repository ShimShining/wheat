# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/9
Describe: turtle画图
爬行: forward(n);backward(n)
转向: left(a); right(a)
抬笔放笔:penup(),pendown()
笔属性: pensize(s); pencolor(c)
"""
import turtle

t = turtle.Turtle()
#
# t.forward(100)

# for i in range(4):
#     t.forward(100)
#     t.right(90)
# t.pencolor('red')
# t.pensize(3)
# for i in range(5):
#     t.forward(100)
#     t.right(144)
# t.hideturtle()
#
# turtle.done()


def draw_spiral(t, line_len):
    if line_len > 0:
        t.forward(line_len)
        t.right(90)
        draw_spiral(t, line_len - 5)


def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)  # 退回到原地


if __name__ == '__main__':

    # draw_spiral(t, 100)
    t.left(90)
    t.penup()
    t.backward(100)
    t.pendown()
    t.pencolor("green")
    t.pensize(2)
    tree(100)
    t.hideturtle()
    turtle.done()

