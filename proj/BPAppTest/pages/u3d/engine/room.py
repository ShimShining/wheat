# -*- coding: utf-8 -*-
"""
@Author: shining
@File: room.py
@Date: 2022/5/25 8:45 下午
@Version: python 3.9
@Describe: 联机房间封装
大世界
普通ugc
可继承此类
"""
import time

from airtest.core.cv import Template
import pic_source.room as pkg
from base.UPath import UPath
from base.BP_app import BPApp
from utils.get_pic import GetPIC as gp


class Room(BPApp):
    # loading页的返回按钮
    __loading_back_pic = gp.get_pic(package=pkg, pic_name="loading_back")
    _loading_back = Template(__loading_back_pic, record_pos=(-0.437, -0.176), resolution=(2160, 1080))
    __menu_pic = gp.get_pic(package=pkg, pic_name="menu")
    _menu = Template(__menu_pic, record_pos=(-0.428, -0.181), resolution=(1600, 720))
    # 点击左上角菜单后的icon
    __head_img_pic = gp.get_pic(package=pkg, pic_name="head_img")  # 头像
    _head_img = Template(__head_img_pic)

    __chat_pic = gp.get_pic(package=pkg, pic_name="chat")  # 聊天信息框按钮
    _chat = Template(__chat_pic, record_pos=(-0.383, -0.181), resolution=(1600, 720))
    # 右上角菜单
    __share_pic = gp.get_pic(package=pkg, pic_name="share")  # 分享按钮
    _share = Template(__share_pic, record_pos=(0.189, -0.182), resolution=(1600, 720))
    __back_birth_point_pic = gp.get_pic(package=pkg, pic_name="back_birth_point")
    _back_birth_point = Template(__back_birth_point_pic, record_pos=(0.244, -0.182), resolution=(1600, 720))
    __clothes_change_pic = gp.get_pic(package=pkg, pic_name="clothes_change")
    _clothes_change = Template(__clothes_change_pic, record_pos=(0.297, -0.181), resolution=(1600, 720))
    __camera_pic = gp.get_pic(package=pkg, pic_name="camera")
    _camera = Template(__camera_pic, record_pos=(0.351, -0.181), resolution=(1600, 720))
    __camera_shutter_pic = gp.get_pic(package=pkg, pic_name="camera_shutter")
    _camera_shutter = Template(__camera_shutter_pic, record_pos=(0.406, -0.053), resolution=(1600, 720))
    __camera_selfie_pic = gp.get_pic(package=pkg, pic_name="camera_selfie")
    _camera_selfie = Template(__camera_selfie_pic, record_pos=(0.404, -0.184), resolution=(1600, 720))
    __camera_selfie_exit_pic = gp.get_pic(package=pkg, pic_name="camera_selfie_exit")
    _camera_selfie_exit = Template(__camera_selfie_exit_pic, record_pos=(0.403, -0.184), resolution=(1600, 720))
    __camera_exit_pic = gp.get_pic(package=pkg, pic_name="camera_exit")
    _camera_exit = Template(__camera_exit_pic, record_pos=(-0.427, -0.183), resolution=(1600, 720))
    __take_photo_pic = gp.get_pic(package=pkg, pic_name="take_photo")
    _take_photo = Template(__take_photo_pic, record_pos=(0.406, -0.181), resolution=(1600, 720))
    __settings_pic = gp.get_pic(package=pkg, pic_name="__settings")
    _settings = Template(__settings_pic, record_pos=(0.459, -0.181), resolution=(1600, 720))
    # 底部按钮
    __control_rod_pic = gp.get_pic(package=pkg, pic_name="control_rod")
    _control_rod = Template(__control_rod_pic, record_pos=(-0.354, 0.12), resolution=(1600, 720))
    __voice_open_pic = gp.get_pic(package=pkg, pic_name="voice_open")
    _voice_open = Template(__voice_open_pic, record_pos=(-0.174, 0.176), resolution=(1600, 720))
    __micro_open_pic = gp.get_pic(package=pkg, pic_name="micro_open")
    _micro_open = Template(__micro_open_pic, record_pos=(-0.134, 0.174), resolution=(1600, 720))
    _permission_allow = (UPath(name="id/permission_allow_foreground_only_button"), "")
    __voice_close_pic = gp.get_pic(package=pkg, pic_name="voice_close")
    _voice_close = Template(__voice_close_pic, record_pos=(-0.172, 0.175), resolution=(1600, 720))
    __micro_close_pic = gp.get_pic(package=pkg, pic_name="micro_close")
    _micro_close = Template(__micro_close_pic, record_pos=(-0.136, 0.177), resolution=(1600, 720))
    __input_pic = gp.get_pic(package=pkg, pic_name="input")
    _input = Template(__input_pic, record_pos=(0.018, 0.176), resolution=(1600, 720))
    __emote_pic = gp.get_pic(package=pkg, pic_name="emote")
    _emote = Template(__emote_pic, record_pos=(0.169, 0.176), resolution=(1600, 720))

    __jump_key_pic = gp.get_pic(package=pkg, pic_name="jump_key")
    _jump_key = Template(__jump_key_pic, record_pos=(0.386, 0.128), resolution=(1600, 720))

    def wait_for_join_odyssey_server_success(self, timeout=25):
        self.wait_loading_page_close()
        self.handle_how_to_play_guide()
        s = int(time.time())

        while not self.air_exist(self._chat):
            self.air_wait(self._chat)
            if int(time.time()) - s > timeout:
                break

    @staticmethod
    def control_rod_vector(direction='up'):
        return {
            "up": [-0.005, -0.1459],
            "down": [0.0071, 0.1609],
            "left": [-0.0788, 0.011],
            "right": [0.074, -0.0046],
            "ur": [0.0701, -0.0703],
            'ul': [-0.0596, -0.096],
            'dl': [-0.0493, 0.1209],
            "dr": [0.0695, 0.0739]
        }.get(direction, [0.0528, -0.1117])

    def swipe_control_rod(self, direction="up", duration=0.1):
        """
        swipe(Template(r"tpl1669280634766.png", record_pos=(-0.354, 0.121), resolution=(1600, 720)), vector=[0.047, -0.1145], duration=10)
        swipe(Template(r"tpl1669280880266.png", record_pos=(-0.356, 0.121), resolution=(1600, 720)), vector=[-0.057, -0.1059], duration=2)
        swipe(Template(r"tpl1669280893839.png", record_pos=(-0.357, 0.122), resolution=(1600, 720)), vector=[0.0598, 0.0368], duration=1)
        swipe(Template(r"tpl1669281526547.png", record_pos=(-0.356, 0.12), resolution=(1600, 720)), vector=[-0.0372, 0.1067])
        ['up', "down", "left", "right", "ur", 'ul', 'dl', "dr"]
        :return:
        """
        end_point = self.control_rod_vector(direction=direction)
        self.air_swipe(self._control_rod, vector=end_point, duration=duration)
        return self

    def goto_emote_panel(self):
        self.air_touch(self._emote)
        from pages.u3d.engine.emote import Emote
        return Emote()

    def goto_people_in_the_server_panel(self):
        """
        打开房间里的人列表
        :return:
        """

        self.air_touch(self._menu)

    def assert_enter_room_success(self):

        self.air_assert_exists(self._head_img)

    def wait_loading_page_close(self, timeout=25):
        """
        等待loading加载页是否关闭，超时时间默认25秒
        :param timeout:
        :return:
        """
        s = int(time.time())

        while self.air_exist(self._loading_back):
            flag = (not self.air_exist(self._loading_back)) or self.air_exist(self._chat)
            if flag:
                break
            if int(time.time()) - s > timeout:
                break

    def back_to_birth_point(self):
        """
        返回出生点
        :return:
        """

        if self.air_exist(self._back_birth_point):
            self.air_exist(self._back_birth_point)
        return self
