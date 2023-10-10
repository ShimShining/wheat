# -*- coding: utf-8 -*-
"""
@Author: shining
@File: data_model.py
@Date: 2022/12/1 3:50 下午
@Version: python 3.9
@Describe:
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