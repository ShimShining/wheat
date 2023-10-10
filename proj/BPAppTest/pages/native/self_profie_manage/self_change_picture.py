# -*- coding: utf-8 -*-
# @Time :2022/11/14 5:03 下午
# @File : self_change_picture.py
# @Software :更换头像

from base.UPath import UPath
from base.BP_app import BPApp
from airtest.core.cv import Template
from utils.get_pic import GetPIC as gp
import pic_source.avatar as pkg_avatar
import pic_source.avatar_assert.my_public_profile as pkg_avatar_assert
from base.base_app import BaseApp


class ChangeProfilePicture(BPApp):
    __picture = {"android": UPath(host=True, resourceId="id/tvAvatarChange"), "ios": ""}  # Change Profilr Picture按钮
    __choose = {"android": UPath(host=True, resourceId="id/tvActionSelect"), "ios": ""}  # 更换choose
    __photos = {"android": UPath(host=True, resourceId="id/tvAlbumSelect"), "ios": ""}  # 更换photos
    __album_picture = {"android": UPath(host=True, resourceId="id/cslRoot"), "ios": ""}  # 图片页

    def goto_Change_picture_button(self):  # 点击更换头像 按钮
        self.find_and_click(self.__picture)

    def goto_poses(self):  # 点击更换choose
        self.find_and_click(self.__choose)
        return Choose_a_selfie()

    def selfie_whole(self):
        self.air_assert_exists(self.__Selfie, msg='ghtx,姿势按钮ui异常')

    def fenish_button(self):  # finish按钮
        self.air_touch(self.finish)

    # choose from photos

    def Choose_from_phatos(self):  # 点击更换photos
        self.find_and_click(self.__photos)

    def album(self):  # 选择图片
        self.find_and_click(self.__album_picture)

    def Done_button(self):
        self.find_and_click(self.__done)

    # 换头像选择形象页面


class Choose_a_selfie(BPApp):
    __chooses_pic = gp.get_pic(package=pkg_avatar, pic_name="avar1")  # 拿到 第二个头像
    __chooses = Template(__chooses_pic, record_pos=(-0.005, 0.067), resolution=(1080, 2280))  # 查找

    __done = {"android": UPath(host=True, resourceId="id/doneBtn"), "ios": ""}

    __finish_pic = gp.get_pic(package=pkg_avatar, pic_name="Finish")
    __finish = Template(__finish_pic, record_pos=(0.001, 0.827), resolution=(1080, 2280))

    __selfie_whole = gp.get_pic(package=pkg_avatar, pic_name="selfieaa")
    __Selfie = Template(__selfie_whole, record_pos=(-0.005, 0.224), resolution=(1080, 2280))

    __assert_avatar = gp.get_pic(package=pkg_avatar_assert, pic_name="assert_avatar")
    __assert1 = Template(__assert_avatar, record_pos=(-0.004, 0.414), resolution=(1080, 2280))
    exists = BaseApp()

    # def choose_a_selfie(self):  # choose a selfie
    #     self.air_touch(self.__chooses)
    #     return

    def selfie_whole(self):
        self.air_assert_exists(self.__Selfie, msg='ghtx,姿势按钮ui异常')

    def fenish_button(self):  # finish按钮
        self.air_touch(self.__finish)

    def choose_a_selfie(self):  # choose a selfie111
        self.air_touch(self.__chooses)

    def exists_selfie_finish(self):
        self.air_wait(self.__assert1)


