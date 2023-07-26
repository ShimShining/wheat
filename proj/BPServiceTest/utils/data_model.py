# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: data_model.py
@Date: 2021/11/22 8:03 下午
@Version: python 3.10
@Describle: 抽象数据模型
"""


class DataModel:

    def __init__(self, data_dict):

        for k, v in data_dict.items():

            if isinstance(v, list) or isinstance(v, dict):
                exec(f"self.{k} = {v}")
            elif isinstance(v, int) and v < 10000:
                exec(f"self.{k} = {v}")
            else:
                exec(f"self.{k} = '{v}'")

            # self.k = v

