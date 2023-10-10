# -*- coding: utf-8 -*-
"""
@Author: shining
@File: ios_crash_oom_sender.py
@Date: 2022/6/28 8:16 下午
@Version: python 3.9
@Describe:
"""
import sys
sys.path.append("../")
import time
from jira_lark_bot.config import Config
from lark_bot.ios_lark_bot import IOSLarkBot
from online_monitor.handle_sql.handle_query import HandleQuery
from utils.time_tools import TimeTools



def run():

    yesterday = TimeTools.get_yesterday_ymd()
    # debug_date = "20220628"
    yesterday_data = HandleQuery.handle_ios_crash_oom_rate_query(yesterday)
    # print(yesterday_data)
    # hook_url = Config.DEBUG_BOT
    hook_url = Config.IOS_OOM_CRASH_RATE_INDEX
    lark = IOSLarkBot(hook_url)
    lark.send_to_lark(yesterday_data)


if __name__ == "__main__":
    start = time.time()

    run()

    end = time.time()
    print(f"执行耗时{end - start} 秒")
