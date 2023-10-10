# -*- coding: utf-8 -*-
"""
@Author: shining
@File: gender_choose_page.py
@Date: 2022/10/25 9:31 下午
@Version: python 3.9
@Describe: 性别选择页
"""
from base.UPath import UPath
from base.BP_app import BPApp
from pages.u3d.avatar.register_avatar_page import RegisterAvatarPage


class GenderChoosePage(BPApp):

    __male = {"android": UPath(name="id/icMale")}
    __female = {"android": UPath(name="id/icFemale")}
    __gender_queer = {"android": UPath(name="id/icQueer")}
    __skip = {"android": UPath(name="id/header_right_text")}
    __continue = UPath(name="id/continueBtn")

    def choose_gender_to_avatar(self, gender="female"):
        if gender == 'male':
            self.find_and_click(self.__male)
        elif gender == "queer":
            self.find_and_click(self.__gender_queer)
        else:
            self.find_and_click(self.__female)
        self.click_continue()
        return RegisterAvatarPage()

    def click_continue(self):

        self.find_and_click(self.__continue)

    def click_skip(self):

        self.find_and_click(self.__skip)
