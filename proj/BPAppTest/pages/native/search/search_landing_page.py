# -*- coding: utf-8 -*-
"""
@Author: shining
@File: search_landing_page.py
@Date: 2022/12/1 2:41 下午
@Version: python 3.9
@Describe: 搜索落地页
"""
from base.UPath import UPath
from base.BP_app import BPApp


class SearchLandingPage(BPApp):

    __search_result_tab = (UPath(name="id/tabLayout"), "")
    __users_tab = (UPath(host=False, text="Users"), "")
    __search_cancel = (UPath(name="id/tvCancel"), "")

    def assert_search_user_in_result(self, search_word="queen"):
        """
        检查搜索的目标用户在搜索结果中
        :return:
        """
        username = "@" + search_word
        search_target_user = (UPath(host=False, text=username), "")
        self.log.info(f"search_target_user={search_target_user}")
        assert self.is_exist(search_target_user)
        return self

    def goto_home_page(self):
        """
        搜索落地页返回首页
        :return:
        """
        self.find_and_click(self.__search_cancel)
        from pages.native.home_page.home_page import HomePage
        return HomePage(self.poco)

    def is_search_landing_page(self):
        """
        判断是否进入搜索落地页成功
        :return:
        """

        return self.is_exist(self.__users_tab) and self.is_exist(self.__search_result_tab)
