# -*- coding: utf-8 -*-
"""
@Author: shining
@File: defect_leakage_rate.py
@Date: 2022/6/26 11:17 下午
@Version: python 3.8
@Describle: 漏测率统计-飞速机器人
"""
import requests
import time

from config import Config


def return_iteam(func):
    def r(*args, **kwargs):
        key, data = func(*args, **kwargs)
        res = {
            'key': key,
            'data': data
        }
        return res

    return r


class LarkBotCSS:
    def __init__(self):
        self.header = ""
        self.elements = []

    def lark_data_interactive(self, card):  # 返回interactive类型data数据
        d = {
            "msg_type": "interactive",
            "card": card
        }
        return d

    # @return_iteam
    def lark_header(self, text, template="turquoise"):
        # key="header"
        d = {
            "template": template,
            "title": {
                "content": text,
                "tag": "plain_text"}
        }
        self.header = d

    def add_divider_for_elements(self):  # 分割线
        self.elements.append({"tag": "hr"})

    def add_text_dev_for_elements(self, text):  # 文字模块
        div = {
            "tag": "div",
            "text": {
                "content": "**" + str(text) + "**",
                "tag": "lark_md"
            }
        }
        self.elements.append(div)

    def add_text_but_for_elements(self, text, options_text: list):  # 带按钮列表的文字模块
        div = {
            "tag": "div",
            "text": {
                "content": "**" + str(text) + "**",
                "tag": "lark_md"},
            "extra": {
                "tag": "overflow",
                "options": []}
        }
        for text in options_text:
            option = {
                "text": {
                    "tag": "plain_text",
                    "content": text},
                "value": "",
            }
            div["extra"]["options"].append(option)
        self.elements.append(div)

    def add_fields_for_elements(self, fields):  # fields,就是放时间、什么一级值班啊、二级值班那个图表文本的东西
        self.elements.append({"fields": fields, "tag": "div"})

    def add_url_link_button(self, url, content="点击此处跳转"):
        link_button = {
            "actions": [{

                "tag": "button",
                "text": {
                    "content": f"**{content}**",
                    "tag": "lark_md"
                },
                "url": url,
                "type": "default",
                "value": {
                }
            }],
            "tag": "action"
        }
        self.elements.append(link_button)

    def add_text_for_fields(self, fields, text_title, text, is_short: bool = True):  # 添加field进fields里面：标题内容
        finld = {
            "is_short": is_short,
            "text": {"content": "**" + str(text_title) + "**\n" + str(text),
                     "tag": "lark_md"
                     }
        }
        fields.append(finld)

    def handl_card(self):  # 整合card字段数据
        res = {
            "config": {"wide_screen_mode": True},
            "elements": self.elements,
            "header": self.header

        }
        return res


def handle_tab(text_list: list):
    res = []
    length = len(text_list)
    for i, text in enumerate(text_list):
        if i == 0 or i < length - 1:
            res.append(text + "  ")
        elif i == length - 1:
            res.append(text)
    return res


