# -*- coding: utf-8 -*-
"""
@Author: shining
@File: config.py
@Date: 2022/5/20 2:31 下午
@Version: python 3.9
@Describe: 配置文件
"""
import os
import app_global_variable as agv

try:
    agv._get("RUN_ENV")
except Exception:
    agv._init()


class Config:
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__)).split('BPUITest')[0] + "\\"

    PLATFORM = "android" if not agv._get("PLATFORM") else agv._get("PLATFORM")
    # PLATFORM = "android"
    # PLATFORM = "ios"
    # PLATFORM = "u3d"
    RUN_ENV = 'master' if not agv._get("RUN_ENV") else agv._get("RUN_ENV")
    # RUN_ENV = 'master'5641
    # RUN_ENV = 'alpha'
    # RUN_ENV = 'prod'
    PACKAGE_LIST = {
        "android": {
            "master": "",
            "alpha": "",
            "prod": "",
            # 将adb devices后的列表，添加到这个list里
            "devices_list": [
                #"Android:///3046379845000CL",     # guanglin
                # "Android://127.0.0.1:5037/SKAAB6QCUSMRSG4P",    # 垃圾红米9A 需要登录小米账号+插入SIM卡才可以安装
                # "Android://127.0.0.1:5037/R58M81M64SA",          # longyonghe 三星
                # "Android:///emulator-5554"
                # "Android://127.0.0.1:5037/R58M835CJAD"
                 "Android:///" #liwen 设备1
            ],
            "another_devices": [
                # "Android:///cc9997d3"   # cc9997d3
                "Android:///b64a97dc"     # vivo 1906
            ]
        },
        "ios": {
            "master": "",
            "alpha": "",
            "prod": "",
            "devices_list": [

            ]
        }
    }
    BUNDLE_ID = PACKAGE_LIST[PLATFORM][RUN_ENV]
    LANGUAGE = 'en'

    # 配置自己的Google Account在这个地方
    GOOGLE_ACCOUNT = ""
    # GOOGLE_ACCOUNT = ""
    # GOOGLE_ACCOUNT = ""
    # GOOGLE_ACCOUNT = ""
    # 设备B的账号
    # ANOTHER_DEVICE_ACCOUNT = ""

    # airtest 日志等级
    """ CRITICAL = 50
        FATAL = CRITICAL
        ERROR = 40
        WARNING = 30
        WARN = WARNING
        INFO = 20
        DEBUG = 10
        NOTSET = 0
    """
    AIRTEST_LOGGING_LEVEL = "INFO"

    # 飞书机器人webhook
    # DEBUG ==> QA Team
    DEBUG_WEB_HOOK_URL = ""
    # 专项测试群
    SPECIAL_WEB_HOOK_URL = ""

    # 工程师群
    ENGINER_WEB_HOOK_URL = ""

    BLACK_POPUP_LISTS = {
        'android': [],
        'ios': []
    }


if __name__ == "__main__":
    print(Config.ROOT_DIR)
