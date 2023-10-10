# -*- coding: utf-8 -*-
"""
@Author: shining
@File: jira_pm_issues_run.py
@Date: 2022/8/12 11:15 下午
@Version: python 3.9
@Describe:
"""
import sys
sys.path.append("../")
from jira_lark_bot.jira_operation.get_jira_pm_issues import GetJiraPMIssues
from jira_lark_bot.config import Config

from jira_lark_bot.lark_bot.jira_pm_bug_sync_lark_bot import *

def run():
    gp = GetJiraPMIssues(server=Config.JIRA_SERVER, username=Config.USER_NAME, token=Config.TOKEN)
    pm_issues_info = gp.statistics_pm_issues(Config.PM_TEAM_OWNERS)
    # print(pm_issues_info)
    # hook_url = Config.DEBUG_BOT
    hook_url = Config.PM_ISSUES_SYNC_URL
    send_jira_pm_bug_sync(hook_url, pm_issues_info)


if __name__ == "__main__":

    start = time.time()

    run()

    end = time.time()
    print(f"执行耗时=【{end - start}】秒")
