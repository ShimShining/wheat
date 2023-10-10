# -*- coding: utf-8 -*-
"""
@Author: shining
@File: lark.py
@Date: 2022/2/13 10:14 下午
@Version: python 3.10
@Describe:lark robot base
"""
import requests

from config import Config


class Lark:

    def __init__(self, app_id=None, app_secret=None):

        self.app_id = app_id
        self.app_secret = app_secret

    def get_token(self):

        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        headers = {
            "Content-Type": "application/json; charset=utf-8"
        }
        body = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        r = requests.post(url, headers=headers, json=body)
        print(r.json())
        return r.json()["tenant_access_token"]

    def upload_iamge(self):

        pass

    def post_sec_info(self, info, unpack=False):

        res = ""
        for i in info:
            if i.isdigit():
                if unpack:
                    i = str(int(i) - 1)
                else:
                    i = str(int(i) + 1)
                res += i
                continue
            res += i
        return res

    def get_open_id_by_email_or_phone(self, emails=None, mobiles=None):

        res = dict()
        if emails is None and mobiles is None:
            return res
        # get_url = "https://open.feishu.cn/open-apis/user/v1/batch_get_id"
        contact_url = "https://open.feishu.cn/open-apis/contact/v3/users/batch_get_id"
        token = self.get_token()
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json; charset=utf-8"
        }
        params = dict()
        if emails:
            params['emails'] = emails
        if mobiles:
            params['mobiles'] = mobiles
        r = requests.post(url=contact_url, headers=headers, json=params)
        print(r.json())
        res["email_users"] = r.json()['data'].get("email_users", None)
        res["mobile_users"] = r.json()['data'].get("mobile_users", None)
        return res


if __name__ == "__main__":
    l = Lark(Config.APP_ID, Config.APP_SECRET)
    # r = l.get_token()
    email_list = ['']
    pm_emails = [""]
    # r = l.get_open_id_by_email_or_phone(emails=email_list)
    r = l.get_open_id_by_email_or_phone(emails=email_list)
    print(r)
