# -*- coding: utf-8 -*-
"""
@Author: shining
@File: logout_flow.py
@Date: 2022/10/24 4:46 下午
@Version: python 3.9
@Describe:从首页开始退出登录
"""
from pages.native.home_page.home_page import HomePage


class LogoutFlow:

    @staticmethod
    def logout_form_home_page(device=None):

        hm = HomePage(mutil_device=device)
        hm.goto_personal_page().goto_settings_page().logout_and_confirm()
