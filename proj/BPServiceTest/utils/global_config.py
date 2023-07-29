# -*- coding: utf-8 -*-
"""
@Author: shining
@File: global_config.py
@Date: 2021/11/22 6:58 下午
@Version: python 3.10
@Describle:全局项目配置文件读取
"""
import os


class GlobalConfig:

    ROOT_DIR = os.path.abspath(os.path.dirname(__file__)).split('BUDTest')[0] + "BUDTest/"

