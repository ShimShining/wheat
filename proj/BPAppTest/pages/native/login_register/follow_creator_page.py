# -*- coding: utf-8 -*-
"""
@Author: shining
@File: follow_creator_page.py
@Date: 2022/10/19 9:40 下午
@Version: python 3.9
@Describe:
"""
from base.UPath import UPath
from base.BP_app import BPApp


class FollowCreatorPage(BPApp):

    __continue = {'android': UPath(name="id/continueBtn")}
    __finish = {}

    def goto_finish_page(self):

        self.find_and_click(self.__continue)
        from pages.native.login_register.finish_page import FinishPage
        return FinishPage()
