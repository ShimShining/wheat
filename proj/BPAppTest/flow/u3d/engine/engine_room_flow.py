# -*- coding: utf-8 -*-
"""
@Author: shining
@File: engine_make_emote_flow.py
@Date: 2022/11/24 9:17 下午
@Version: python 3.9
@Describe: 房间内做表情流
"""


class EngineRoomFlow:

    def __init__(self, server=None, emote=None, device=None):

        if server:
            self.server = server
        else:
            from pages.u3d.engine.room import Room
            self.server = Room(mutil_device=device)
        if emote:
            self.emote = emote
        else:
            from pages.u3d.engine.emote import Emote
            self.emote = Emote(mutil_device=device)

    def make_emote_flow(self, e='hi'):

        return self.server.goto_emote_panel().make_emote(e=e)

    def check_odyssey_people_in_the_server_flow(self):

        self.server.goto_people_in_the_server_panel()
        self.server.assert_enter_room_success()
        return self.server.close_odyssey_people_in_the_server_panel()

