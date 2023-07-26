# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: base_test.py
@Date: 2021/11/15 8:17 下午
@Version: python 3.10
@Describle: 测试基类封装
"""
import allure
from base.base_api import logger, log_api_cost
from hamcrest import *
from base.bud_exception import *
from utils.fake import Fake
from utils.read_config import *


class BaseTest:
    log = logger
    fake = Fake()

    # todo 封装所有的assertThat方法
    def assert_equal(self, actual, expect):

        self.log.info(f"实际值={actual},期望值={expect}")
        try:
            assert_that(actual, equal_to(expect))
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f"捕获异常ActualNEExpectedError: 实际值={actual} !===! 期望值={expect}")
            raise ActualNEExpectedError(f"实际值={actual} !===! 期望值={expect}")
        else:
            # assert isinstance(self.log.info, object)
            self.log.info(f"{actual} == {expect}")

    def assert_engine_api_code_success(self, r):
        """
        联机接口返回成功码断言
        err_code = 0 and err_msg = "ok"
        :param r:
        :return:
        """

        self.assert_equal(r["err_code"], 0)
        self.assert_equal(r["err_msg"], "ok")


if __name__ == '__main__':
    b = BaseTest()
    b.assert_equal(1, 2)
