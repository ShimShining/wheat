# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/13
Describe:侧边菜单栏页面
"""
from appium.webdriver.common.mobileby import MobileBy

from app.app_page_obj.base_app_page import BaseAppPage
from app.app_page_obj.forecast_page import ForecastPage


class MenuPage(BaseAppPage):

    __forecast = (MobileBy.XPATH,
                  "//*[@resource-id='hko.MyObservatory_v1_0:id/left_drawer']"
                  "//*[contains(@text,'9-Day') or contains(@text,'九天預報')]")
    __forecast_text_en = '9-Day Forecast'
    __forecast_text_cns = '九天预报'
    __forecast_text_cnt = '九天預報'

    # TODO 多语言的支持
    def goto_forecast_page(self):

        self.swipe_find(self.__forecast_text_cnt)
        self.find(self.__forecast).click()
        return ForecastPage(self.driver)

