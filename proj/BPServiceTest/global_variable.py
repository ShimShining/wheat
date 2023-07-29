# -*- coding: utf-8 -*-
"""
@Author: shining
@File: us_global_variable.py
@Date: 2022/5/1 11:16 下午
@Version: python 3.8
@Describe: 全局变量存放位置,可设置和获取
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
        print(f'INFO: 使用全局变量中key={key},值={val}')
        return val
    except KeyError:
        # print(f'INFO: 全局变量中没有查找到key={key}的全局变量值')
        return False
