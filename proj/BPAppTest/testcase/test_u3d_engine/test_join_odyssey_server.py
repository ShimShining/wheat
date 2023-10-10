# -*- coding: utf-8 -*-
"""
@Author: shining
@File: test_join_server.py
@Date: 2022/11/25 1:45 下午
@Version: python 3.9
@Describe: 加入房间流程
1. 加入房间成功
2. 检查房间里的人列表
3. 做表情
4. check 联机表情广播
5. 退出房间
"""
import pytest

from testcase.BP_app_test import BPAppTest


class TestJoinOdysseyServer(BPAppTest):

    @pytest.mark.parametrize("server_type,", ['public', 'private'])
    def test_join_odyssey_server(self, login, server_type):
        """
        1. 进入首页
        2. 加入公共/私人房间
        3. 点击emote按钮
        4. 做表情hi，并断言hi
        5. 点击房间菜单
        6. 退出房间
        :param login:
        :param server_type:
        :return:
        """

        self.log.info(f"server_type === {server_type}")

        ody = login.goto_odyssey_server(server_type=server_type)
        ody.wait_for_join_odyssey_server_success()
        ody.goto_emote_panel().make_emote()

        hm = ody.leave_room()
        hm.is_home_page()

    def test_join_odyssey_server_make_double_emote(self, login, start_another_devices):
        """
        1. 启动A设备，进入首页
        2. 启动B设备，进入首页
        3. A设备进入大世界kingdom
        4. 切换到B设备，初始化B设备的页面实例
        5. B设备进入大世界kingdom
        6. B设备进房成功，进入表情面板，切换到双人表情tab，点击high five，发起动作
        7. 切换A设备，响应high five，并断言有双人表情联机广播
        8. A设备退出房间，回到首页，断言回到首页成功
        9. 切换B设备，回到首页，断言回到首页成功
        :param login:
        :param start_another_devices:
        :return:
        """
        # 切换到默认设备1
        login.change_device()
        user_a = login.goto_odyssey_server()  # 默认设备进入大世界公共房间

        login.change_device(device=1)    # 切换到设备2
        from pages.native.home_page.home_page import HomePage
        device_b = HomePage(mutil_device=start_another_devices)     # 设备2初始化首页对象
        user_b = device_b.goto_odyssey_server()    # 设备2进入大世界公共房间
        emote = user_b.goto_emote_panel().goto_emote_tab(tab_name='double')   # 设备2打开emote面板，进入双人动作面板
        emote.make_emote(e='high_five')    # 设备2 发起双人high five
        user_b.sleep(1)
        # 设换到设备1
        user_b.change_device()
        emote.response_double_emote(e='high_five')  # 设备1 响应双人动作
        emote.sleep(1)
        home_a = user_a.leave_room()   # 设备1玩家离开房间，回到首页
        home_a.sleep(3)
        home_a.assert_is_home_page()  # 断言设备1 回到首页成功
        # 切换到设备2
        home_a.change_device(device=1)
        home_b = user_b.leave_room()    # 设备2玩家离开房间，回到首页
        home_b.sleep(3)
        home_b.assert_is_home_page()   # 断言设备2 回到首页成功


