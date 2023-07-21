# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/13
Describe:天气预测界面
"""
from appium.webdriver.common.mobileby import MobileBy

from app.app_page_obj.base_app_page import BaseAppPage


class ForecastPage(BaseAppPage):

    __title = (MobileBy.XPATH, "//*[contains(@text,'Weather Forecast')]")
    __tab_title = (MobileBy.ACCESSIBILITY_ID, "9-Day Forecast")
    __title_cnt = (MobileBy.XPATH, "//*[contains(@text,'天氣預報')]")

    __tab_title_cnt = (MobileBy.ACCESSIBILITY_ID, "九天預報")
    __9day = (MobileBy.XPATH,
              "//*[@class='android.widget.ListView']//*[@class='android.widget.LinearLayout']")

    def check_elem_exist(self):

        self.find(self.__title_cnt)
        self.find(self.__tab_title_cnt)
        self.log.info("进入九天预报界面成功.")

    def get_nine_list(self):

        res = []
        self.wait_for_visible(self.__9day)
        elems = self.finds(self.__9day)
        for elem in elems:
            desc = elem.get_attribute("content-desc")
            if desc not in res and desc is not None:
                res.append(desc)
        self.log.info(f"获取的天气预报content-desc长度={len(res)}")
        self.log.info(f"天气content-des=>{res}")
        return res

