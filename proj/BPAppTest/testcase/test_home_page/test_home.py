# -*- coding: utf-8 -*-
from pages.native.home_page.map_detail_page import MapDetailPage
from testcase.BP_app_test import BPAppTest


class TestHomePage(BPAppTest):

    # def setup(self):
    #     self.MapDeta = MapDetailPage()

    def test_home(self, login):
        """
        进入到地图详情
        :return:
        """
        md = login.goto_odyssey_server()



