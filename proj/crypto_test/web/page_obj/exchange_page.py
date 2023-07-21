# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/12
Describe:exchange page PO
"""
from selenium.webdriver.common.by import By
from web.page_obj.base_page import BasePage
import allure


class ExchangePage(BasePage):

    __CRO_btn = (By.XPATH, "//*[@class='e-tabs']//*[contains(@class,'e-tabs__nav-item')][last()]")
    __CRO_USDC_trade = (By.XPATH, "//*[contains(text(),'/USDC')]/../../../../..//*[contains(text(),'Trade')]")
    __bottom_copyright = (By.XPATH, "//*[contains(text(),'Copyright© ')]")

    def goto_trade_page(self):

        self.wait_for_visible(self.__CRO_btn)
        self.save_screenshot("首页")
        self.find(self.__CRO_btn).click()
        self.logger.info("进入CRO子tab成功")
        self.save_screenshot("CRO_TAB")
        self.scroll_to_element_div(self.__bottom_copyright)
        # self.scroll_to_bottom()
        # self.scroll(self.__CRO_USDC_trade, 0, 10000)
        self.scroll_by(0, 10000)
        self.wait_for_visible(self.__CRO_USDC_trade)

        self.save_screenshot("CRO_USDC")
        # self.find(self.__CRO_USDC_trade).click()
        self.js_click(self.__CRO_USDC_trade)
        self.logger.info("点击trade按钮成功")
        from web.page_obj.trade_page import TradePage
        return TradePage(self.driver)



