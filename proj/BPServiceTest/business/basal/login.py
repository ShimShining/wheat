# -*- coding: utf-8 -*-
"""
@Author: shining
@File: login.py
@Date: 2021/12/30 3:38 下午
@Version: python 3.10
@Describe: 登录模块
"""
from proj.BPServiceTest.business.bp_service import BPService


class Login(BPService):

    def login_v2(self, **kwargs):
        """
        用户登录-登录新接口(分配UID优化)
        :param kwargs:
        :return:
        """
        path = ""
        name = "用户登录-登录新接口(分配UID优化)"
        h = {
        }
        req = self.handle_req_params(locals())
        # print(req)
        r = self.bp_post(req, **kwargs)
        return r.json()

    def get_register_recommend_group(self, uid, **kwargs):

        path = ""
        name = "新手注册-获取注册流程推荐团体列表"
        h = {"uid": uid}
        # print(locals())
        req = self.handle_req_params(locals())
        r = self.bp_get(req, **kwargs)
        return r.json()

    def get_register_recommend_creator(self, uid, **kwargs):

        path = ""
        name = "新手注册-获取注册流程推荐创作者列表"
        h = {"uid": uid}
        req = self.handle_req_params(locals())
        r = self.bud_get(req, **kwargs)
        return r.json()

    def get_login_user_info(self, uid, **kwargs):

        path = ""
        name = "获取用户登录信息"
        h = {"uid": uid}
        req = self.handle_req_params(locals())
        r = self.bud_get(req, **kwargs)
        return r.json()

    def get_newbie_village_step(self, uid, **kwargs):
        path = ""
        name = "获取用户登录信息"
        h = {"uid": uid}
        req = self.handle_req_params(locals())
        r = self.bud_get(req, **kwargs)
        return r.json()


if __name__ == '__main__':
    login = Login()
    login.get_register_recommend_creator('1111', open_id="aaa", token='bbbbb', version='1.99.0')
