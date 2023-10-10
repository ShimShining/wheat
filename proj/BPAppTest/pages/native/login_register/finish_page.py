# -*- coding: utf-8 -*-
"""
@Author: shining
@File: finish_page.py
@Date: 2022/10/20 1:19 下午
@Version: python 3.9
@Describe:团体推荐完成页
"""
from base.UPath import UPath
from base.BP_app import BPApp
from pages.native.login_register.register_wallet_page import RegisterWalletPage


class FinishPage(BPApp):

    __finish = (UPath(name='id/continueBtn'), '')

    def goto_create_wallet_page(self):

        self.find_and_click(self.__finish)
        return RegisterWalletPage(self.poco)


