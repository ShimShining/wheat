# -*- coding: utf-8 -*-
"""
@Author: shining
@File: lark.py
@Date: 2022/5/25 7:31 下午
@Version: python 3.9
@Describe:
"""
import datetime
import requests
from config import Config


class Lark:

    def __init__(self, hook_url, token_url=None):
        super(Lark, self).__init__()
        self.hook_url = hook_url
        self.token_url = token_url

    def post_allure_report_url(self, env, job=None):

        # TODO url放在配置文件中读取

        if job:
            return ""
        report_url = ""
        if "MASTER" in env:
            return report_url
        if "ALPHA" in env:
            report_url = ""
        elif "PROD" in env:
            report_url = ""
        return report_url

    def handle_report_body(self, data, job=None):
        mod_fail_str = ''
        mod_error_str = ''
        if data.get("fail_mod", None) and data['fail_mod']:
            mod_fail_str = ",".join(data['fail_mod'])
        if data.get("error_mod", None) and data['error_mod']:
            mod_error_str = ",".join(data['error_mod'])
        report_url = self.post_allure_report_url(data['host'], job=job)
        request_body = {
            "msg_type": "interactive",
            "card": {
                "config": {
                    "wide_screen_mode": True
                },
                "elements": [
                    {
                        "fields": [
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**运行通过率**\n{data['success_rate']} %",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**用例总数**\n{data['total']}",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": False,
                                "text": {
                                    "content": "",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**📅 运行日期**\n{datetime.datetime.today().strftime('%Y-%m-%d')}",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**通过用例数**\n{data['passed']}",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": False,
                                "text": {
                                    "content": "",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**运行耗时**\n{data['duration']} 秒",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**失败用例数**\n{data['failed']}",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": False,
                                "text": {
                                    "content": "",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**error-用例数**\n{data['error']}",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**skip(deselected)用例数**\n{data['skipped']}({data['deselected'] })",
                                    "tag": "lark_md"
                                }
                            }
                        ],
                        "tag": "div"
                    },
                    {
                        "tag": "hr"
                    },
                    {
                        "actions": [
                            {
                                "tag": "button",
                                "text": {
                                    "content": "点击查看测试报告详情",
                                    "tag": "plain_text"
                                },
                                "type": "default",
                                "url": report_url
                            }
                        ],
                        "tag": "action"
                    }
                ],
                "header": {
                    "template": "b",
                    "title": {
                        "content": f"BUD-US {data['host']}-{data['platform']} P0 UI自动化运行结果同步",
                        "tag": "plain_text"
                    }
                }
            }}
        msg = []
        if mod_fail_str:
            fail_message = {
                "tag": "markdown",
                "content": f"失败用例模块: **{mod_fail_str}**",
            }
            msg.append(fail_message)
        if mod_error_str:
            error_message = {
                "tag": "markdown",
                "content": f"error用例模块: **{mod_error_str}**",
            }
            msg.append(error_message)
        for i, message in enumerate(msg):
            request_body['card']['elements'].insert(1+i, message)
        return request_body

    def send_report_to_lark(self, data, job=None):

        request_body = self.handle_report_body(data, job=job)
        headers = {
            "Content-Type": "application/json;charset=utf-8"
        }

        # print(request_body)
        req = {
            'url': self.hook_url,
            'method': 'POST',
            'headers': headers,
            'json': request_body
        }
        res = requests.request(**req)
        print(res.json())


if __name__ == "__main__":
    l = Lark(Config.DEBUG_WEB_HOOK_URL)
    data = []
    l.send_report_to_lark(data)
