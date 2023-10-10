# -*- coding: utf-8 -*-
"""
@Author: shining
@File: app_global_variable.py
@Date: 2022/5/25 6:18 下午
@Version: python 3.9
@Describe:全局变量存储
"""


def _init():
    """
    模块初始化
    :return:
    """
    global GLOBAL_DICT
    GLOBAL_DICT = {}


def _set(key, value):

    try:
        GLOBAL_DICT[key] = value
    except KeyError:
        return False


def _get(key):
    try:
        val = GLOBAL_DICT[key]
        print(f"==> 使用全局变量key={key}, value={val}")
        return val
    except KeyError:
        return False

