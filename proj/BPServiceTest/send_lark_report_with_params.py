# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: send_lark_report.py
@Date: 2022/4/27 10:17 上午
@Version: python 3.8
@Describe:
"""
from notification.lark import Lark
from us_api_test.config import Config
from utils.read_yaml import ReadYAML


def send_lark_report():

    report_data = ReadYAML.read('./notification/us_api_report.yml')
    # l = Lark(Config.DEBUG_WEB_HOOK_URL)
    # l = Lark(Config.SPECIAL_WEB_HOOK_URL)
    l = Lark(Config.ENGINER_WEB_HOOK_URL)
    res = l.send_report_to_lark(report_data, job=True)
    # print(res)


if __name__ == "__main__":

    send_lark_report()
