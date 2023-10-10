# -*- coding: utf-8 -*-
"""
@Author: shining
@File: register_avatar_page.py
@Date: 2022/10/19 5:00 下午
@Version: python 3.9
@Describe:
"""
from airtest.core.cv import Template

from base.BP_app import BPApp
from utils.get_pic import GetPIC as gp
import pic_source.avatar as pkg


class RegisterAvatarPage(BPApp):

    __done_pic = gp.get_pic(package=pkg, pic_name="avatar_done")
    __done = Template(__done_pic, record_pos=(0.413, -0.643), resolution=(1300, 2080))

    def goto_profile_picture(self):

        self.air_touch(self.__done)
        from pages.u3d.avatar.selfie_choose_page import SelfieChoosePage
        return SelfieChoosePage()


