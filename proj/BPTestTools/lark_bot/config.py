# -*- coding: utf-8 -*-
"""
@Author: shining
@File: config.py.py
@Date: 2021/11/30 11:19 下午
@Version: python 3.10
@Describle: 配置文件
"""


class Config:
    # JIRA 相关配置
    JIRA_SERVER = ""
    USER_NAME = ""
    TOKEN = ""
    CN_BOARD_URL = ""
    BP_BOARD_URL = ""
    BP_STATISTICAL_ANALYSIS_URL = ""

    # Lark bot 相关配置
    # real调试机器人
    DEBUG_BOT = ""

    # lark-robot-notification
    DEBUG_Lark_Bot = ""
    # 调试飞书发送卡片信息的机器人
    DEBUG_WEB_HOOK_URL = ""

    CN_WEB_HOOK_URL = ""
    US_WEB_HOOK_URL = ""
    # 进展群机器人
    US_ENGINE_WEB_HOOK_URL = ""
    # 项目群机器人
    US_OFFLINE_RENDER_WEB_HOOK_URL = ""

    # ios oom-crash rate index sync robot
    IOS_OOM_CRASH_RATE_INDEX = ""

    # BP 小Q自建应用  and APP_SECRET
    APP_ID = ""
    APP_SECRET = ""

    # 运行昨日查询校验时间（小于该时间运行时，会运行昨天指标的查询）
    YESTERDAY_QUERY_HOUR = 11

    # 联机暴露的健康度和联机道具成功率指标接口
    ENGINE_HEALTH_PROP_GET_MASTER_URL = ""
    ENGINE_HEALTH_PROP_GET_PROD_URL = ""

    # Google Big Query Dataset prefix
    GOOGLE_BIGQUERY_DATASET_PREFIX = ""

    QA_TEAM_OWNERS = ['']
    # Open ID与姓名对应
    OPEN_IDS_QA = [
        {"name": "", "open_id": ""}
    ]

    # PM Jira名字，Open IDs配置
    PM_TEAM_OWNERS = [""]

    OPEN_IDS_PM = [
        {"name": "", "open_id": ""}
    ]
    PM_ISSUES_SYNC_URL = ""
