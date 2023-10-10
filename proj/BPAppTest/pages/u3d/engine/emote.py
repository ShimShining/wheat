# -*- coding: utf-8 -*-
"""
@Author: shining
@File: emote.py
@Date: 2022/11/24 6:12 下午
@Version: python 3.9
@Describe: 联机点击表情后展开的面板
"""
from base.BP_app import BPApp
from airtest.core.cv import Template
from utils.get_pic import GetPIC as gp
import pic_source.emote as pkg


class Emote(BPApp):

    __favorite_pic = gp.get_pic(package=pkg, pic_name="favorite")
    _favorite = Template(__favorite_pic, record_pos=(0.171, -0.211), resolution=(2160, 1080))
    __single_pic = gp.get_pic(package=pkg, pic_name="single")
    _single = Template(__single_pic, record_pos=(0.242, -0.212), resolution=(2160, 1080))
    __circle_pic = gp.get_pic(package=pkg, pic_name="circle")
    _circle = Template(__circle_pic, record_pos=(0.315, -0.211), resolution=(2160, 1080))
    __double_pic = gp.get_pic(package=pkg, pic_name="double")
    _double = Template(__double_pic, record_pos=(0.384, -0.212), resolution=(2160, 1080))
    __special_pic = gp.get_pic(package=pkg, pic_name="special")
    _special = Template(__special_pic, record_pos=(0.455, -0.212), resolution=(2160, 1080))
    # 单人表情
    __hi_pic = gp.get_pic(package=pkg, pic_name="hi")
    __hi_success = gp.get_pic(package=pkg, pic_name="hi_success")
    # 双人表情
    __double_emote_response = gp.get_pic(package=pkg, pic_name="double_emote_response")
    __high_five = gp.get_pic(package=pkg, pic_name="high_five")
    __high_five_success = gp.get_pic(package=pkg, pic_name="high_five_success")

    def get_locator(self):
        return {
            "hi": Template(self.__hi_pic, record_pos=(0.256, -0.126), resolution=(1600, 720)),
            "hi_success": Template(self.__hi_success, record_pos=(-0.351, 0.006), resolution=(1600, 720)),
            "high_five": Template(self.__high_five, record_pos=(0.226, -0.081), resolution=(2160, 1080)),
            "double_emote_response": Template(self.__double_emote_response, record_pos=(0.114, -0.066), resolution=(2160, 1080)),
            "high_five_success": Template(self.__high_five_success, record_pos=(-0.362, 0.031), resolution=(2160, 1080))
        }

    def make_emote(self, e='hi'):
        """
        todo 滑动查找
        :param e:
        :return:
        """
        self.air_touch(getattr(self, e))
        self.sleep(1)
        self.assert_emote_success(e=e)
        from pages.u3d.engine.room import Room
        return Room()

    def assert_emote_success(self, e='hi'):
        e_success = e + '_success'
        self.air_assert_exists(getattr(self, e_success))

    def response_double_emote(self, e='high_five'):

        self.air_touch(getattr(self, "double_emote_response"))
        self.assert_emote_success(e=e)

    def goto_emote_tab(self, tab_name='single'):
        if tab_name == 'single':
            self.air_touch(self._single)
            return self
        if tab_name == 'favorite':
            self.air_touch(self._favorite)
            return self
        if tab_name == 'circle':
            self.air_touch(self._circle)
            return self
        if tab_name == 'double':
            self.air_touch(self._double)
            return self
        if tab_name == 'special':
            self.air_touch(self._special)
        return self
