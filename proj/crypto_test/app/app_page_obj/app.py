# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/13
Describe:app基类封装
"""
from appium import webdriver

from app.app_page_obj.base_app_page import BaseAppPage
from app.app_page_obj.home_page import HomePage


class App(BaseAppPage):

    def start(self):
        """
        启动app
        :return:
        """
        if not self.driver:
            self.log.info("app 类初始化driver")
            caps = {
                "platformName": "android",
                "deviceName": "mumu",
                "appPackage": "hko.MyObservatory_v1_0",
                "appActivity": "hko.homepage.Homepage2Activity",
                "noReset": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True,
                "skipServerInstallation": True,
                "skipDeviceInitialization": True,
                "dontStopAppOnReset": True
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self.driver.implicitly_wait(20)
        else:
            self.log.info("复用已有driver")
            self.driver.launch_app()
        return self

    def restart(self):
        """
        重启app
        :return:
        """
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):

        """
        关闭app session连接
        :return:
        """
        if self.driver:
            self.driver.quit()

    def go_main(self):

        return HomePage(self.driver)

    def skip_guide(self):

        pass
