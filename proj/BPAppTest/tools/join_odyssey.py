# -*- coding: utf-8 -*-
"""
@Author: shining
@File: join_odyssey.py
@Date: 2022/11/25 2:34 下午
@Version: python 3.9
@Describe:
"""
import time

from airtest.core.api import *
from config import Config
from flow.u3d.engine.engine_room_flow import EngineRoomFlow
from pages.native.home_page.home_page import HomePage


def init_app(dev=None):

    platform = Config.PLATFORM
    if platform == 'android':
        # 使用auto_setup
        if not dev:
            auto_setup(__file__, devices=Config.PACKAGE_LIST['android']['devices_list'])
        else:
            connect_device(dev)
        start_app(Config.BUNDLE_ID)
    elif platform == 'ios':
        if dev:
            auto_setup(__file__, devices=["iOS:///http://127.0.0.1:8100"])
        else:
            connect_device(dev)
        start_app(Config.BUNDLE_ID)
    else:
        # 连接安卓
        auto_setup(__file__)
        start_app(Config.BUNDLE_ID)


def start(dev=None):

    bundle_id = Config.BUNDLE_ID
    # stop_app(bundle_id)

    init_app(dev=dev)
    from pages.native.home_page.home_page import HomePage
    hm = HomePage()
    if hm.is_home_page():
        hm.handle_home_page_popup()
        return hm

    # stop_app(Config.BUNDLE_ID)
    # app_init()
    from flow.native.login_with_exsist_account_flow import LoginWithExistAccFlow
    login_flow = LoginWithExistAccFlow()
    return login_flow.login_in()


class JoinOdyssey:

    def join(self, server_type="public", home_page: HomePage = None):

        if not home_page:
            home_page = HomePage()
        ody = home_page.goto_odyssey_server(server_type=server_type)
        ody.sleep(27)
        emote = ody.goto_emote_panel()
        emote.make_emote()
        return ody.leave_room()

    def joins(self, times=1, home_obj=None):
        tmp = home_obj
        for i in range(times):
            s = time.time()
            print(f"=============> 第{i + 1}次进房")
            tmp = self.join(home_page=tmp)
            end = time.time()
            print(f"进房耗时{end -s} 秒")
            time.sleep(3)


if __name__ == '__main__':

    hm = start()

    join_server = JoinOdyssey()

    join_server.joins(home_obj=hm, times=5)
