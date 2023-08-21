# -*- coding: utf-8 -*-
"""
@Author: shining
@File: bud_exception.py
@Date: 2022/10/10 4:58 下午
@Version: python 3.9
@Describe: 自定义异常类
ValueEmptyError
ValuesEmptyError
ValueNotEmptyError
ResultIsNotZeroError
LengthLTZeroError
NotContainValueError
ContainInvalidValueError
ActualNEExpectedError
"""


class BPException(Exception):

    pass


class ValueEmptyError(BPException):

    pass


class ValuesEmptyError(BPException):

    pass


class ValueNotEmptyError(BPException):
    pass


class ResultIsNotZeroError(BPException):
    pass


class LengthLTZeroError(BPException):

    pass


class NotContainValueError(BPException):
    pass


class ContainInvalidValueError(BPException):

    pass


class ActualNEExpectedError(BPException):

    pass


class ValueIsNoneError(BPException):

    pass


class ActualEQExpectedError(BPException):

    pass


class ServerRSPError(BPException):

    pass
