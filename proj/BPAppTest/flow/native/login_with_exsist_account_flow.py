# -*- coding: utf-8 -*-
"""
@Author: shining
@File: login_with_exsist_account_flow.py
@Date: 2022/10/24 3:08 下午
@Version: python 3.9
@Describe: 使用已有账号登录进入首页
"""
from pages.native.login_register.login_page import LoginPage


class LoginWithExistAccFlow:

    @staticmethod
    def login_in(acc=None, device=None):

        lp = LoginPage(mutil_device=device)
        return lp.goto_account_page().login_with_google(acc=acc)

