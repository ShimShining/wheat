# -*- coding: utf-8 -*-
"""
@Author: shining
@File: defect_leakage_rate.py
@Date: 2022/6/26 11:17 下午
@Version: python 3.8
@Describle: 漏测率统计&飞速机器人-Run
"""
import sys

sys.path.append("../")
from jira_lark_bot.config import Config
from jira_lark_bot.jira_operation.defect_leakage_rate import DefectLeakageRate
from jira_lark_bot.lark_bot.leakage_lark_bot import *


def run():
    jira = DefectLeakageRate(server=Config.JIRA_SERVER, username=Config.USER_NAME, token=Config.TOKEN)
    # qa_rales=jira.get_qa_roles()
    his_file = r'./satic_resource/total_issues.yml'
    rate_info = jira.get_defect_leakage_rate(Config.QA_TEAM_OWNERS, history_file=his_file)
    hook_url = Config.DEBUG_BOT
    # hook_url = Config.US_WEB_HOOK_URL
    post_leakage_rate_lark_bot(hook_url=hook_url, rate_info=rate_info)


if __name__ == "__main__":
    start = time.time()
    run()
    end = time.time()
    print(f"耗时={end -start} 秒")
