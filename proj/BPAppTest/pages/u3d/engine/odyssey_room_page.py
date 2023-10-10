# -*- coding: utf-8 -*-
"""
@Author: shining
@File: OdysseyRoomPage.py
@Date: 2022/11/23 4:44 下午
@Version: python 3.9
@Describe: 大世界地图页
"""
from airtest.core.cv import Template

from base.UPath import UPath
from base.BP_app import BPApp
from pages.u3d.engine.room import Room
from utils.get_pic import GetPIC as gp
import pic_source.room as pkg


class OdysseyRoomPage(Room):
    # 点击左上角菜单后的icon
    __leave_pic = gp.get_pic(package=pkg, pic_name="leave")  # leave按钮
    __leave = Template(__leave_pic, record_pos=(0.001, 0.169), resolution=(1600, 720))
    __close_pic = gp.get_pic(package=pkg, pic_name="close")
    __close = Template(__close_pic, record_pos=(-0.442, -0.184), resolution=(1600, 720))

    __how_to_play_guide_pic = gp.get_pic(package=pkg, pic_name="how_to_play_guide")
    __how_to_play_guide = Template(__how_to_play_guide_pic, record_pos=(0.449, -0.134), resolution=(1600, 720))
    __how_to_play_pic = gp.get_pic(package=pkg, pic_name="how_to_play")
    __how_to_play = Template(__how_to_play_pic, record_pos=(-0.003, 0.164), resolution=(1600, 720))
    __next_pic = gp.get_pic(package=pkg, pic_name="next")
    __next = Template(__next_pic, record_pos=(0.0, 0.163), resolution=(1600, 720))
    __start_pic = gp.get_pic(package=pkg, pic_name="start")
    __start = Template(__start_pic, record_pos=(-0.002, 0.163), resolution=(1600, 720))

    def leave_room(self):
        """
        大世界离开房间
        :return:
        """
        self.goto_people_in_the_server_panel()
        self.air_touch(self.__leave)
        self.sleep(3)
        from pages.native.home_page.home_page import HomePage
        return HomePage(self.poco)

    def close_odyssey_people_in_the_server_panel(self):
        self.air_touch(self.__close)
        return self

    def handle_how_to_play_guide(self):
        if self.air_exist(self.__how_to_play):
            self.air_touch(self.__how_to_play)
            self.air_touch(self.__next)
            self.air_touch(self.__next)
            self.air_touch(self.__start)


if __name__ == '__main__':
    orp = OdysseyRoomPage()
    orp.leave_room()
