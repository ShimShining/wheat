# -*- coding: utf-8 -*-
"""
@Author: shining
@File: decorator.py
@Date: 2021/11/18 8:51 下午
@Version: python 3.10
@Describle:
"""
import inspect
from functools import wraps
import pytest
from _pytest.mark import ParameterSet


def yaml_load(func, args):
    @wraps(func)
    def wrapper(func, args):
        pass
    return wrapper()


