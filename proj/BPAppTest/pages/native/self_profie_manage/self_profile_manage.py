# -*- coding: utf-8 -*-
"""
@Author: shining
@File: self_profile_manage.py
@Date: 2022/5/26 10:58 下午
@Version: python 3.9
@Describe: 点击首页头像，进入的个人主页管理页
"""
from base.UPath import UPath
from base.BP_app import BPApp
from pages.native.settings_page.settings_page import SettingsPage


class SelfProfileManage(BPApp):

    __setting = {"android": UPath(host=True, resourceId="id/setting"), "ios": ""}
    __bind_account = (UPath(name="id/clBindAccount"), "")
    __back = (UPath(name='id/back'), '')

    def goto_settings_page(self):

        self.find_and_click(self.__setting)
        return SettingsPage(self.poco)

    def is_bind_account(self):
        """
        是否绑定三方账号
        :return:
        """
        return self.is_exist(self.__bind_account)

    def back_to_home_page(self):

        self.find_and_click(self.__back)

    def get_back_btn(self):
        return self.__back


