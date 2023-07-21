# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/12
Describe:trade page PO
"""
from selenium.webdriver.common.by import By

from web.page_obj.base_page import BasePage


class TradePage(BasePage):

    __order_book = (By.CSS_SELECTOR, ".order-book")
    __charts = (By.CSS_SELECTOR, ".chart-markup-table")

    def get_order_book(self):

        order_book = self.find(self.__order_book)
        self.logger.info(f"定位order-book={order_book}")
        self.save_screenshot("交易界面")
        return order_book
