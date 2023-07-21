# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/13
Describe:底层基础页面封装
"""
import os
import sys
import time

import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.log import Logger


log_filename = os.path.realpath(sys.argv[1]).split("\\")[-1]. \
    replace(".py::", "_").replace("::", ".") \
    if sys.argv[1] else None
# log_filename = os.path.basename(__file__)
print(f"日志主文件路径={log_filename}")
print(f"Sys.argv参数列表={sys.argv}")
logger = Logger(log_filename).logger


class BaseAppPage:

    def __init__(self, driver: WebDriver = None):

        self.driver = driver
        self.log = logger

    def wait_for_visible(self, loc, timeout=20, frequency=0.5):

        try:
            self.log.info(f"等待元素{loc}可见")
            WebDriverWait(self.driver, timeout, frequency).\
                until(expected_conditions.visibility_of_element_located(loc))
        except Exception as e:
            raise e

    def scroll_to_text(self, dis_text):

        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().scrollable(true).'
                                        f'instance(0)).scrollIntoView(new UiSelector().text("{dis_text}").'
                                        'instance(0));')

    def find(self, mobile_by, path=None):

        if path:
            return self.driver.find_element(mobile_by, path)
        return self.driver.find_element(*mobile_by)

    def finds(self, mobile_by, path=None):

        if path:
            return self.driver.find_elements(mobile_by, path)
        return self.driver.find_elements(*mobile_by)

    def check_toast_info(self, info):
        """

        :return:
        """
        try:
            self.driver.find_element(MobileBy.XPATH,
                                     f"//*[@class='android.widget.Toast' and @text='{info}']")
            self.log.info(f"查找定位文本信息=[{info}]成功.")
        except NoSuchElementException as e:
            self.log.error(f"查找定位文本信息=[{info}]失败!!!")

    def swipe_find(self, text, limit=5):
        '''
        滑动查找text
        :param text:
        :param limit:
        :return:
        '''
        loc = (MobileBy.XPATH, f"//*[@text='{text}']")
        self.driver.implicitly_wait(6)
        for i in range(limit):
            try:
                element = self.find(loc)
                self.driver.implicitly_wait(10)
                self.log.info(f"查找元素{loc}成功")
                return element
            except NoSuchElementException:
                self.log.info(f"未找到{text}文本,继续滑动查找")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']
                start_x = width / 2
                start_y = height * 0.8
                to_x = width / 2 + width * 1 / 9
                to_y = height * 0.3
                duration = 2000   # 毫秒
                self.driver.swipe(start_x, start_y, to_x, to_y, duration)
            if i == limit - 1:
                self.driver.implicitly_wait(10)
                self.log.error(f"查找元素{loc}失败")
                raise NoSuchElementException(f"查找文本text={text}[{i+1}]次后未找到.")

    def save_screenshot(self, src_des):
        """
        截图
        :param src_des:截图说明
        :return:
        """
        OUTPUTS_DIR = 'D:\\personProc\\crypto_test\\logs'
        file_name = OUTPUTS_DIR + "\\{}_{}.png".format(time.strftime("%Y%m%d%H%M", time.localtime(time.time())), src_des)
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
            allure.attach(file, src_des, allure.attachment_type.PNG)
        self.logger.info("页面截图文件保存在：{}".format(file_name))

    def clear_env(self):

        time.sleep(2)
        self.driver.quit()
