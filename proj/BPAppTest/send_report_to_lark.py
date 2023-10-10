# -*- coding: utf-8 -*-
"""
@Author: shining
@File: send_report_to_lark.py
@Date: 2022/5/27 11:52 上午
@Version: python 3.9
@Describe:
"""


from notification.lark import Lark
from config import Config
from utils.yaml_handler import YAMLHandler


def send_report_to_lark():

    report_data = YAMLHandler.read('./notification/us_api_report.yml')
    l = Lark(Config.DEBUG_WEB_HOOK_URL)
    # l = Lark(Config.SPECIAL_WEB_HOOK_URL)
    # l = Lark(Config.ENGINER_WEB_HOOK_URL)
    res = l.send_report_to_lark(report_data)
    # print(res)


if __name__ == "__main__":

    send_report_to_lark()
