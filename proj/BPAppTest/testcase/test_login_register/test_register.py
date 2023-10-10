# -*- coding: utf-8 -*-
"""
@Author: shining
@File: test_register.py
@Date: 2022/10/25 1:27 下午
@Version: python 3.9
@Describe: 新手注册流程
"""
from flow.native.sign_up_flow import SignUpFlow
from pages.native.home_page.home_page import HomePage


class TestRegister():

    def setup(self):
        self.sl = SignUpFlow()
        self.hm = HomePage()

    def test_register_from_sign_up(self, clear_app_data):
        self.sl.sign_up()
        self.hm.is_home_page()

    def test_register_double_device(self, clear_app_data, start_another_devices):

        self.hm.change_device()
        self.sl.sign_up()
        self.hm.sleep(3)
        self.hm.log.info("============> 开始切换B设备")
        print(f"切换前cur_device = {self.hm.cur_device}")
        self.hm.change_device(device=1)
        another_hm = HomePage(mutil_device=start_another_devices)
        print(f"切换后another_hm.cur_device = {another_hm.cur_device}")
        another_hm.log.info("============> 开始清除B设备")
        another_hm.clear_app()
        another_hm.log.info("============> B设备开始注册")
        another_hm.start_app()
        self.sl.sign_up(device=start_another_devices)
        another_hm.is_home_page()
        self.hm.change_device()
        self.hm.is_home_page()


