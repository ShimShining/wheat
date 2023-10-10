# -*- coding: utf-8 -*-
"""
@Author: shining
@File: lark_bot.py
@Date: 2021/12/6 10:22 上午
@Version: python 3.10
@Describle: 飞书机器人配置
"""
import json
import time

import requests
from jira_lark_bot.config import *
from lark_bot.lark import Lark


class LarkBot(Lark):

    def __init__(self, hook_url, token_url=None):
        self.hook_url = hook_url
        self.token_url = token_url

    def handle_data(self, data):
        """
        todo 后面拆分下这个方法
        :param data:
        :return:
        """
        total_info = data['total_issues_info']
        total, todo, prog, review, t_closed = total_info['cur_total'], total_info['todo_num'], \
                                              total_info['progress_num'], total_info['review_num'], \
                                              total_info['closed_num']
        # 今日bug
        today_info = data['today_issues_info']
        cre, progr, fix, closed = today_info['today_create'], today_info['today_progress'], \
                                  today_info['today_fix'], today_info['today_closed']
        # android
        anr = data['end_issues_info']['android']
        anr_total, anr_todo, anr_pro, anr_rev, anr_cls, anr_t_c, anr_t_cls = anr['total'], anr['todo'], anr['progress'], \
                                                                             anr['review'], anr['closed'], anr[
                                                                                 'today_create'], anr['today_closed']

        # ios
        ios = data['end_issues_info']['ios']
        ios_total, ios_todo, ios_pro, ios_rev, ios_cls, ios_t_c, ios_t_cls = ios['total'], ios['todo'], ios['progress'], \
                                                                             ios['review'], ios['closed'], ios[
                                                                                 'today_create'], ios['today_closed']

        # backend
        backend = data['end_issues_info']['backend']
        backend_total, backend_todo, backend_pro, backend_rev, backend_cls, backend_t_c, backend_t_cls = \
            backend['total'], backend['todo'], backend['progress'], backend['review'], \
            backend['closed'], backend['today_create'], backend['today_closed']
        # unity 3D
        u3d = data['end_issues_info']['u3d']
        u3d_total, u3d_todo, u3d_pro, u3d_rev, u3d_cls, u3d_t_c, u3d_t_cls = u3d['total'], u3d['todo'], u3d['progress'], \
                                                                             u3d['review'], u3d['closed'], u3d[
                                                                                 'today_create'], u3d['today_closed']
        # 其他
        oth = data['end_issues_info']['oth']
        oth_total, oth_todo, oth_pro, oth_rev, oth_cls, oth_t_c, oth_t_cls = oth['total'], oth['todo'], oth['progress'], \
                                                                             oth['review'], oth['closed'], oth[
                                                                                 'today_create'], oth['today_closed']
        # engine

        engine = data['end_issues_info']['engine']
        engine_total, engine_todo, engine_pro, engine_rev, engine_cls, engine_t_c, engine_t_cls = engine['total'], \
                                                                                                  engine['todo'], \
                                                                                                  engine['progress'], \
                                                                                                  engine['review'], \
                                                                                                  engine['closed'], \
                                                                                                  engine[
                                                                                                      'today_create'], \
                                                                                                  engine['today_closed']
        # default 暂时不做
        # Carmine，Violet
        template_color = "purple"
        if "Alpha" in data['sprint_name']:
            template_color = "Carmine"
        request_body = {

            "msg_type": "interactive",
            "card": {

                "config": {

                    "wide_screen_mode": True,
                    "enable_forward": True
                },
                "elements": [{

                    "tag": "div",
                    "text": {

                        "content": f"**版本Bug总览**：【总数：{total}，待办：{todo}，处理中： {prog}，Review中: {review}, 已关闭：{t_closed}】\n"
                                   f"**今日Bug概况**：【新增：{cre}，处理中：{progr}，已修复：{fix}，关闭：{closed}】\n",
                        "tag": "lark_md"
                    }
                },
                    {
                        "tag": "hr"
                    },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"**安卓缺陷总览**：【总数：{anr_total}, 待办：{anr_todo}，处理中： {anr_pro}，Review中: {anr_rev}, "
                                       f"已关闭：{anr_cls}, 今日新增：{anr_t_c}, 今日关闭：{anr_t_cls}】\n"
                                       f"**iOS缺陷总览**：【总数：{ios_total}, 待办：{ios_todo}，处理中： {ios_pro}，Review中: {ios_rev}, "
                                       f"已关闭：{ios_cls}, 今日新增：{ios_t_c}, 今日关闭：{ios_t_cls}】\n",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "hr"
                    },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"**U3D问题总览**：【总数：{u3d_total}, 待办：{u3d_todo}，处理中： {u3d_pro}，Review中: {u3d_rev}, "
                                       f"已关闭：{u3d_cls}, 今日新增：{u3d_t_c}, 今日关闭：{u3d_t_cls}】\n",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "hr"
                    },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"**后端问题总览**：【总数：{backend_total}, 待办：{backend_todo}，处理中： {backend_pro}，Review中: {backend_rev}, "
                                       f"已关闭：{backend_cls}, 今日新增：{backend_t_c}, 今日关闭：{backend_t_cls}】",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "hr"
                    },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"**联机问题总览**：【总数：{engine_total}, 代办：{engine_todo}，处理中： {engine_pro}，Review中: {engine_rev}, "
                                       f"已关闭：{engine_cls}, 今日新增：{engine_t_c}, 今日关闭：{engine_t_cls}】",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "hr"
                    },
                    {
                        "actions": [{

                            "tag": "button",
                            "text": {

                                "content": "**点击查看JIRA-BUG冲刺看板**",
                                "tag": "lark_md"
                            },
                            "url": f"{data['board_url']}",
                            "type": "default",
                            "value": {
                            }
                        }],
                        "tag": "action"
                    },
                    {
                        "tag": "hr"
                    },
                    {
                        "actions": [{

                            "tag": "button",
                            "text": {

                                "content": "**点击查看JIRA-BUG数据统计面板**",
                                "tag": "lark_md"
                            },
                            "url": f"{data['statistics_analysis_board']}",
                            "type": "default",
                            "value": {
                            }
                        }],
                        "tag": "action"
                    }
                ],
                "header": {

                    "title": {

                        "content": f"🐛 {data['project_name']}本：迭代 {data['sprint_name']} 今日bug情况",
                        "tag": "plain_text"
                    },
                    "template": f"{template_color}"
                }
            }
        }
        if oth_total or oth_todo or oth_pro or oth_rev or oth_cls or oth_t_c or oth_t_cls:
            request_body["card"]["elements"].insert(9, {"tag": "hr"})
            data = {
                "tag": "div",
                "text": {

                    "content": f"**其他端问题总览**：【总数：{oth_total}, 待办：{oth_todo}，处理中： "
                               f"{oth_pro}，Review中: {oth_rev}, "
                               f"已关闭：{oth_cls}, 今日新增：{oth_t_c}, 今日关闭：{oth_t_cls}】",
                    "tag": "lark_md"
                }
            }
            request_body["card"]["elements"].insert(10, data)
        return request_body

    def get_tenant_access_token(self, app_info):
        """
        获取上传token
        :param app_info:
        :return:
        """
        headers = {"Content-Type": "application/json"}
        data = {
            "app_id": app_info['app_id'],
            "app_secret": app_info['app_secret']

        }
        request = requests.post(url=self.token_url, headers=headers, json=data)
        response = json.loads(request.content)['tenant_access_token']
        return response

    def get_chat_id(self, tenant_access_token):
        # 获取chatid
        chat_url = "https://open.feishu.cn/open-apis/chat/v4/list?page_size=20"
        headers = {"Authorization": "Bearer %s" % tenant_access_token, "Content-Type": "application/json"}
        request = requests.get(url=chat_url, headers=headers)
        response = json.loads(request.content)['data']['groups'][0]['chat_id']
        return response

    def upload_img(self, graph_name, app_id=None, app_secret=None):
        with open(graph_name, 'rb') as f:
            image = f.read()
        img_url = 'https://open.feishu.cn/open-apis/image/v4/put/'
        headers = {'Authorization': "Bearer %s" % self.get_token(app_id=app_id, app_secret=app_secret)}
        files = {
            "image": image
        }
        data = {
            "image_type": "message"
        }

        resp = requests.post(
            url=img_url,
            headers=headers,
            files=files,
            data=data)
        resp.raise_for_status()
        content = resp.json()
        return content['data']['image_key']

    def send_notification(self, content):
        headers = {
            "Content-Type": "application/json;charset=utf-8"
        }
        body = self.handle_data(content)
        requests.post(self.hook_url, headers=headers, json=body)

    def send_mes_with_image(self, user_id, chat_id, tenant_access_token, image_key, msg):
        send_url = "https://open.feishu.cn/open-apis/message/v4/send/"
        headers = {"Authorization": "Bearer %s" % tenant_access_token, "Content-Type": "application/json"}
        # 向群里发送富文本消息
        subject, messages = msg
        data = {
            "chat_id": chat_id,
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": subject,
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "un_escape": True,
                                    "text": messages
                                },
                                {
                                    "tag": "at",
                                    "user_id": user_id

                                }
                            ],
                            [
                                {
                                    "tag": "img",
                                    "image_key": image_key,
                                    "width": 700,
                                    "height": 400
                                }
                            ]
                        ]
                    }
                }
            }
        }

        request = requests.post(url=send_url, headers=headers, json=data)
        print(request.content)

    def handle_ctop_send_content(self, info, app_version):

        success, total, rate = info
        d, version, env = app_version
        rate = str(round(rate * 100, 2)) + "%"
        success = format(success, ',')
        total_format = format(total, ',')
        m, dat = self.handle_date(d)
        d = m + "月" + dat + "日"
        placeholder = (len(d) + 8) * " "
        version_content = f"**BP版本 {version} {env}** "
        if int(total) <= 0:
            rate_content = f"{d} 成  功  率:  0.00% \n" \
                           f"{placeholder} 成功进房量:  {success}\n" \
                           f"{placeholder} 样本   总量:  {total_format}"
        else:
            rate_content = f"{d} 成    功   率:  {rate}\n" \
                           f"{placeholder} 成功进房量:  {success}\n" \
                           f"{placeholder} 样本    总量:  {total_format}"

        return version_content, rate_content

    def send_click_to_play_rate(self, prod_info, alpha_info, app_version, yesterday_info=None):

        prod_version, alpha_version = app_version
        prod_version_content, prod_rate_content = self.handle_ctop_send_content(prod_info, prod_version)
        alpha_version_content, alpha_rate_content = self.handle_ctop_send_content(alpha_info, alpha_version)
        request_body = {
            "msg_type": "interactive",
            "card": {

                "config": {

                    "wide_screen_mode": True,
                    "enable_forward": True
                },
                "elements": [{

                    "tag": "div",
                    "text": {

                        "content": "**计算方式**：unity_startFrameStep_recv / BP_call_unity",
                        "tag": "lark_md"
                    }
                },
                    {
                        "tag": "hr"
                    },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"{prod_version_content} ",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"{prod_rate_content}",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "hr"
                    },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"{alpha_version_content} ",
                            "tag": "lark_md"
                        }
                    },
                    # {
                    #     "tag": "hr"
                    # },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"{alpha_rate_content}",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "hr"
                    },
                ],
                "header": {

                    "title": {

                        "content": "😈  今日BP-US联机进房成功率指标clickToPlay同步",
                        "tag": "plain_text"
                    },
                    "template": "purple"
                }
            }
        }
        # print(request_body)
        if yesterday_info:
            yes_prod, yes_alpha = yesterday_info[0], yesterday_info[1]
            request_body = self.handle_other_day_data(request_body, yes_prod, yes_alpha, yesterday_info[4])

        headers = {
            "Content-Type": "application/json;charset=utf-8"
        }
        requests.post(self.hook_url, headers=headers, json=request_body)

    def handle_avg_fps_send_content(self, info, app_version):

        avg_fps, total = info
        d, version, env = app_version
        avg_fps = round(avg_fps, 2)
        total_format = format(total, ',')
        m, dat = self.handle_date(d)
        d = m + "月" + dat + "日"
        version_content = f"**BP版本 {version} {env}** "
        placeholder = (len(d) + 8) * " "
        if int(total) <= 0:
            fps_content = f"{d} 平均FPS：0 \n" \
                          f"{placeholder} 样本总量：{total_format}"
        else:
            fps_content = f"{d} 平均FPS：{avg_fps}\n" \
                          f"{placeholder} 样本总量：{total_format}"
        return version_content, fps_content

    def send_map_play_avg_fps(self, prod_info, alpha_info, app_version, yesterday_info=None):

        prod_version, alpha_version = app_version
        prod_version_content, prod_fps_content = self.handle_avg_fps_send_content(prod_info, prod_version)
        alpha_version_content, alpha_fps_content = self.handle_avg_fps_send_content(alpha_info, alpha_version)
        request_body = {
            "msg_type": "interactive",
            "card": {

                "config": {

                    "wide_screen_mode": True,
                    "enable_forward": True
                },
                "elements": [{

                    "tag": "div",
                    "text": {

                        "content": "**计算方式**：unity_avg_fps: avg（sum(unity_avg_fps.fps))",
                        "tag": "lark_md"
                    }
                },
                    {
                        "tag": "hr"
                    },
                    {
                        "tag": "div",
                        "text": {
                            "content": f"{prod_version_content} ",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"{prod_fps_content}",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "hr"
                    },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"{alpha_version_content} ",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "div",
                        "text": {

                            "content": f"{alpha_fps_content}",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "hr"
                    },
                ],
                "header": {
                    "title": {
                        "content": "😈  今日BP-US-U3D场景游玩平均FPS指标同步",
                        "tag": "plain_text"
                    },
                    "template": "purple"
                }
            }
        }
        # print(request_body)
        if yesterday_info:
            yes_prod, yes_alpha = yesterday_info[2], yesterday_info[3]
            request_body = self.handle_other_day_data(request_body, yes_prod, yes_alpha, yesterday_info[4], index=None)
        headers = {
            "Content-Type": "application/json;charset=utf-8"
        }
        requests.post(self.hook_url, headers=headers, json=request_body)

    def handle_other_day_data(self, req, prod, alpha, version, index="ctop"):

        yes_prod_version, yes_alpha_version = version
        if index == "ctop":
            _, yes_prod_rate_content = self.handle_ctop_send_content(prod, yes_prod_version)
            _, yes_alpha_rate_content = self.handle_ctop_send_content(alpha, yes_alpha_version)
        else:
            _, yes_prod_rate_content = self.handle_avg_fps_send_content(prod, yes_prod_version)
            _, yes_alpha_rate_content = self.handle_avg_fps_send_content(alpha, yes_alpha_version)
        req["card"]["elements"].insert(4, {"tag": "hr"})
        data_prod = {
            "tag": "div",
            "text": {

                "content": f"{yes_prod_rate_content}",
                "tag": "lark_md"
            }
        }
        req["card"]["elements"].insert(5, data_prod)
        req["card"]["elements"].insert(9, {"tag": "hr"})
        data_alpha = {
            "tag": "div",
            "text": {

                "content": f"{yes_alpha_rate_content}",
                "tag": "lark_md"
            }
        }
        req["card"]["elements"].insert(10, data_alpha)
        return req

    def handle_date(self, d):

        if int(d[4]) == 0:
            m = d[5]
        else:
            m = d[4:6]
        if int(d[6]) == 0:
            dat = d[7]
        else:
            dat = d[6:]
        return m, dat

    def handle_offline_single_version_interact_card(self, info):

        m, dat = self.handle_date(info['dat'])
        dat = m + "月" + dat + '日'
        card_template = [
            {
                "tag": "hr"
            },
            {
                "tag": "div",
                "text": {
                    "content": f"**{dat} 版本{info['version']}  {info['env']}** ",
                    "tag": "lark_md"
                }
            },
            {
                "fields": [
                    {
                        "is_short": True,
                        "text": {
                            "content": f"**总平均FPS(30满帧 | 60满帧)：**\n**{info['avg_fps']}({info['avg_fps30']}|{info['avg_fps60']})**\n",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "is_short": True,
                        "text": {
                            "content": f"**总FPS样本量(30满帧 | 60满帧)：**\n**{info['total_fps']:,}({info['total_fps30']:,}|{info['total_fps60']:,})**\n",
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
                            "content": f"**cToPlayLatency均耗时：**\n**{round(info['enter_time'], 2)} 秒**\n",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "is_short": True,
                        "text": {
                            "content": f"**总体样本量 ：**\n**{info['total_enter']:,}**\n",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "is_short": False,
                        "text": {
                            "content": "",
                            "tag": "lark_md"
                        }
                    }
                    # {
                    #     "is_short": True,
                    #     "text": {
                    #         "content": f"**总体ab替换平均耗时：**\n**{info['ab_time']} 秒**\n",
                    #         "tag": "lark_md"
                    #     }
                    # },
                    # {
                    #     "is_short": True,
                    #     "text": {
                    #         "content": f"**总体ab样本量：**\n**{info['total_ab']:,}**\n",
                    #         "tag": "lark_md"
                    #     }
                    # }
                ],
                "tag": "div"
            },
            {
                "tag": "hr"
            },
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "安卓/ios cToPlayLatency均耗时 || 样本量==>"
                },
                "extra": {
                    "tag": "overflow",
                    "options": [
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"安卓：{round(info['android_enter_time'], 2)} 秒 || {info['android_total_enter']:,}"
                            },
                            "value": "document"
                        },
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"iOS：{round(info['ios_enter_time'], 2)} 秒 || {info['ios_total_enter']:,}",
                            },
                            "value": "document"}]
                }},
            {
                "tag": "hr"
            },
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "安卓/ios均FPS(总/30/60) || 样本量==>"
                },
                "extra": {
                    "tag": "overflow",
                    "options": [
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"安卓：{info['android_avg_fps']} || {info['android_total_fps']:,}"
                            },
                            "value": "document"
                        },
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"安卓30：{info['android_avg_fps30']} || {info['android_total_fps30']:,}"
                            },
                            "value": "document"
                        },
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"安卓60：{info['android_avg_fps60']} || {info['android_total_fps60']:,}"
                            },
                            "value": "document"
                        },
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"iOS：{info['ios_avg_fps']} || {info['ios_total_fps']:,}",
                            },
                            "value": "document"},
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"iOS30：{info['ios_avg_fp30s']} || {info['ios_total_fps30']:,}",
                            },
                            "value": "document"},
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"iOS60：{info['ios_avg_fp60s']} || {info['ios_total_fps60']:,}",
                            },
                            "value": "document"}
                    ]
                }},
            {
                "tag": "hr"
            },
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "总/安卓/ios 编辑器均FPS || 样本量==>"
                },
                "extra": {
                    "tag": "overflow",
                    "options": [
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"总：{info['editor_avg_fps']} || {info['editor_total_fps']:,}"
                            },
                            "value": "document"
                        },
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"安卓：{info['editor_android_avg_fps']} || {info['editor_android_total_fps']:,}"
                            },
                            "value": "document"
                        },
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"iOS：{info['editor_ios_avg_fps']} || {info['editor_ios_total_fps']:,}",
                            },
                            "value": "document"}]
                }}
            # {
            #     "tag": "hr"
            # },
            # {
            #     "tag": "div",
            #     "text": {
            #         "tag": "lark_md",
            #         "content": "安卓/ios ab替换均耗时 || 样本量==>"
            #     },
            #     "extra": {
            #         "tag": "overflow",
            #         "options": [
            #             {
            #                 "text": {
            #                     "tag": "plain_text",
            #                     "content": f"安卓：{info['android_ab_time']} 秒 || {info['android_total_ab']:,}"
            #                 },
            #                 "value": "document"
            #             },
            #             {
            #                 "text": {
            #                     "tag": "plain_text",
            #                     "content": f"iOS：{info['ios_ab_time']} 秒 || {info['ios_total_ab']:,}",
            #                 },
            #                 "value": "document"}]
            #     }}
        ]
        return card_template

    def send_offline_index(self, prod_info, alpha_info, yesterday_info=None):

        request_body = {
            "msg_type": "interactive",
            "card": {
                "config": {
                    "wide_screen_mode": True
                },
                "header": {
                    "title": {
                        "content": "😈  今日BP-US-U3D场景游玩平均FPS指标同步 👉",
                        "tag": "plain_text"
                    },
                    "template": "purple"
                },
                "i18n_elements": {
                    "zh_cn": [
                        {
                            "tag": "hr"
                        },
                        {
                            "tag": "div",
                            "text": {
                                "content": "**计算方式**\n• 平均FPS：unity_avg_fps: avg（sum(unity_avg_fps.fps))\n• "
                                           "clickToPlayLatency平均耗时（两个埋点时间戳相减求和后平均）：\navg(sum(unity_startFrameStep_recv - "
                                           "BP_call_unity))\n• 平均ab加载时长（两个埋点时间戳相减求和后平均）："
                                           "\navg(sum(unity_endOffline - unity_startOffline))",
                                "tag": "lark_md"
                            }
                        },
                        {
                            "tag": "hr"
                        },
                        {
                            "actions": [{

                                "tag": "button",
                                "text": {
                                    "content": "**点击可进入飞书文档查看相关指标计算SQL**",
                                    "tag": "lark_md"
                                },
                                "url": "",
                                "type": "default",
                                "value": {
                                }
                            }],
                            "tag": "action"
                        }
                    ]
                }
            }
        }
        today_prod_offline_card = self.handle_offline_single_version_interact_card(prod_info)
        today_alpha_offline_card = self.handle_offline_single_version_interact_card(alpha_info)
        for i in range(len(today_prod_offline_card)):
            request_body['card']['i18n_elements']['zh_cn'].insert(i, today_prod_offline_card[i])
        index_prod = len(request_body['card']['i18n_elements']['zh_cn']) - 4
        for i, item in enumerate(today_alpha_offline_card):
            request_body['card']['i18n_elements']['zh_cn'].insert(i + index_prod, item)

        if yesterday_info:

            yes_prod, yes_alpha = yesterday_info[0], yesterday_info[1]
            yes_prod_offline_card = self.handle_offline_single_version_interact_card(yes_prod)
            yes_alpha_offline_card = self.handle_offline_single_version_interact_card(yes_alpha)
            yes_prod_index = len(request_body['card']['i18n_elements']['zh_cn']) - 4
            for i, item in enumerate(yes_prod_offline_card):
                request_body['card']['i18n_elements']['zh_cn'].insert(i + yes_prod_index, item)
            yes_alpha_index = len(request_body['card']['i18n_elements']['zh_cn']) - 4
            for i, item in enumerate(yes_alpha_offline_card):
                request_body['card']['i18n_elements']['zh_cn'].insert(i + yes_alpha_index, item)
        headers = {
            "Content-Type": "application/json;charset=utf-8"
        }
        # print(request_body)
        print(f"requst_body assemble done，start send to lark. time = [{time.time()}]")
        r = requests.post(self.hook_url, headers=headers, json=request_body)
        print(r.json())
        print(f"lark sync done. time = [{time.time()}]")

    def handle_single_version_engine_rate(self, info: dict):

        m, dat = self.handle_date(info['dat'])
        dat = m + "月" + dat + '日'
        total_zombie_rate = round(info['total_success_rate'] - info['total_success_exit_rate'], 2) \
            if round(info['total_success_rate'] - info['total_success_exit_rate'], 2) >= 0 else 0.0
        android_zombie_rate = round(info['android_success_rate'] - info['android_success_exit_rate'], 2) \
            if round(info['android_success_rate'] - info['android_success_exit_rate'], 2) >= 0 else 0.0
        ios_zombie_rate = round(info['ios_success_rate'] - info['ios_success_exit_rate'], 2) \
            if round(info['ios_success_rate'] - info['ios_success_exit_rate'], 2) >= 0 else 0.0
        card_template = [
            {
                "tag": "hr"
            },
            {
                "tag": "div",
                "text": {
                    "content": f"**{dat} 版本{info['version']}  {info['env']}** ",
                    "tag": "lark_md"
                }
            },
            # exclude_quit_total_success_rate, exclude_quit_android_success_rate, exclude_quit_ios_success_rate
            {
                "fields": [
                    {
                        "is_short": True,
                        "text": {
                            "content": f"成功率(退房成功率|僵尸率)：\n**{info['total_success_rate']}%"
                                       f"（{info['total_success_exit_rate']}% | "
                                       f"{total_zombie_rate}%)**\n"
                                       f"进房量减掉quit：**{info['exclude_quit_total_success_rate']}%**\n",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "is_short": True,
                        "text": {
                            "content": f"成功进房量(quit量/总样本量)：\n**{info['success_enter']:,}({info['total_quit']:,}/{info['total_enter']:,})**\n",
                            "tag": "lark_md"
                        }
                    }
                ],
                "tag": "div"
            },
            {
                "fields": [
                    {
                        "is_short": True,
                        "text": {
                            "content": f"**平均ping值（样本量）**：\n**{info['avg_ping']} ms"
                                       f"({info['total']:,})**",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "is_short": True,
                        "text": {
                            "content": f"**ping值区间百分比分布**：\n**[0,100]:{info['lt100_ms_rate']}% | (100, 200]:{info['gt100_le200_ms_rate']}%**\n"
                                       f"\n**(200,300]:{info['gt200_le300_ms_rate']}% | (300, inf]:{info['gt300_ms_rate']}%**",
                            "tag": "lark_md"
                        }
                    }
                ],
                "tag": "div"
            },
            # {
            #     "fields": [
            #         {
            #             "is_short": True,
            #             "text": {
            #                 "content": f"cToPlayLatency均耗时：\n**{round(info['ctop_cost'], 2)} 秒**\n",
            #                 "tag": "lark_md"
            #             }
            #         },
            #         {
            #             "is_short": True,
            #             "text": {
            #                 "content": f"总样本量 ：\n**{info['total_click']:,}**\n",
            #                 "tag": "lark_md"
            #             }
            #         },
            #     ],
            #     "tag": "div"
            # },
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "安卓/ios成功率(退房成功率|僵尸率)| 成功进房量/quit量/进房量=>"
                },
                "extra": {
                    "tag": "overflow",
                    "options": [
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"安卓:{info['android_success_rate']}%({info['exclude_quit_android_success_rate']}%)"
                                           f"（{info['android_success_exit_rate']}%|"
                                           f"{android_zombie_rate}%)|{info['android_success_enter']:,}/{info['android_quit']:,}/{info['android_total_enter']:,}"
                            },
                            "value": "document"
                        },
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"iOS：{info['ios_success_rate']}%({info['exclude_quit_ios_success_rate']}%)"
                                           f"（{info['ios_success_exit_rate']}% | "
                                           f"{ios_zombie_rate}%)|{info['ios_success_enter']:,}/{info['ios_quit']:,}/{info['ios_total_enter']:,}"
                            },
                            "value": "document"}]
                }},
            {
                "tag": "hr"
            },
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "总/安卓/ios rmCodeToPlay总成功率 || 成功进房量/进房量==>"
                },
                "extra": {
                    "tag": "overflow",
                    "options": [
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"总:{info['rc_success_rate']}% || "
                                           f"{info['room_success_enter']:,}/{info['total_room_enter']:,}"
                            },
                            "value": "document"
                        },
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"安卓:{info['android_rc_success_rate']}% || "
                                           f"{info['android_room_success_enter']:,}/{info['android_total_room_enter']:,}"
                            },
                            "value": "document"},
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"iOS:{info['ios_rc_success_rate']}% || "
                                           f"{info['ios_room_success_enter']:,}/{info['ios_total_room_enter']:,}"
                            },
                            "value": "document"}
                    ]
                }},
            {
                "tag": "hr"
            },
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": "安卓/ios 平均ping值 || 样本量==>"
                },
                "extra": {
                    "tag": "overflow",
                    "options": [
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"安卓：{round(info['android_avg_ping'], 2)}ms || "
                                           f"{info['android_total']:,} "
                            },
                            "value": "document"
                        },
                        {
                            "text": {
                                "tag": "plain_text",
                                "content": f"iOS：{round(info['ios_avg_ping'], 2)}ms || "
                                           f"{info['ios_total']:,} "
                            },
                            "value": "string",
                        }]
                }}
            # {
            #     "tag": "div",
            #     "text": {
            #         "tag": "lark_md",
            #         "content": "安卓/ios cToPlayLatency || 进房量==>"
            #     },
            #     "extra": {
            #         "tag": "overflow",
            #         "options": [
            #             {
            #                 "text": {
            #                     "tag": "plain_text",
            #                     "content": f"安卓：{round(info['android_ctop_cost'], 2)}秒 || "
            #                                f"{info['android_total_click']:,} "
            #                 },
            #                 "value": "document"
            #             },
            #             {
            #                 "text": {
            #                     "tag": "plain_text",
            #                     "content": f"iOS：{round(info['ios_ctop_cost'], 2)}秒 || "
            #                                f"{info['ios_total_click']:,} "
            #                 },
            #                 "value": "string",
            #             }]
            #     }}
        ]
        region_distribute = {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": "SA-region平均ping值==>"
            },
            "extra": {
                "tag": "overflow",
                "options": [
                    {
                        "text": {
                            "tag": "plain_text",
                            "content": f"菲律宾：{round(info['filipino_avg_ping'], 2)}ms"
                        },
                        "value": "document"
                    },
                    {
                        "text": {
                            "tag": "plain_text",
                            "content": f"印尼：{round(info['indonesian_avg_ping'], 2)}ms"
                        },
                        "value": "document"
                    },
                    {
                        "text": {
                            "tag": "plain_text",
                            "content": f"越南：{round(info['vietnam_avg_ping'], 2)}ms"
                        },
                        "value": "document"
                    }, {
                        "text": {
                            "tag": "plain_text",
                            "content": f"墨西哥：{round(info['mexico_avg_ping'], 2)}ms"
                        },
                        "value": "document"
                    }, {
                        "text": {
                            "tag": "plain_text",
                            "content": f"巴西：{round(info['brazil_avg_ping'], 2)}ms"
                        },
                        "value": "document"
                    }, {
                        "text": {
                            "tag": "plain_text",
                            "content": f"美国：{round(info['us_avg_ping'], 2)}ms"
                        },
                        "value": "document"
                    },
                ]
            }}
        if info['env'] == 'prod':
            length = len(card_template)
            card_template.insert(length - 2, region_distribute)
            # health_rate, prop_success_rate, total_game_count, bad_game_count, total_prop_count, failed_prop_count
            health_rate = {
                "fields": [
                    {
                        "is_short": True,
                        "text": {
                            "content": f"**房间健康度(24h内)(正常数/总房间数)**：\n**{round(info['health_rate'], 2)}%**\n"
                                       f"\n**({info['total_game_count'] - info['bad_game_count']:,}/{info['total_game_count']:,})**\n",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "is_short": True,
                        "text": {
                            "content": f"**道具成功率(24h内)(成功数/总次数)**：\n**{round(info['prop_success_rate'], 2)}%**\n"
                                       f"\n**({info['total_prop_count'] - info['failed_prop_count']:,}/{info['total_prop_count']:,})**\n",
                            "tag": "lark_md"
                        }
                    },
                ],
                "tag": "div"
            }
            card_template.insert(4, health_rate)
        if info['env'] == 'alpha':
            card_template.pop(0)
        return card_template

    def send_engine_index(self, prod_info, alpha_info, yesterday_info=None):
        """
        发送联机相关指标
        :param prod_info:
        :param alpha_info:
        :param app_version:
        :param yesterday_info:
        :return:
        """

        request_body = {
            "msg_type": "interactive",
            "card": {
                "config": {
                    "wide_screen_mode": True
                },
                "header": {
                    "title": {
                        "content": "😈 今日BP-US联机进房成功率指标同步 👉",
                        "tag": "plain_text"
                    },
                    "template": "purple"
                },
                "i18n_elements": {
                    "zh_cn": [
                        {
                            "tag": "hr"
                        },
                        {
                            "tag": "hr"
                        },
                        {
                            "tag": "div",
                            "text": {
                                "content": "**计算方式**\n• 成功率: (unity_enterRoom_rsp / BP_call_unity) * 100%\n"
                                           "• clickToPlayLatency平均耗时（两个埋点时间戳相减求和后平均）：\n"
                                           "avg(sum(unity_startFrameStep_recv - BP_call_unity))",
                                "tag": "lark_md"
                            }
                        },
                        {
                            "tag": "hr"
                        },
                        {
                            "actions": [{

                                "tag": "button",
                                "text": {
                                    "content": "**点击可进入飞书文档查看相关指标计算SQL**",
                                    "tag": "lark_md"
                                },
                                "url": "",
                                "type": "default",
                                "value": {
                                }
                            }],
                            "tag": "action"
                        }
                    ]
                }
            }
        }
        today_prod_engine_card = self.handle_single_version_engine_rate(prod_info)
        today_alpha_engine_card = self.handle_single_version_engine_rate(alpha_info)
        # TODO 根据已插入的卡片进行计算位置 done
        for i in range(len(today_prod_engine_card)):
            request_body['card']['i18n_elements']['zh_cn'].insert(i, today_prod_engine_card[i])

        index_prod = len(request_body['card']['i18n_elements']['zh_cn']) - 4
        # print(f"index_prod = {index_prod}")

        for i, item in enumerate(today_alpha_engine_card):
            request_body['card']['i18n_elements']['zh_cn'].insert(i + index_prod, item)

        if yesterday_info:
            yes_prod, yes_alpha = yesterday_info[0], yesterday_info[1]
            yes_prod_engine_card = self.handle_single_version_engine_rate(yes_prod)
            yes_alpha_engine_card = self.handle_single_version_engine_rate(yes_alpha)
            yes_prod_index = len(request_body['card']['i18n_elements']['zh_cn']) - 4
            # print(f"yes_prod_index = {yes_prod_index}")

            for i, item in enumerate(yes_prod_engine_card):
                request_body['card']['i18n_elements']['zh_cn'].insert(i + yes_prod_index, item)

            yes_alpha_index = len(request_body['card']['i18n_elements']['zh_cn']) - 4
            # print(f"yes_alpha_index = {yes_alpha_index}")
            for i, item in enumerate(yes_alpha_engine_card):
                request_body['card']['i18n_elements']['zh_cn'].insert(i + yes_alpha_index, item)
        headers = {
            "Content-Type": "application/json;charset=utf-8"
        }
        print(f"requst_body组装完成，开始同步飞书[{time.time()}]")
        # res = requests.post(self.hook_url, headers=headers, json=request_body)
        requests.post(self.hook_url, headers=headers, json=request_body)
        # print(res.json())
        print(f"sync done，time = [{time.time()}]")
