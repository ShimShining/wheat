# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
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


class BUDException(Exception):

    pass


class ValueEmptyError(BUDException):

    pass


class ValuesEmptyError(BUDException):

    pass


class ValueNotEmptyError(BUDException):
    pass


class ResultIsNotZeroError(BUDException):
    pass


class LengthLTZeroError(BUDException):

    pass


class NotContainValueError(BUDException):
    pass


class ContainInvalidValueError(BUDException):

    pass


class ActualNEExpectedError(BUDException):

    pass


class ValueIsNoneError(BUDException):

    pass


class ActualEQExpectedError(BUDException):

    pass


class ServerRSPError(BUDException):

    pass
