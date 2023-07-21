# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/13
Describe:首页
"""
from appium.webdriver.common.mobileby import MobileBy

from app.app_page_obj.base_app_page import BaseAppPage


class HomePage(BaseAppPage):

    __menu_btn = (MobileBy.ACCESSIBILITY_ID, "转到上一层级")
    __home = (MobileBy.ID, "hko.MyObservatory_v1_0:id/home_page")

    def goto_menu_page(self):

        self.find(self.__menu_btn).click()
        self.log.info("点击进入侧边栏菜单按钮成功")
        elem = self.find(self.__home)
        if elem:
            self.log.info("吊起侧边栏菜单成功")
        else:
            self.log.error("未成功吊起侧边栏")
        from app.app_page_obj.menu_page import MenuPage
        return MenuPage(self.driver)

