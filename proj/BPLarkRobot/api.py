#! /usr/bin/env python3.8
import json
import os
import logging
import requests
from urllib import request

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")

# const
TENANT_ACCESS_TOKEN_URI = "/open-apis/auth/v3/tenant_access_token/internal"
MESSAGE_URI = "/open-apis/im/v1/messages"


class MessageApiClient(object):
    def __init__(self, app_id, app_secret, lark_host):
        self._app_id = app_id
        self._app_secret = app_secret
        self._lark_host = lark_host
        self._tenant_access_token = ""

    @property
    def tenant_access_token(self):
        return self._tenant_access_token

    def send_text_with_open_id(self, open_id, content):
        # "content": "{\"text\":\" test content\"}"
        self.send("open_id", open_id, "text", content)

    def send(self, receive_id_type, receive_id, msg_type, content):
        # send message to user, implemented based on Feishu open api capability. doc link: https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/create
        self._authorize_tenant_access_token()
        url = "{}{}?receive_id_type={}".format(
            self._lark_host, MESSAGE_URI, receive_id_type
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.tenant_access_token,
        }

        req_body = {
            "receive_id": receive_id,
            "content": content,
            "msg_type": msg_type,
        }
        resp = requests.post(url=url, headers=headers, json=req_body)
        MessageApiClient._check_error_response(resp)

    def reply(self, message_id, msg_type, content):

        self._authorize_tenant_access_token()
        url = "{}{}/{}/reply".format(
            self._lark_host, MESSAGE_URI, message_id
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.tenant_access_token,
        }

        req_body = {
            "content": content,
            "msg_type": msg_type,
        }
        resp = requests.post(url=url, headers=headers, json=req_body)
        MessageApiClient._check_error_response(resp)

    def send_message(self, event, payload):
        url = "https://open.feishu.cn/open-apis/im/v1/messages"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self._tenant_access_token
        }

        chat_type = event.get("chat_type", "")
        chat_id = event.get("open_chat_id", "")
        open_id = event.get("open_id", "")
        payload_type = "dict" if isinstance(payload, dict) else "str"

        req_body = dict()

        # 加群通知 add_bot
        if event.get("type", "add_bot"):
            if chat_id and payload_type == "dict":
                payload["chat_id"] = chat_id
            elif chat_id and payload_type == "str":
                req_body["chat_id"] = chat_id
            elif open_id and payload_type == "dict":
                payload["open_id"] = open_id
            elif open_id and payload_type == "str":
                req_body["open_id"] = open_id
        else:
            # 群聊或私聊
            if chat_type == "group" and payload_type == "dict":
                payload["chat_id"] = chat_id
            elif chat_type == "group" and payload_type == "str":
                req_body["chat_id"] = chat_id
            elif chat_type == "private" and payload_type == "dict":
                payload["open_id"] = open_id
            elif chat_type == "private" and payload_type == "str":
                req_body["open_id"] = open_id

        if payload_type == "str":
            # 文本
            req_body["msg_type"] = "text"
            req_body["content"] = {
                "text": payload
            }
        elif payload_type == "dict":
            req_body = payload
        else:
            print("[send_message] Error payload", payload)
            pass

        data = bytes(json.dumps(req_body), encoding='utf8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e.read().decode())
            return

        rsp_body = response.read().decode('utf-8')
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:
            print("send message error, code = ", code, ", msg =", rsp_dict.get("msg", ""))

    def _authorize_tenant_access_token(self):
        # get tenant_access_token and set, implemented based on Feishu open api capability. doc link: https://open.feishu.cn/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token_internal
        url = "{}{}".format(self._lark_host, TENANT_ACCESS_TOKEN_URI)
        print(url)
        req_body = {"app_id": self._app_id, "app_secret": self._app_secret}
        print(req_body)
        response = requests.post(url, req_body)
        print(response.json())
        MessageApiClient._check_error_response(response)
        self._tenant_access_token = response.json().get("tenant_access_token")

    @staticmethod
    def _check_error_response(resp):
        # check if the response contains error information
        if resp.status_code != 200:
            resp.raise_for_status()
        response_dict = resp.json()
        code = response_dict.get("code", -1)
        if code != 0:
            logging.error(response_dict)
            raise LarkException(code=code, msg=response_dict.get("msg"))


class LarkException(Exception):
    def __init__(self, code=0, msg=None):
        self.code = code
        self.msg = msg

    def __str__(self) -> str:
        return "{}:{}".format(self.code, self.msg)

    __repr__ = __str__


if __name__ == '__main__':
    ma = MessageApiClient("", "", "https://open.feishu.cn")
    ma._authorize_tenant_access_token()
    token = ma.tenant_access_token
    print(token)