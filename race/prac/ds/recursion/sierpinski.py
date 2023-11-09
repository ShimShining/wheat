# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/9
Describe: 谢尔宾斯基三角形
"""
import turtle


t = turtle.Turtle()


def sierpinski(degree, points):

    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'orange']
    draw_triangle(points, color_map[degree])
    if degree > 0:
        sierpinski(degree-1,
                   {'left': points['left'], 'top':get_mid(points['left'], points['top']),
                    'right': get_mid(points['left'], points['right'])})
        sierpinski(degree - 1,
                   {'left': get_mid(points['left'], points['top']), 'top': points['top'],
                    'right': get_mid(points['right'], points['top'])})
        sierpinski(degree -1,
                   {
                       'left': get_mid(points['left'], points['right']),
                       "top":  get_mid(points['top'], points['right']),
                       "right": points['right']
                   })


def draw_triangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()


def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


if __name__ == '__main__':

    points = {
        "left": (-200, -100),
        "top": (0, 200),
        "right": (200, -100)
    }
    sierpinski(5, points)

    turtle.done()

