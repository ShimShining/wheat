# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/12
Describe:基础页面封装
"""
import datetime
import os
import sys
import time

import allure
from selenium import webdriver
from selenium.webdriver import TouchActions
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


class BasePage:

    __base_url = 'https://crypto.com/exchange/'

    def __init__(self, origin_driver=None):

        self.logger = logger
        if origin_driver is None:

            option = webdriver.ChromeOptions()
            option.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(self.__base_url)
            self.logger.info("初始化driver成功")
        else:
            self.driver = origin_driver

    def find(self, by, elem=None):

        if elem:
            return self.driver.find_element(by, elem)
        return self.driver.find_element(*by)

    def finds(self, by, elem=None):

        if elem:
            return self.driver.find_elements(by, elem)
        return self.driver.find_elements(*by)

    def scroll_to_element_div(self, elem):

        self.logger.info(f"开始滑动查找元素{elem}")
        div = self.find(elem)
        js_code = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js_code, div)
        self.logger.info(f"滑动到元素{elem}成功.元素可见.")

    def scroll_to_bottom(self):

        self.driver.execute_script("document.documentElement.scrollTop=15000")
        self.logger.info("滑动到页面底部成功")

    def scroll(self, elem, x, y):

        loc = self.find(elem)
        action = TouchActions(self.driver)
        action.scroll_from_element(loc, x, y).perform()
        self.logger.info(f"滑动页面[{y}]px成功")

    def scroll_by(self, x, y):

        js = f"window.scrollBy({x}, {y})"
        self.logger.info(f"滑动js脚本是{js}.")
        self.driver.execute_script(js)
        self.logger.info(f"滑动页面[{y}]px成功")

    def js_find_by_class_name(self, elem):

        _, cls_name = elem
        cls_name = cls_name[1:]
        js = f'return document.getElementsByClassName({cls_name})'
        loc = self.driver.execute_script(js)
        return loc

    def js_click(self, elem):

        loc = self.find(elem)
        self.driver.execute_script("(arguments[0]).click()", loc)
        self.logger.info(f"{elem}使用js点击成功.")

    def wait_for_visible(self, elem, timeout=10):

        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(elem))
        self.logger.info(f"{elem}-->可见=True")

    def wait_for_any_visible(self, elems, timeout=15):

        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_any_elements_located(elems))
        self.logger.info(f"{elems}-->可见=True")

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

        self.driver.quit()

