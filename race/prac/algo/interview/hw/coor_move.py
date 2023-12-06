# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/12/6
Describe: HJ17 坐标移动
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：
起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)
结果 （10， -10）
"""


def coor_move(ins):
    s = ins.split(";")
    d = {
        "A": (-1, 0),    # (-1, 0)  负方向移动,移动的索引是0
        "D": (1, 0),
        "W": (1, 1),
        "S": (-1, 1)
    }
    origin = [0, 0]
    for c in s:
        if not c or len(c) < 2 or c[0] not in "ADWS" or not c[1:].isdigit():
            continue
        else:
            index = d[c[0]][1]
            origin[index] += (d[c[0]][0] * int(c[1:]))
    return tuple(origin)


if __name__ == '__main__':
    s = "A10;S20;W10;D30;X;A1A;B10A11;;A10;"
    print(coor_move(s))

