# -*- coding: utf-8 -*-
"""
@Author: shining
@File: search_input_page.py
@Date: 2022/12/1 2:38 下午
@Version: python 3.9
@Describe: 搜索输入页面
"""
from base.UPath import UPath
from base.BP_app import BPApp


class SearchInputPage(BPApp):

    __search_input = (UPath(name="id/editText"), "")

    def goto_search_landing_page(self, search_word="queen"):
        """
        输入搜索词，点击搜索，进入搜索落地页
        :param search_word: 搜索关键词
        :return:
        """
        # self.input_text(self.__search_input, search_word)
        self.find_and_click(self.__search_input)
        self.input_text(self.__search_input, "")
        # poco("com.pointone.BPdyglobal:id/editText").set_text("thisi")
        self.air_text(search_word, search=True)

        from pages.native.search.search_landing_page import SearchLandingPage
        slp = SearchLandingPage(self.poco)
        if not slp.is_search_landing_page():
            self.find_and_click(self.__search_input)
            self.input_text(self.__search_input, "")
            self.air_text(search_word, search=True)
        return slp

