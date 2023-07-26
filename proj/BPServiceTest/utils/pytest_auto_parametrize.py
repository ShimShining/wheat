# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: pytest_auto_parametrize.py
@Date: 2021/11/21 4:45 下午
@Version: python 3.10
@Describle:
"""
import inspect
import pytest
from _pytest.mark import ParameterSet

__version__ = '0.1.0'


def auto_parametrize(argvalues, *args, **kwargs):
    """
    pytest框架参数化时，重复编写参数优化
    :param argvalues:
    :param args:
    :param kwargs:
    :return:
    """
    def decorator(func):
        try:
            argvalue = argvalues[0]
        except IndexError:
            raise ValueError("argvalues must be not empty")
        except TypeError:
            raise TypeError("argvalues must be a sequence")
        argvalue = ParameterSet.extract_from(argvalue).values
        argspec = inspect.getfullargspec(func)[0]
        if "self" in argspec:
            argspec.remove("self")
        argnames = argspec[:len(argvalue)] if isinstance(argvalue, (list, tuple)) else argspec[0]
        return pytest.mark.parametrize(argnames, argvalues, *args, **kwargs)(func)
    return decorator


def pytest_namespace():
    """
    注册装饰器auto_parametrize到pytest的plugin中
    :return:
    """
    return {'auto_parametrize': auto_parametrize}
