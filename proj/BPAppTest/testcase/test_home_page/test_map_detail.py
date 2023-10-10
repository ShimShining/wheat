# -*- coding: utf-8 -*-
"""
@Author: shining
@File: test_map_detail.py
@Date: 2022/10/25 1:21 下午
@Version: python 3.9
@Describe: 地图详情页测试
"""


class TestMapDetail():

    def test_create_private(self, login):
        login.create_private_server()

         #进公共房间
    def test_join_public(self, login):
        login.join_public_server()
