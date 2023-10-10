# -*- coding: utf-8 -*-
"""
@Author: shining
@File: yaml_handler.py
@Date: 2022/5/25 6:34 下午
@Version: python 3.9
@Describe:Yaml 文件处理
"""

import yaml
from utils.data_model import DataModel


class YAMLHandler:

    @classmethod
    def read_case_data(cls, yaml_path, env=None, case_name=None):
        """
        读取对应环境的接口测试数据
        :param yaml_path: yaml文件路径
        :param env: 用例执行环境
        :param case_name: 用例名称
        :return:
        """
        yaml_data = cls.read(yaml_path)
        if case_name:
            return yaml_data[env][case_name]
        return yaml_data[env]

    @staticmethod
    def read(yaml_path):
        """
        读取yaml文件
        :param yaml_path:
        :return: yaml文件内内容
        """
        with open(yaml_path, encoding="utf-8") as yf:

            return yaml.safe_load(yf)

    @staticmethod
    def write_yaml(yaml_path, data: dict):
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)

    @classmethod
    def case_data(cls, yaml_name, case_name=None):
        data_dict = cls.case_data_dict(yaml_name, case_name=case_name)
        return DataModel(data_dict)

    @classmethod
    def case_data_dict(cls, yaml_name, case_name=None):
        if ".yml" not in yaml_name:
            yaml_name += ".yml"
        from config import Config
        data_dict = cls.read_case_data(Config.ROOT_DIR +r"data/" + yaml_name, env=Config.RUN_ENV, case_name=case_name)
        return data_dict


