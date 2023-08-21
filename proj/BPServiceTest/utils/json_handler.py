# -*- coding: utf-8 -*-
"""
@Author: shining
@File: json_handler.py
@Date: 2022/6/12 8:42 下午
@Version: python 3.9
@Describe: 读取json文件
"""
import json


class JsonHandler:

    @staticmethod
    def read_json(json_path):
        """
        读取并返回json数据
        :param json_path:
        :return:
        """

        with open(json_path, 'r') as f:
            json_data = json.load(f)
        return json_data

    @staticmethod
    def get_json_value_by_json_path():
        pass


if __name__ == "__main__":
    from config import Config

    path = Config.DATA_PATH
    file_path = path + 'matchRegion.json'
    data = JsonHandler.read_json(file_path)
    print(data)

