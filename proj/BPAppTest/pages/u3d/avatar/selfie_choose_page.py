# -*- coding: utf-8 -*-
"""
@Author: shining
@File: selfie_choose_page.py
@Date: 2022/10/19 9:16 下午
@Version: python 3.9
@Describe: 头像选择页
"""
from airtest.core.cv import Template
from utils.get_pic import GetPIC as gp
from base.BP_app import BPApp
import pic_source.avatar as pkg


class SelfieChoosePage(BPApp):

    __continue = Template(gp.get_pic(package=pkg, pic_name="selfie_continue"), record_pos=(0.005, 0.592), resolution=(1300, 2080))
    __skip = Template(gp.get_pic(package=pkg, pic_name="selfid_skip"), record_pos=(0.005, 0.592), resolution=(1300, 2080))

    def goto_follow_creator_page(self, method="continue"):

        if method == "continue":
            self.air_touch(self.__continue)
        else:
            self.air_touch(self.__skip)
        from pages.native.login_register.follow_creator_page import FollowCreatorPage
        return FollowCreatorPage()

