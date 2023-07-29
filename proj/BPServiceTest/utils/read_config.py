# -*- coding: utf-8 -*-
"""
@Author: shining
@File: read_config.py
@Date: 2021/10/27 11:15 下午
@Version: python 3.10
@Describle: 读取ini配置文件
"""
import configparser
import os
import sys


class ReadConfig:

    __cf = configparser.ConfigParser()

    @classmethod
    def get_project_env_host(cls, project):
        """
        获取指定环境的测试url
        :param project:
        :return:
        """
        run_env = cls.get_project_env(project)
        return cls.__cf.get(run_env, "host")

    @classmethod
    def get_root_dir(cls):
        root_dir = os.path.abspath(os.path.dirname(__file__)).split('BUDTest')[0] + "BUDTest/"
        return root_dir

    @classmethod
    def get_project_env(cls, project):

        __root_dir = cls.get_root_dir()
        proj_config_path = __root_dir + f"{project}/env.ini"
        # print(proj_config_path)
        cls.__cf.read(proj_config_path)
        # print(cls.__cf.sections())
        run_env = cls.__cf.get("ENV", "run_env")
        return run_env


