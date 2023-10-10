# -*- coding: utf-8 -*-
# @Time :2022/11/14 2:35 下午
# @File : self_My_public_profile.py
# @Software :个人公共主——功能人口

from base.UPath import UPath
from base.BP_app import BPApp
from pages.native.self_profie_manage.self_profile_manage import SelfProfileManage



class  PublicHomepaga(BPApp):
    __publicProfileContent = {"android": UPath(host=True, resourceId="id/publicProfileContent"), "ios": ""}    # 进入个人公共主页
    __my_setting = {"android": UPath(host=True, resourceId="id/setting"), "ios": ""}    # 个人主页右上角设置按钮
    __my_avatar = {"android": UPath(host=True, resourceId="id/headImage"), "ios": ""}    # 个人主页头像
    __edit_profile = {"android": UPath(host=True, resourceId="id/tapToEditProfile"), "ios": ""}    # 个人 Edit Profile

    s =SelfProfileManage()

    def goto_home_page(self):    # 返回到首页
        back_btn = self.s.get_back_btn()
        self.find_and_click(back_btn)

    """    
    def goto_my_setting(self): #点击个人公共主页右上角设置按钮
    self.find_and_click(self.__mysetting) 
    """
    def goto_my_avatar(self):    # 点击头像
        self.find_and_click(self.__my_avatar)
        from pages.native.self_profie_manage.self_change_picture import ChangeProfilePicture
        return ChangeProfilePicture(self.poco)

    def goto_edit_profile(self):    # 进入edit profile
        self.find_and_click(self.__edit_profile)

    def goto_My_public_profile(self):    # 进入个人公共主页
        self.find_and_click(self.__publicProfileContent)
