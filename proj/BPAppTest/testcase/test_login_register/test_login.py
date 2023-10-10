# -*- coding: utf-8 -*-
"""
@Author: shining
@File: test_login.py
@Date: 2022/5/25 11:13 下午
@Version: python 3.9
@Describe:
"""
from time import sleep
from pages.native.home_page.home_page import HomePage
from pages.native.login_register.account_choose_page import AccountChoosePage
from pages.native.login_register.login_page import LoginPage


class TestLogin():

    # def setup(self):
    #     self.app = LoginPage()
    #     self.acc = AccountChoosePage()
    #     self.home = HomePage()

    def test_login_with_google(self, no_login):
        """
        登录
        :return:
        """
        app = no_login
        home = app.goto_account_page().login_with_google()
        app.sleep(10)
        assert home.is_home_page()

    def test_logout(self, login):
        """
        退出登录
        :return:
        """
        lp = login.goto_personal_page().goto_settings_page().logout_and_confirm()
        lp.is_login_page()

    def test_log_in_with_same_acc(self, login):
        """
        同一账号，退出登录后，点击Log in再次登录
        :return:
        """
        lp = login.goto_personal_page().goto_settings_page().logout_and_confirm()
        lp.is_login_page()
        lp.remember_log_in_same_acc().is_home_page()
