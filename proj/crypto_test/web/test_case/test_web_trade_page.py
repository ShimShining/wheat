# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/12
Describe:
"""
from web.page_obj.exchange_page import ExchangePage
import allure


@allure.feature("交易功能页面")
class TestWebTradePage:

    def setup(self):

        self.ex_page = ExchangePage()

    def teardown(self):

        self.ex_page.clear_env()

    @allure.story("交易页面进入")
    def test_enter_trade_page_success(self):

        order_book = self.ex_page.goto_trade_page().get_order_book()
        assert order_book is not None

