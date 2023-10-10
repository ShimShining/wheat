# -*- coding: utf-8 -*-
"""
@Author: shining
@File: settings_page.py
@Date: 2022/5/26 11:03 下午
@Version: python 3.9
@Describe: 设置页
"""
from base.UPath import UPath
from base.BP_app import BPApp


class SettingsPage(BPApp):

    __logout = {"android": UPath(host=True, resourceId="id/logOutLayout"), "ios": ""}
    __popup_confirm = {"android": UPath(host=True, resourceId="id/confirm"), "ios": ""}
    __Languages = {"android": UPath(host=True, resourceId="id/languageText"), "ios": ""}

    __popup_confirm = {"android": UPath(host=True, resourceId="id/tvConfirm"), "ios": ""}
    __account = (UPath(name="id/header_right_image"), "")

    def logout_and_confirm(self):
        self.find_and_click(self.__logout)
        self.find_and_click(self.__popup_confirm)
        from pages.native.login_register.login_page import LoginPage
        return LoginPage(self.poco)

    def goto_account_page(self):

        self.find_and_click(self.__account)
        from pages.native.settings_page.delete_account import AccountPage
        return AccountPage(self.poco)


    #切换语言
    def settings_and_change(self):
        self.find_and_click(self.__Languages)
        pass