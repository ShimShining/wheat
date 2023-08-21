# -*- coding: utf-8 -*-
"""
@Author: shining
@File: base_api_test.py
@Date: 2021/12/25 8:57 下午
@Version: python 3.10
@Describe: api 自动化测试基类
"""
from proj.BPServiceTest.base.base_test import BaseTest
import pytest
from proj.BPServiceTest.base.bp_exception import *


# todo 封装一层Exception，重新定义AssertError


class BaseApiTest(BaseTest):

    def assert_response_json(self):
        """
        todo 通过json schema 进行校验接口返回
        :return:
        """

    def assert_data_not_empty(self, r):

        data = r['data']
        try:
            assert data
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f" ValueEmptyError: api返回体data字段为空，r['data'] = {data}")
            raise ValueEmptyError()

    def assert_not_empty(self, r: object, **kwargs) -> object:

        msg = kwargs.get('msg', None)
        try:
            assert r
        except AssertionError as e:
            err_info = f" ValueEmptyError: 字段实际返回值为空，value=[{r}]"
            if msg:
                err_info = f" ValueEmptyError: 字段[{msg}]实际返回值为空，value=[{r}]"
            self.log.error(e)
            self.log.error(err_info)
            raise ValueEmptyError(err_info)

    def assert_not_none(self, r):

        try:
            assert r is not None
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f" ValueIsNoneError: 字段实际返回值为None(Null), value={r}")
            raise ValueIsNoneError(f" ValueIsNoneError: 字段实际返回值为None(Null), value={r}")

    def assert_value_in(self, value, seq):

        try:
            assert value in seq
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f" NotContainValueError: {value}不包含在序列{seq}!!!")
            raise NotContainValueError(f" NotContainValueError: {value}不包含在序列{seq}!!!")

    def assert_value_not_in_seq(self, val, seq):

        try:
            assert val not in seq
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f" ContainInvalidValueError: {val}不应该包含在序列{seq}!!!")
            raise ContainInvalidValueError(f" ContainInvalidValueError: {val}不应该包含在序列{seq}!!!")

    def assert_not_value(self, r, seq):

        self.assert_value_not_in_seq(r, seq)

    def assert_any_not_empty(self, seq: list):

        flag = False
        for s in seq:
            if s:
                flag = True
        try:
            assert flag
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f" ValuesEmptyError: seq中所有的值都为空，seq={seq}")
            raise ValuesEmptyError(f" ValuesEmptyError: seq中所有的值都为空，seq={seq}")

    def assert_rsp_json(self, map_info: dict):
        """
        校验UGC发布后应该返回对应的json（map_json,props_json,clothes_json, space_json）
        :param map_info:
        :return:
        """
        # [map_info['mapJson'], map_info['propsJson'], map_info['clothesJson'], map_info['clothesUrl']]
        map_json = map_info.get("mapJson", None)
        props_json = map_info.get("propsJson", None)
        clothes_json = map_info.get("clothesJson", None)
        clothes_url = map_info.get("clothesUrl", None)
        self.assert_any_not_empty([map_json, props_json, clothes_json, clothes_url])

    def assert_not_equal(self, actual, expected):

        try:
            assert actual != expected
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f" ActualEQExpectedError: actual={actual}预期不应该等于expected={expected}")
            raise ActualEQExpectedError(f" ActualEQExpectedError: actual={actual}预期不应该等于expected={expected}")

    def assert_any_not_equal(self, seq):
        """
        seq中的二维数组任意一组不相等，通过校验
        :param seq:
        :return:
        """
        flag = False
        for item in seq:
            actual, expected = item
            if actual != expected:
                flag = True
                break
        try:
            assert flag
        except AssertionError as e:
            self.log.error(e)
            err = f" ActualEQExpectedError: seq={seq}中的每一组数据都相等，不符合预期！！！"
            self.log.error(err)
            raise ActualEQExpectedError(err)
