# -*- coding: utf-8 -*-
"""
@Author: shining
@File: jira_pm_bug_sync_lark_bot.py
@Date: 2022/8/12 9:30 下午
@Version: python 3.9
@Describe:
"""
import time

import requests

from config import Config
from lark_bot.leakage_lark_bot import LarkBotCSS, handle_tab


def send_jira_pm_bug_sync(hook_url, pm_issues):
    lbc = LarkBotCSS()
    # 标题
    lbc.lark_header("🔧 BP-US国际版 BUUUUUUG Sync 🔧")  # Todo
    # 概要
    fields_t_v = []
    lbc.add_text_for_fields(fields_t_v, "🕙 统计时间：", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    lbc.add_text_for_fields(fields_t_v, "📦 相关版本：", "BP-US国际版" + '：' + pm_issues['version_nums'])
    lbc.add_fields_for_elements(fields_t_v)
    lbc.add_divider_for_elements()

    at_user_open_ids = dict(zip(pm_issues['pm_owners'].keys(), Config.OPEN_IDS_PM))
    # print(at_user_open_ids)
    # print(pm_issues['pm_owners'])
    res = sorted(pm_issues['pm_owners'].items(),
           key=lambda i: (int(i[1]["status_issues"]['待办']) + int(i[1]["status_issues"]['处理中'])), reverse=True)
    for k, val in res:
        icon = '🙆 '
        if k in ["shliy", "qiqi", "Nicole"]:
            icon = '👧 '
        open_id = at_user_open_ids[k]["open_id"]
        name = at_user_open_ids[k]["name"]
        at_text = r'<at id=' + open_id + '>' + name + '</at>'
        # print(at_text)
        owner = icon + ' ' + at_text + '\tBug总数：' + str(val['total']) + "\n"
        # '\t当前活跃BUG统计>>'
        btn_text = [str(status) + ':' + str(num) + "\t" for status, num in val['status_issues'].items()]
        btn_text = handle_tab(btn_text)
        btn_text = "活跃sprint-BUG>>  " + "".join(btn_text) + "\n"
        # 处理需求相关的bug跟进状态
        demands_issues = val.get("demand_issues_status", None)
        demands_btn_text = ""
        index = 0
        if not (len(demands_issues.keys()) == 1 and "未关联需求" in demands_issues.keys()):
            i = 1
            for d_k, d_v in demands_issues.items():
                if d_k == "未关联需求":
                    continue
                demand_btn_text = [str(status) + ':' + str(num) + "\t" for status, num in d_v.items()]
                demand_btn_text = handle_tab(demand_btn_text)
                demand_btn_text = str(i) + ". [" + d_k + "] >> " + "".join(demand_btn_text) + "\n"
                i += 1
                index = i
                demands_btn_text += demand_btn_text
            # 将未关联需求的bug放在最后一栏
            not_union_demand_bugs = demands_issues.get("未关联需求", None)
            if not_union_demand_bugs:
                not_union_demand_bugs_text = [str(status) + ':' + str(num) + "\t" for status, num in not_union_demand_bugs.items()]
                not_union_demand_bugs_text = handle_tab(not_union_demand_bugs_text)
                not_union_demand_bugs_text = str(index) + ". [" + "未关联需求" + "] >> " + "".join(not_union_demand_bugs_text) + "\n"
                demands_btn_text += not_union_demand_bugs_text

        lbc.add_text_dev_for_elements(owner + btn_text + demands_btn_text)
        lbc.add_divider_for_elements()

    lbc.add_url_link_button("url",
                            content="点击button跳转Jira活跃冲刺面板")
    lbc.add_divider_for_elements()

    # 打包数据
    data = lbc.handl_card()
    data = lbc.lark_data_interactive(data)

    return requests.post(url=hook_url, headers={"Content-Type": "application/json"}, json=data)
