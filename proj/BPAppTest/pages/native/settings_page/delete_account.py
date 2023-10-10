# -*- coding: utf-8 -*-
"""
@Author: shining
@File: delete_account.py
@Date: 2022/10/24 2:13 下午
@Version: python 3.9
@Describe: 注销账号-各个流程界面
"""
from base.UPath import UPath
from base.BP_app import BPApp


class AccountPage(BPApp):

    __manage_account = (UPath(name="id/manageAccountLayout"), "")

    def goto_delete_acc(self):

        self.find_and_click(self.__manage_account)
        return ManageAccountPage(self.poco)


class ManageAccountPage(BPApp):

    __delete_acc = (UPath(name="id/deleteAccountLayout"), "")

    def goto_delete_your_account_page(self):

        self.find_and_click(self.__delete_acc)
        return DeleteYourAccountPage(self.poco)


class DeleteYourAccountPage(BPApp):

    __continue = (UPath(name="id/continueBtn"))

    def goto_delete_confirm_page(self):
        self.sleep(12)   # 等待continue按钮可点击
        self.find_and_click(self.__continue)
        return DeleteConfirmPage(self.poco)


class DeleteConfirmPage(BPApp):

    __del_reason = (UPath(name="id/reason"), "")
    __continue = (UPath(name="id/continueBtn"), "")

    def input_reason_and_continue(self, content="automation test delete account!!!"):

        self.input_text(self.__del_reason, content=content)
        self.find_and_click(self.__continue)
        return DeleteAgreePage(self.poco)


class DeleteAgreePage(BPApp):

    __agree_btn = (UPath(name="id/selectIv"), '')
    __delete_account = (UPath(name="id/deleteBtn"), "")
    __confirm_delete = (UPath(name="id/tvConfirm"), '')

    def agree_and_delete_acc(self):

        self.find_and_click(self.__agree_btn)
        self.find_and_click(self.__delete_account)
        self.find_and_click(self.__confirm_delete)
        from pages.native.login_register.login_page import LoginPage
        return LoginPage()


