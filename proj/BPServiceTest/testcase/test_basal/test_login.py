# -*- coding: utf-8 -*-
"""
@Author: shining
@File: test_login.py
@Date: 2022/4/11 4:21 下午
@Version: python 3.10
@Describe: 登录模块测试用例
"""
import allure
import pytest
from us_api_test.business.basal.login import Login
from us_api_test.business.user_info.image import Image
from us_api_test.config import Config
from us_api_test.flow.native.register_flow import RegisterFlow
from proj.BPServiceTest.testcase.service_test import ServiceTest


@allure.feature("登录模块")
class TestLogin(ServiceTest):

    def setup(self):

        self.login = Login()
        self.register_flow = RegisterFlow()
        self.user = Image()
        self.global_uid = Config.case_data('global_user_info.yml').uid

    @pytest.mark.smoking
    @pytest.mark.basal
    @allure.story("登录成功")
    def test_registered_user_login_success(self):
        allure.dynamic.title("已注册用户，正常登录成功")
        dm = Config.case_data("login.yml", "registered_user_login_success")
        open_id = dm.open_id
        r = self.login.login_v2(open_id=open_id, provider=dm.provider)
        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        self.assert_equal(str(r["data"]["userInfo"]["uid"]), str(dm.uid))
        self.assert_not_empty(r["data"]["userInfo"]["userName"])
        self.assert_not_empty(r["data"]["userInfo"]["imageJson"])
        self.assert_not_empty(r["data"]["token"])
        assert not r["data"]["newUser"]

    @pytest.mark.smoking
    @pytest.mark.basal
    @allure.story("新用户注册并登录成功")
    @pytest.mark.skip(reason="注销流程改版中，注销后不会立即生效")
    def test_register_flow(self):
        allure.dynamic.title("未注册用户，新手流程正常")
        info = Config.case_data_dict("login.yml", 'register_flow')

        uid, token = self.register_flow.register_flow(info)
        r = self.user.get_user_info(uid, uid, token=token)
        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        self.assert_not_empty(r["data"]["userInfo"]["imageJson"])
        self.assert_equal(str(r["data"]["userInfo"]["uid"]), str(uid))

    @pytest.mark.smoking
    @pytest.mark.basal
    @allure.story("注册流程")
    @pytest.mark.parametrize("uid,token", Config.case_data_dict("login.yml", "get_register_recommend"))
    def test_get_register_recommend_group(self, uid, token):
        allure.dynamic.title("获取推荐团体")

        r = self.login.get_register_recommend_group(uid, token=token)
        self.assert_api_success_code(r)
        team_infos = r['data'].get("teamInfos", None)
        if team_infos:
            self.assert_length_gt_zero(team_infos)
            team = team_infos[0]
            target_id = team.get('targetId', None)
            team_id = team.get('teamId', None)
            # self.assert_not_empty(team['targetId'], msg="team['targetId']")
            self.assert_any_not_empty([target_id, team_id])
            self.assert_not_empty(team['teamId'], msg="team['teamId']")
            self.assert_not_empty(team['teamName'], msg="team['teamName']")
            # self.assert_not_empty(team['teamDesc'], msg="team['teamDesc']") # 不校验teamDesc字段，此场景不需要返回
            self.assert_not_empty(str(team['onlineUserNum']), msg="team['onlineUserNum']")   # 断言 onlineUserNum字段

    @pytest.mark.smoking
    @pytest.mark.basal
    @allure.story("注册流程")
    @pytest.mark.parametrize("uid,token", Config.case_data_dict("login.yml", "get_register_recommend"))
    def test_get_register_recommend_creator(self, uid, token):
        allure.dynamic.title("获取推荐创作者列表")

        r = self.login.get_register_recommend_creator(uid, token=token)
        self.assert_api_success_code(r)
        creator_infos = r['data'].get("creatorInfos", None)
        self.assert_length_gt_zero(creator_infos)
        creator = creator_infos[0]
        self.assert_not_empty(creator['uid'], msg="creator['uid']")
        self.assert_not_empty(creator['userNick'], msg="creator['userNick']")
        self.assert_not_empty(creator['userName'], msg="creator['userName']")
        self.assert_not_empty(creator['portraitUrl'], msg="creator['portraitUrl']")

    @pytest.mark.smoking
    @pytest.mark.basal
    @allure.story("登录用户信息")
    def test_get_login_user_info(self):
        allure.dynamic.title("获取登录用户信息")
        r = self.login.get_login_user_info(self.global_uid)
        self.assert_api_success_code(r)
        self.assert_value_in(r['data']['needBindTripartite'], [True, False])



