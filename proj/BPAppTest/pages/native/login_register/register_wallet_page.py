# -*- coding: utf-8 -*-
"""
@Author: shining
@File: register_wallet_page.py
@Date: 2022/10/24 3:23 下午
@Version: python 3.9
@Describe: 注册流程创建钱包的页面
"""
from base.UPath import UPath
from base.BP_app import BPApp


class RegisterWalletPage(BPApp):

    __skip = (UPath(name="id/header_right_text"), "")
    __create_wallet = (UPath(name="id/createBtn"), '')
    __import_wallet = (UPath(name='id/importBtn'), '')

    def goto_new_user_group_server(self, btn='skip'):
        if btn == 'skip':
            self.find_and_click(self.__skip)
        elif btn == "create":
            self.find_and_click(self.__create_wallet)
        else:
            self.find_and_click(self.__import_wallet)

        self.sleep(3)
        return   # todo 新用户超级群页面

