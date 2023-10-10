# -*- coding: utf-8 -*-
"""
@Author: shining
@File: ios_lark_bot.py
@Date: 2022/6/28 5:43 下午
@Version: python 3.9
@Describe:ios oom and crash rate index lark robot syn
"""
import time

import requests

from lark_bot.lark_bot import LarkBot


class IOSLarkBot(LarkBot):

    def send_to_lark(self, info):
        print(f"开始执行{time.time()}")
        m, dat = self.handle_date(info['dat'])
        dat = m + "月" + dat + '日'
        request_body = {
            "msg_type": "interactive",
            "card": {
                "config": {
                    "wide_screen_mode": True
                },
                "header": {
                    "title": {
                        "content": f"😈  昨日 {dat} BP-US-iOS OOM-Crash指标同步👉",
                        "tag": "plain_text"
                    },
                    "template": "red"
                },
                "i18n_elements": {
                    "zh_cn": [
                        {
                            "tag": "hr"
                        },
                        {
                            "fields": [
                                {
                                    "is_short": True,
                                    "text": {
                                        "content": f"**normal_crash_rate：**\n**{info['normal_crash_rate']}%"
                                                   f"（{info['normal_crash']:,}/{info['reboot_all']:,})**\n",
                                        "tag": "lark_md"
                                    }
                                },
                                {
                                    "is_short": True,
                                    "text": {
                                        "content": f"**foreground_oom_rate：**\n**{info['foreground_oom_rate']}%"
                                                   f"（{info['foreground_oom']:,}/{info['reboot_all']:,})**\n",
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
                            "fields": [
                                {
                                    "is_short": True,
                                    "text": {
                                        "content": f"**normal_crash次数前10机型：**\n**{info['crashs'][0][0]}: {int(info['crashs'][0][1]):,}**\n"
                                                   f"\n**{info['crashs'][1][0]}: {int(info['crashs'][1][1]):,}**\n"
                                                   f"\n**{info['crashs'][2][0]}: {int(info['crashs'][2][1]):,}**\n"
                                                   f"\n**{info['crashs'][3][0]}: {int(info['crashs'][3][1]):,}**\n"
                                                   f"\n**{info['crashs'][4][0]}: {int(info['crashs'][4][1]):,}**\n"
                                                   f"\n**{info['crashs'][5][0]}: {int(info['crashs'][5][1]):,}**\n"
                                                   f"\n**{info['crashs'][6][0]}: {int(info['crashs'][6][1]):,}**\n"
                                                   f"\n**{info['crashs'][7][0]}: {int(info['crashs'][7][1]):,}**\n"
                                                   f"\n**{info['crashs'][8][0]}: {int(info['crashs'][8][1]):,}**\n"
                                                   f"\n**{info['crashs'][9][0]}: {int(info['crashs'][9][1]):,}**\n",
                                        "tag": "lark_md"
                                    }
                                },
                                {
                                    "is_short": True,
                                    "text": {
                                        "content": f"**foreground_oom次数前10机型：**\n**{info['ooms'][0][0]}: {int(info['ooms'][0][1]):,}**\n"
                                                   f"\n**{info['ooms'][1][0]}: {int(info['ooms'][1][1]):,}**\n"
                                                   f"\n**{info['ooms'][2][0]}: {int(info['ooms'][2][1]):,}**\n"
                                                   f"\n**{info['ooms'][3][0]}: {int(info['ooms'][3][1]):,}**\n"
                                                   f"\n**{info['ooms'][4][0]}: {int(info['ooms'][4][1]):,}**\n"
                                                   f"\n**{info['ooms'][5][0]}: {int(info['ooms'][5][1]):,}**\n"
                                                   f"\n**{info['ooms'][6][0]}: {int(info['ooms'][6][1]):,}**\n"
                                                   f"\n**{info['ooms'][7][0]}: {int(info['ooms'][7][1]):,}**\n"
                                                   f"\n**{info['ooms'][8][0]}: {int(info['ooms'][8][1]):,}**\n"
                                                   f"\n**{info['ooms'][9][0]}: {int(info['ooms'][9][1]):,}**\n",
                                        "tag": "lark_md"
                                    }
                                }
                            ],
                            "tag": "div"
                        },

                    ]
                }
            }
        }
        headers = {
            "Content-Type": "application/json;charset=utf-8"
        }
        # print(request_body)
        print(f"start sync ios crash index============>{time.time()}")
        r = requests.post(self.hook_url, headers=headers, json=request_body)
        print(f"sync ios crash index done============>{time.time()}")
        print(r.json())
