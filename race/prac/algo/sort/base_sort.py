# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2021/9/30
Describe: 排序基类
"""
from abc import ABCMeta, abstractmethod


class BaseSort:

    def __init__(self, nums):

        self.nums = nums

    def sort(self):
        pass
