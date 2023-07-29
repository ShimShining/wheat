# -*- coding: utf-8 -*-
"""
@Author: shining
@File: send_engine_report_to_lark.py
@Date: 2022/6/23 10:14 上午
@Version: python 3.9
@Describe:
"""

from notification.lark import Lark
from us_api_test.config import Config
from utils.read_yaml import ReadYAML


def send_lark_report():

    report_data = ReadYAML.read('./notification/us_api_report.yml')
    # l = Lark(Config.DEBUG_WEB_HOOK_URL)
    # l = Lark(Config.SPECIAL_WEB_HOOK_URL)
    # l = Lark(Config.ENGINER_WEB_HOOK_URL)
    l = Lark(Config.ENGINE_SYNC_WEB_HOOK_URL)
    res = l.send_report_to_lark(report_data, engine=True)
    # print(res)


if __name__ == "__main__":

    send_lark_report()
