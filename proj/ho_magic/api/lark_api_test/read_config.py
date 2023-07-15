# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/7/15
Describe: 读取配置文件信息
"""
import configparser
import os


class ReadConfig:

    __root_dir = "D:\\personProc\\wheat\\proj\\ho_magic\\api\\lark_api_test\\config.ini"
    __cf = configparser.ConfigParser()

    @classmethod
    def get_lark_api_base_url(cls):
        cls.__cf.read(cls.__root_dir)
        # print(cls.__root_dir)
        #         # print(cls.__cf)
        #         # print(cls.__cf.sections())
        return cls.__cf.get("lark-api", "base_url")


if __name__ == '__main__':
    url = ReadConfig.get_lark_api_base_url()
    print(url)

