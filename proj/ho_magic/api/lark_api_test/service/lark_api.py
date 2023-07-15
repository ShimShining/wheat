# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/7/15
Describe: 飞书基础API
"""
from proj.ho_magic.api.lark_api_test.read_config import ReadConfig
from proj.ho_magic.api.lark_api_test.service.api import Api


class LarkApi(Api):
    _base_url = ReadConfig.get_lark_api_base_url()
    __token_path = "/auth/v3/tenant_access_token/internal"

    def __init__(self, app_id="cli_a1a5914d54f99013", app_secret="anOniQndOyvmODm3FRN3jd17wfIUOOPx"):
        # 多个应用如何构造Token?
        super().__init__()
        self.token = None
        self.app_id = app_id
        self.app_secret = app_secret

    def get_token(self):

        if self.token is not None:
            self.logger.info(f"使用已有token={self.token}")
            return self.token

        data = {
            "method": "POST",
            "url": self._base_url + self.__token_path,
            "headers": {
                "Content-Type": "application/json; charset=utf-8"
            },
            "json": {
                "app_id": self.app_id,
                "app_secret": self.app_secret
            }

        }
        j = self.request(data)
        assert j["code"] == 0
        self.logger.info(f"第1次获取token成功,token={j['tenant_access_token']}")
        # todo 没有对self.token赋值 导致每次请求都重新获取,改成赋值后,如果token失效呢?怎么处理
        self.token = j["tenant_access_token"]
        return self.token

    def lark_request(self, request):

        if not request.get('headers'):
            request["headers"] = {
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {self.get_token()}"
            }
            self.logger.info(f"headers添加成功")

        j = self.request(request)
        assert j['code'] == 0
        return j

