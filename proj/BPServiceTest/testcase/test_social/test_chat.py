# -*- coding: utf-8 -*-
"""
@Author: longyonghe
@File: test_get_chat_list.py
@Date: 2022/10/27 11:30
@Version: python 3.10
@Describe:
"""
import time

import allure
import pytest

from us_api_test.business.social.chat import Chat
from us_api_test.business.social.social import Social
from us_api_test.config import Config
from proj.BPServiceTest.testcase.service_test import ServiceTest


class TestChat(ServiceTest):

    def setup(self):
        self.chat = Chat()
        self.soc = Social()
        self.uid = Config.case_data("global_user_info.yml").uid
        self.chat_test = Config.case_data("chat.yml")
        self.members = self.chat_test.members
        self.leave_members = self.chat_test.leave_members
        self.req = Config.case_data_dict("multi_share.yml", "multi_share_body")

    @pytest.mark.smoking
    @pytest.mark.chat
    @allure.story("拉取单聊会话列表")
    def test_get_chat_list_DM(self, BUDGlobalArgs):
        chat_info = dict()
        chat_info['chat_type'] = 0  # 0单聊，1群聊，2queen公告，3超级群
        chat_info['target_id'] = ""
        r = self.soc.post_multi_share(self.uid, self.req)  # 分享地图至会话
        self.assert_result_is_zero(r)
        r1 = self.chat.post_chat_list_info(self.uid, chat_info)
        self.assert_rsmg_is_empty(r1)
        self.assert_data_not_empty(r1)
        self.assert_not_empty(r1["data"]["chatList"], msg='r1["data"]["chatList"]')

    @pytest.mark.smoking
    @pytest.mark.chat
    @pytest.mark.dependency(name='pre')  # 执行用例顺序排序，depends一定在name后执行
    @allure.story("创建超级群")
    @pytest.mark.run(order=1)
    def test_create_group_chat(self, BUDGlobalArgs):  # BUDGlobalArgs是fixture全局变量的一种方式，放在conftest.py内定义空字典，在case层传入，全局可调用
        chat_info = dict()
        chat_info["chat_type"] = 3  # 0单聊，1群聊，2queen公告，3超级群
        chat_info["target_id"] = ""
        chat_info["uid"] = self.uid
        chat_info["operation"] = 0  # (0创建群聊，1删除群聊，2修改群名，3邀请用户，4剔除用户，5用户退群，
        # 6修改群头像（仅团体群聊）7用户进群 8修改简介 9设置三方平台 10取消三方平台 11修改Icon)
        stmp = str(int(time.time() * 1000))
        chat_info["teamName"] = "test_group" + "+" + stmp
        r1 = self.chat.post_set_group(self.uid, chat_info)  # 创建超级群
        self.assert_api_success_code(r1)
        self.assert_not_empty(r1)
        self.assert_not_empty(r1["data"]["chatInfo"]["targetId"], msg='r1["data"]["chatInfo"]["targetId"]')
        self.assert_not_empty(r1["data"]["chatInfo"]["teamInfo"]["teamId"], msg='r1["data"]["chatInfo"]["teamInfo"]["teamId"]')
        BUDGlobalArgs['rsp'] = r1["data"]

    @pytest.mark.smoking
    @pytest.mark.chat
    @allure.story("拉取超级群会话列表")
    def test_get_group_chat_list(self, BUDGlobalArgs):
        r = self.chat.get_group_chat_list(self.uid)  # 查询超级群会话列表
        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        self.assert_not_empty(r["data"]["chatList"], msg='r["data"]["chatList"]')
        self.assert_not_empty(r["data"]["chatList"][0]["targetId"], msg='r["data"]["chatList"][0]["targetId"]')
        BUDGlobalArgs["isEnd"] = r["data"]["isEnd"]
        BUDGlobalArgs["cookie"] = r["data"]["cookie"]

    @pytest.mark.smoking
    @pytest.mark.chat
    @allure.story("翻页拉取超级群列表")
    def test_get_group_chat_list_V2(self, BUDGlobalArgs):
        cookie = BUDGlobalArgs.get("cookie", None)
        isEnd = BUDGlobalArgs.get("isEnd", None)
        if isEnd == 1:
            pytest.skip("超级群会话不足一页")
        else:
            r = self.chat.get_group_chat_list(self.uid, cookie=cookie)  # 拉取第二页
            self.assert_api_success_code(r)
            self.assert_not_empty(r["data"]["chatList"], msg='r["data"]["chatList"]')
            self.assert_not_empty(r["data"]["chatList"][0]["targetId"], msg='r["data"]["chatList"][0]["targetId"]')
            cookie = r["data"]["cookie"]
            if r["data"]["isEnd"] != 1:
                r1 = self.chat.get_group_chat_list(self.uid, cookie=cookie)  # 拉取第三页
                self.assert_api_success_code(r1)
                self.assert_not_empty(r1["data"]["chatList"], msg='r1["data"]["chatList"]')
                self.assert_not_empty(r1["data"]["chatList"][0]["targetId"], msg='r1["data"]["chatList"][0]["targetId"]')

    @pytest.mark.smoking
    @pytest.mark.chat
    @pytest.mark.dependency(depends=['pre'])
    @allure.story("修改超级群群名称")
    @pytest.mark.run(order=2)
    def test_modify_group_name(self, BUDGlobalArgs):
        chat_info = dict()
        rsp = BUDGlobalArgs.get("rsp", None)
        target_id = rsp["chatInfo"]["targetId"]
        team_id = rsp["chatInfo"]["teamInfo"]["teamId"]
        team_name = rsp["chatInfo"]["teamInfo"]["teamName"]
        chat_info["target_id"] = target_id
        chat_info["operation"] = 2
        chat_info["teamId"] = team_id
        stmp = str(int(time.time()))
        chat_info["teamName"] = "updata_name_" + stmp
        r = self.chat.post_set_group(self.uid, chat_info)
        self.assert_api_success_code(r)
        self.assert_not_empty(r["data"], msg='r["data"]')
        self.assert_not_empty(r["data"]["chatInfo"], msg='r["data"]["chatInfo"]')
        self.assert_not_value(r["data"]["chatInfo"]["teamInfo"]["teamName"], team_name)
        rsp["chatInfo"]["teamInfo"]["teamName"] = r["data"]["chatInfo"]["teamInfo"]["teamName"]

    @pytest.mark.smoking
    @pytest.mark.chat
    @pytest.mark.dependency(depends=['pre'])
    @allure.story("修改群头像")
    @pytest.mark.run(order=3)
    def test_modify_group_photo(self, BUDGlobalArgs):
        chat_info = dict()
        rsp = BUDGlobalArgs.get("rsp", None)
        target_id = rsp["chatInfo"]["targetId"]
        team_id = rsp["chatInfo"]["teamInfo"]["teamId"]
        team_name = rsp["chatInfo"]["teamInfo"]["teamName"]
        chat_info["target_id"] = target_id
        chat_info["operation"] = 6
        chat_info["teamId"] = team_id
        chat_info["teamName"] = team_name
        r = self.chat.post_set_group(self.uid, chat_info)
        self.assert_api_success_code(r)
        self.assert_not_empty(r["data"], msg='r["data"]')
        self.assert_not_empty(r["data"]["chatInfo"], msg='r["data"]["chatInfo"]')
        self.assert_not_empty(r["data"]["chatInfo"]["teamInfo"]["teamPhoto"],
                              msg='r["data"]["chatInfo"]["teamInfo"]["teamPhoto"]')

    @pytest.mark.smoking
    @pytest.mark.chat
    @allure.story("邀请用户")
    @pytest.mark.run(order=4)
    def test_invite_to_group(self, BUDGlobalArgs):
        # 1.50版本后新接口
        # rsp = BUDGlobalArgs.get("rsp", None)
        # target_id = rsp["chatInfo"]["targetId"]
        # memberlist = self.members
        # r = self.chat.post_invite_group(self.uid, targetId=target_id, memberList=memberlist)
        # self.assert_result_is_zero(r)
        # r1 = self.chat.get_member_group_list(self.uid, targetId=target_id)
        # self.assert_api_success_code(r1)
        # self.assert_not_empty(r1["data"]["itemList"])
        # uid = []
        # for i in r1["data"]["itemList"]:  # 取出超级群成员列表内uid
        #     for x, v in i.items():
        #         if x == "userInfo":
        #             uid.append(v["uid"])
        # for a in self.members:
        #     self.assert_value_in(a, uid)
        chat_info = dict()
        rsp = BUDGlobalArgs.get("rsp", None)
        target_id = rsp["chatInfo"]["targetId"]
        team_id = rsp["chatInfo"]["teamInfo"]["teamId"]
        chat_info["target_id"] = target_id
        chat_info["teamId"] = team_id
        chat_info["operation"] = 3
        chat_info["members"] = self.members
        r = self.chat.post_set_group(self.uid, chat_info)  # 添加成员进超级群
        self.assert_api_success_code(r)
        self.assert_not_empty(r["data"]["chatInfo"], msg='r["data"]["chatInfo"]')
        self.assert_not_empty(r["data"]["chatInfo"]["targetId"], msg='r["data"]["chatInfo"]["targetId"]')
        self.assert_not_empty(r["data"]["chatInfo"]["teamInfo"]["teamId"], msg='r["data"]["chatInfo"]["teamInfo"]["teamId"]')
        targetId = r["data"]["chatInfo"]["targetId"]
        r1 = self.chat.get_subset_member_list(self.uid, targetId=targetId)  # 获取超级群成员列表
        self.assert_api_success_code(r1)
        self.assert_not_empty(r1["data"]["itemList"])
        uid = []
        for i in r1["data"]["itemList"]:  # 取出超级群成员列表内uid
            for x, v in i.items():
                if x == "userInfo":
                    uid.append(v["uid"])
        for a in self.members:
            self.assert_value_in(a, uid)   # 判断添加成功

    @pytest.mark.somking
    @pytest.mark.chat
    @allure.story("用户退群")
    @pytest.mark.run(order=5)
    def test_leave_group(self, BUDGlobalArgs):
        # rsp = BUDGlobalArgs.get("rsp", None)
        # target_id = rsp["chatInfo"]["targetId"]
        # r = self.chat.post_join_group(self.leave_members["uid"], token=self.leave_members["token"], targetId=target_id)
        # self.assert_result_is_zero(r)
        # r1 = self.chat.post_quit_group(self.leave_members["uid"], token=self.leave_members["token"], targetId=target_id)
        # self.assert_result_is_zero(r1)
        # r2 = self.chat.get_member_group_list(self.uid, targetId=target_id)
        # self.assert_api_success_code(r2)
        # self.assert_not_empty(r2["data"]["itemList"])
        # uid = []
        # for i in r2["data"]["itemList"]:  # 取出超级群成员列表内uid
        #     for x, v in i.items():
        #         if x == "userInfo":
        #             uid.append(v["uid"])
        # self.assert_value_not_in_seq(self.leave_members["uid"], uid)  # 判断退出成功
        chat_info = dict()
        rsp = BUDGlobalArgs.get("rsp", None)
        target_id = rsp["chatInfo"]["targetId"]
        team_id = rsp["chatInfo"]["teamInfo"]["teamId"]
        chat_info["target_id"] = target_id
        chat_info["teamId"] = team_id
        chat_info["operation"] = 3
        uid = self.leave_members["uid"]
        chat_info["members"] = [uid]
        r = self.chat.post_set_group(self.uid, chat_info)
        self.assert_api_success_code(r)
        chat_info["operation"] = 5
        r1 = self.chat.post_set_group(self.leave_members["uid"], chat_info, token=self.leave_members["token"])
        self.assert_api_success_code(r1)

    @pytest.mark.smoking
    @pytest.mark.chat
    @allure.story("踢出成员")
    @pytest.mark.run(order=6)
    def test_remove_to_group(self, BUDGlobalArgs):
        chat_info = dict()
        rsp = BUDGlobalArgs.get("rsp", None)
        target_id = rsp["chatInfo"]["targetId"]
        team_id = rsp["chatInfo"]["teamInfo"]["teamId"]
        chat_info["target_id"] = target_id
        chat_info["teamId"] = team_id
        chat_info["operation"] = 4
        chat_info["members"] = self.members
        r = self.chat.post_set_group(self.uid, chat_info)  # 移除刚入群成员
        self.assert_api_success_code(r)
        self.assert_not_empty(r["data"]["chatInfo"], msg='r["data"]["chatInfo"]')
        self.assert_not_empty(r["data"]["chatInfo"]["targetId"], msg='r["data"]["chatInfo"]["targetId"]')
        self.assert_not_empty(r["data"]["chatInfo"]["teamInfo"]["teamId"], msg='r["data"]["chatInfo"]["teamInfo"]["teamId"]')
        targetId = r["data"]["chatInfo"]["targetId"]
        r1 = self.chat.get_subset_member_list(self.uid, targetId=targetId)  # 获取超级群成员列表
        self.assert_api_success_code(r1)
        self.assert_not_empty(r1["data"]["itemList"])
        uid = []
        for i in r1["data"]["itemList"]:  # 取出超级群成员列表内uid
            for x, v in i.items():
                if x == "userInfo":
                    uid.append(v["uid"])
        for a in self.members:
            self.assert_not_value(a, uid)    # 判断移除成功

    @pytest.mark.smoking
    @pytest.mark.chat
    @pytest.mark.dependency(depends=['pre'])  # 明确指出denpends用例依赖与"pre"
    @allure.story("删除超级群")
    @pytest.mark.run(order=7)
    def test_del_group(self, BUDGlobalArgs):
        chat_info = dict()
        rsp = BUDGlobalArgs.get("rsp", None)
        target_id = rsp["chatInfo"]["targetId"]
        team_id = rsp["chatInfo"]["teamInfo"]["teamId"]
        team_name = rsp["chatInfo"]["teamInfo"]["teamName"]
        chat_info["target_id"] = target_id
        chat_info["operation"] = 1
        chat_info["teamName"] = team_name
        chat_info["teamId"] = team_id
        r2 = self.chat.post_set_group(self.uid, chat_info)  # 删除超级群
        self.assert_api_success_code(r2)
        self.assert_not_empty(r2["data"], msg='r2["data"]')
        self.assert_not_empty(r2["data"]["chatInfo"], msg='r2["data"]["chatInfo"]')
        self.assert_not_empty(r2["data"]["chatInfo"]["targetId"], msg='r2["data"]["chatInfo"]["targetId"]')
