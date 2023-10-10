# -*- coding: utf-8 -*-
"""
@Author: shining
@File: map_detail_page.py
@Date: 2022/5/25 8:06 下午
@Version: python 3.9
@Describe:
"""
from base.UPath import UPath
from base.BP_app import BPApp
from pages.u3d.engine.room import Room


class MapDetailPage(BPApp):
    __join_public_server = {'android': UPath(host=True, name="id/joinPublicRoom"), 'ios': ""}  # 创建公共房间
    __create_private_server = {'android': UPath(host=True, name="id/joinPrivateRoom"), 'ios': ""}  # 创建私人房间

    # 创建公共房间
    def join_public_server(self):
        self.find(self.__join_public_server).click()
        return Room()

    # 创建私人房间
    def create_private_server(self):
        self.find(self.__create_private_server).click()
        pass
        # return Room()
