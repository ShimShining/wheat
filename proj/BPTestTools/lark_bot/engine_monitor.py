# -*- coding: utf-8 -*-
"""
@Author: shining
@File: engine_monitor.py
@Date: 2022/1/25 11:05 下午
@Version: python 3.10
@Describe: 联机相关指标同步
clickToPlay
离线渲染平均FPS
"""
import sys
import time
# import os
# import tzlocal
# from apscheduler.schedulers.blocking import BlockingScheduler
from online_monitor.handle_sql.handle_query import HandleQuery
from utils.time_tools import TimeTools

sys.path.append("../")
from jira_operation.jira_operation import JiraOperation
from config import *
from lark_bot.lark_bot import LarkBot


def run(proj_key='BD'):

    # 预留命令行参数，增加项目拓展性
    try:
        env = sys.argv[1]
    except Exception as e:
        print(e)
        env = None
    if env:
        proj_key = env

    # 通过jira获取prod和alpha版本号
    jira = JiraOperation(Config.JIRA_SERVER, Config.USER_NAME, Config.TOKEN)
    prod_version, alpha_version = jira.get_app_version(proj_key)
    # prod_version, alpha_version = '1.35.0', '1.36.0'
    # offline_prod_version = prod_version[:-2] + '%'
    # offline_alpha_version = alpha_version[:-2] + '%'
    if prod_version == "1.47.1":
        offline_prod_version = ['1.47.1', '1.47.2']
    else:
        offline_prod_version = prod_version
    if alpha_version == "1.47.1":
        offline_alpha_version = ['1.47.1', '1.47.2']
    else:
        offline_alpha_version = alpha_version

    # 获取今天的时间
    format_today = TimeTools.get_today_ymd()
    # today_engine = HandleQuery.handle_engine_query(format_today, prod_version, alpha_version)
    today_offline = HandleQuery.handle_offline_query(format_today, offline_prod_version, offline_alpha_version)
    today_offline[0]["version"] = prod_version
    today_offline[1]['version'] = alpha_version
    now_hour = TimeTools.get_now_hour()
    yes_offline = None
    # yes_engine = None
    if int(now_hour) < Config.YESTERDAY_QUERY_HOUR:
        format_yesterday = TimeTools.get_yesterday_ymd()
        # yes_engine = HandleQuery.handle_engine_query(format_yesterday, prod_version, alpha_version)
        yes_offline = HandleQuery.handle_offline_query(format_yesterday, offline_prod_version, offline_alpha_version)
        yes_offline[0]["version"] = prod_version
        yes_offline[1]['version'] = alpha_version

    # 发送click_to_play指标
    # today_engine  = [0, 1]
    # today_engine[0] = {'dat': '20220427', 'version': '1.25.0', 'total_success_rate': 94.63, 'total_enter': 383115, 'success_enter': 362541, 'android_success_rate': 94.61, 'android_total_enter': 359690, 'android_success_enter': 340304, 'ios_success_rate': 94.93, 'ios_total_enter': 23425, 'ios_success_enter': 22237, 'total_success_exit_rate': 77.14, 'android_success_exit_rate': 77.29, 'ios_success_exit_rate': 74.78, 'rc_success_rate': 90.18, 'total_room_enter': 29779, 'room_success_enter': 26854, 'android_rc_success_rate': 90.1, 'android_total_room_enter': 27705, 'android_room_success_enter': 24963, 'ios_rc_success_rate': 91.18, 'ios_total_room_enter': 2074, 'ios_room_success_enter': 1891, 'ctop_cost': 12.280954408975422, 'total_click': 358156, 'android_ctop_cost': 12.790766088738001, 'android_total_click': 336237, 'ios_ctop_cost': 4.460453940508237, 'ios_total_click': 21919, 'exit_success_rate': 295533, 'total_exit': 278015, 'click_success_exit': 17518, 'env': 'prod'}
    # today_engine[1] = {'dat': '20220427', 'version': '1.26.0', 'total_success_rate': 99.16, 'total_enter': 119, 'success_enter': 118, 'android_success_rate': 100.0, 'android_total_enter': 46, 'android_success_enter': 46, 'ios_success_rate': 98.63, 'ios_total_enter': 73, 'ios_success_enter': 72, 'total_success_exit_rate': 100.0, 'android_success_exit_rate': 100.0, 'ios_success_exit_rate': 100.0, 'rc_success_rate': 100.0, 'total_room_enter': 4, 'room_success_enter': 4, 'android_rc_success_rate': 100.0, 'android_total_room_enter': 2, 'android_room_success_enter': 2, 'ios_rc_success_rate': 100.0, 'ios_total_room_enter': 2, 'ios_room_success_enter': 2, 'ctop_cost': 5.215194547008547, 'total_click': 117, 'android_ctop_cost': 6.163998111111112, 'android_total_click': 45, 'ios_ctop_cost': 4.622192319444445, 'ios_total_click': 72, 'exit_success_rate': 144, 'total_exit': 49, 'click_success_exit': 95, 'env': 'alpha'}
    # yes_engine = None
    # lark_engine = LarkBot(Config.US_ENGINE_WEB_HOOK_URL)
    # lark_engine = LarkBot(Config.DEBUG_BOT)
    # lark_engine = LarkBot(Config.DEBUG_Lark_Bot)
    # print(f"id-lark_engine == {id(lark_engine)}")
    # lark_engine.send_engine_index(today_engine[0], today_engine[1],  yes_engine)
    # 发送avg_fps指标
    # time.sleep(3)
    lark_offline_render = LarkBot(Config.US_OFFLINE_RENDER_WEB_HOOK_URL)
    # lark_offline_render = LarkBot(Config.DEBUG_BOT)
    # lark_offline_render = LarkBot(Config.DEBUG_Lark_Bot)
    # print(f"id-lark_offline_render == {id(lark_offline_render)}")
    lark_offline_render.send_offline_index(today_offline[0], today_offline[1], yes_offline)


if __name__ == "__main__":
    start = time.time()
    # 本地定时任务
    # sched = BlockingScheduler(timezone=str(tzlocal.get_localzone()))
    # sched.add_job(run, 'cron', hour='10,15,21', end_date='2022-04-06')
    # sched.start()
    run()
    end = time.time()
    print(f"执行耗时{end - start} 秒")

