# -*- coding: utf-8 -*-
"""
@Author: shining
@File: birthday_page.py
@Date: 2022/5/25 11:06 下午
@Version: python 3.9
@Describe:
"""
from base.UPath import UPath
from base.bp_app import BPApp
from pages.native.login_register.gender_choose_page import GenderChoosePage
from pages.u3d.avatar.register_avatar_page import RegisterAvatarPage


class BirthdayPage(BPApp):

    __continue = (UPath(name="id/continueBtn"), '')

    def goto_gender_choose_page(self):
        self.find_and_click(self.__continue)
        return GenderChoosePage(self.poco)

