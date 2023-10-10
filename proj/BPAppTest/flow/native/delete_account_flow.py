# -*- coding: utf-8 -*-
"""
@Author: shining
@File: delete_account_flow.py
@Date: 2022/10/24 2:50 下午
@Version: python 3.9
@Describe: 注销账号流程
"""
from pages.native.home_page.home_page import HomePage
from pages.native.settings_page.settings_page import SettingsPage


class DeleteAccountFlow:

    @staticmethod
    def del_acc_flow(device=None):

        hm = HomePage(mutil_device=device)
        hm.goto_personal_page().goto_settings_page().goto_account_page().goto_delete_acc().\
            goto_delete_your_account_page().goto_delete_confirm_page(). \
            input_reason_and_continue().agree_and_delete_acc().assert_in_login_page()
