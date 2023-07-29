# -*- coding: utf-8 -*-
"""
@Author: longyonghe
@File: chat.py
@Date: 2022/10/24 21:18
@Version: python 3.10
@Describe:
"""

import us_api_test.req_body.chat as req_pkg
from us_api_test.business.BUDUSApi import BUDUSApi
from utils.get_req_json import GetReqJson as g


class Chat(BUDUSApi):
    def post_chat_list_info(self, uid, chat_info, **kwargs):
        path = ""
        h = {
            "uid": uid

        }
        chat_info["uid"] = uid
        json = g.assemble_dict_req_body(pkg=req_pkg, json_file_name="get_chat_list_info", **chat_info)

        req = {
            "headers": h,
            'name': "获取单聊会话列表",
            "path": path,
            "json": json
        }
        r = self.bud_post(req, **kwargs)
        return r.json()

    def get_group_chat_list(self, uid, **kwargs):
        path = ""
        h = {
            "uid": uid
        }
        req = {
            "headers": h,
            "name": "获取超级群会话列表",
            "path": path
        }
        r = self.bud_get(req, **kwargs)
        return r.json()

    def post_set_group(self, uid, chat_info, **kwargs):
        path = ""
        h = {
            "uid": uid
        }
        chat_info["uid"] = uid
        json = g.assemble_dict_req_body(pkg=req_pkg, json_file_name="set_group", **chat_info)
        req = {
            "headers": h,
            "name": "设置超级群",
            "path": path,
            "json": json
        }
        r = self.bud_post(req, **kwargs)
        return r.json()

    def post_delete_group_members(self, uid, **kwargs):
        path = ""
        h = {
            'uid': uid
        }
        j = {
        }
        req = {
            "headers": h,
            "name": "删除超级群成员",
            "path": path,
            "json": j

        }
        r = self.bud_post(req, **kwargs)
        return r.json()

    def post_join_group(self, uid, **kwargs):
        path = ""
        h = {
            "uid": uid
        }
        params = {
        }
        req = {
            "headers": h,
            "path": path,
            "name": "加入超级群",
            "params": params
        }
        r = self.bud_post(req, **kwargs)
        return r.json()

    def post_invite_group(self, uid, **kwargs):
        path = ""
        h = {
            "uid": uid
        }
        params = {
        }
        req = {
            "headers": h,
            "path": path,
            "name": "邀请加入超级群",
            "params": params
        }
        r = self.bud_post(req, **kwargs)
        return r.json()

    def post_quit_group(self, uid, **kwargs):
        path = ""
        h = {
            "uid": uid
        }
        params = {
        }
        req = {
            "headers": h,
            "path": path,
            "name": "退出超级群",
            "params": params
        }
        r = self.bud_post(req, **kwargs)
        return r.json()

    def get_subset_member_list(self, uid, **kwargs):
        path = ""
        h = {
            "uid": uid
        }
        params = {
        }
        req = {
            "headers": h,
            "path": path,
            "name": "获取超级群成员列表",
            "params": params
        }
        r = self.bud_get(req, **kwargs)
        return r.json()

if __name__ == "__main__":
    c = Chat()
    chat_info = dict()
    chat_info['chat_type'] = 0  # 0单聊，1群聊，2queen公告，3超级群
    chat_info['target_id'] = ""

    s = c.post_chat_list_info("00000", chat_info)
