# -*- coding: utf-8 -*-
"""
@Author: shining
@File: run.py
@Date: 2021/12/4 3:14 下午
@Version: python 3.10
@Describle:运行入口
"""
import sys
import time
sys.path.append("../")
from jira_operation.jira_operation import JiraOperation
from config import *
from lark_bot.lark_bot import LarkBot


def run(project="BD"):

    # now = time.localtime(time.time())
    # hour = now.tm_hour
    # weekday = now.tm_wday
    # if int(hour) == 14 and int(weekday) != 3:
    #     print("非周四的14点，不执行任务！")
    #     return
    # return    # Jenkins任务无法远程关闭，暂时使用直接return来关闭bug机器人每日同步
    try:
        env = sys.argv[1]
    except Exception as e:
        print(e)
        env = None
    if env:
        project = env

    jira = JiraOperation(Config.JIRA_SERVER, Config.USER_NAME, Config.TOKEN)

    issues = jira.handle_active_issues(project)
    for issue in issues:
        current_sprint_issues_info, todo = issue
        # print(current_sprint_issues_info)
        # print(current_sprint_issues_info)
        # print(todo)
        if project == "BC":
            lark = LarkBot(Config.CN_WEB_HOOK_URL)
        elif project == "BD":
            lark = LarkBot(Config.US_WEB_HOOK_URL)
        else:
            raise Exception("没有实例化Lark Bot api，请检查")
        # lark = LarkBot(Config.DEBUG_BOT)
        lark.send_notification(current_sprint_issues_info)


if __name__ == "__main__":
    run()