def post_leakage_rate_lark_bot(hook_url, rate_info):
    lbc = LarkBotCSS()
    # 标题
    lbc.lark_header('🌟' + rate_info['project_name'] + '漏测率以及待办BUG🔧统计🌟')  # Todo
    # 概要
    fields_t_v = []
    lbc.add_text_for_fields(fields_t_v, "🕙 统计时间：", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    lbc.add_text_for_fields(fields_t_v, "📦 最新版本：", rate_info['project_name'] + '：' + rate_info['version'] + " PROD")
    lbc.add_fields_for_elements(fields_t_v)
    lbc.add_divider_for_elements()

    # 团队数据
    fields_team = []
    team_rate = rate_info['team_rate']
    team_rate_str = '👥 Team Rate：' + \
                    '\n历  史-漏测率：' + str(round(team_rate['history_leakages_rate'] * 100, 2)) + '%' + \
                    '\tBug总数：' + str(team_rate['history_total_issues']) + \
                    '\t漏测数量：' + str(team_rate['history_leakages']) + '\n' + \
                    rate_info["version"] + '-漏测率：' + str(round(team_rate['rate'] * 100, 2)) + '%' + \
                    '\tBug总数：' + str(team_rate['defects']) + \
                    '\t漏测数量：' + str(team_rate['leakages']) + '\n'
    # '\t当前活跃BUG统计>>'
    btn_text = [str(status) + ':' + str(defs) + "\t" for status, defs in
                team_rate['active_issues'].items()]
    btn_text = handle_tab(btn_text)
    btn_text = "活跃sprint-BUG>>  " + "".join(btn_text)
    # lbc.add_text_but_for_elements(team_rate_str, btn_text)
    lbc.add_text_dev_for_elements(team_rate_str + btn_text)
    lbc.add_divider_for_elements()
    at_user_open_ids = dict(zip(rate_info['owner_rate'].keys(), Config.OPEN_IDS_QA))
    # print(at_user_open_ids)

    # 个人数据
    # res[owner] = {
    #     'defects': len(ds),
    #     'leakages': len(ls),
    #     'owner_rate': owner_rate,
    #     'status_issues': cla_issues,
    #     'active_issues': act_cla_issues,
    #     'leakages_issues': ls,
    #     'recent_v_demand_issues_distribute': recent_prod_demands_issues_distribute
    # }
    res = sorted(rate_info['owner_rate'].items(),
                 key=lambda i: (int(i[1]["active_issues"]["待办"]) + int(i[1]["active_issues"]["处理中"]) + int(
                     i[1]["active_issues"]["In Review"])), reverse=True)  # i[1]["active_issues"]["已完成"]

    for key, val in res:
        icon = '👤 '
        if key == "llw":
            icon = '👰 '
        if key == 'nqp':
            icon = '🐮 '
        open_id = at_user_open_ids[key]["open_id"]
        name = at_user_open_ids[key]["name"]
        at_text = r'<at id=' + open_id + '>' + name + '</at>'
        # print(at_text)
        owner = icon + ' ' + at_text + '\n'
        leakage_text = rate_info['version'] + '漏测率：' + str(round(val['owner_rate'] * 100, 2)) + '%' + \
                '\tBug总数：' + str(val['defects']) + \
                '\t漏测数：' + str(val['leakages']) + "\n"
        # '\t当前活跃BUG统计>>'
        btn_text = [str(status) + ':' + str(defs) + "\t" for status, defs in
                    val['active_issues'].items()]
        btn_text = handle_tab(btn_text)
        btn_text = "活跃sprint-BUG>>  " + "".join(btn_text) + "\n"
        # 处理最近prod版本需求的bug分布
        demand_issues = val.get("recent_v_demand_issues_distribute", None)
        demand_text = ""
        if demand_issues:
            if not (len(demand_issues.keys()) == 1 and "未关联需求" in demand_issues.keys()):
                i = 1
                for k, v in demand_issues.items():
                    if k == "未关联需求":
                        continue
                    demand_text += str(i) + '. [' + k + "]bug数: " + str(v)
                    if i == len(demand_issues.keys()) or i % 2 == 0:
                        demand_text += '\n'
                    else:
                        demand_text += '\t' * 3
                    i += 1
                not_union_demand = demand_issues.get("未关联需求", None)
                if not_union_demand:
                    demand_text += str(i) + ". " + "未关联需求: " + str(not_union_demand) + '\n'
        # lbc.add_text_but_for_elements(owner, btn_text)
        lbc.add_text_dev_for_elements(owner + btn_text + leakage_text + demand_text)
        lbc.add_divider_for_elements()
    lbc.add_url_link_button("url",
                            content="点击button跳转Jira活跃冲刺面板")
    lbc.add_divider_for_elements()
    # 打包数据
    data = lbc.handl_card()
    data = lbc.lark_data_interactive(data)

    return requests.post(url=hook_url, headers={"Content-Type": "application/json"}, json=data)
