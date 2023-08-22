# -*- coding: utf-8 -*-
"""
@Author: shining
@File: faker.py
@Date: 2021/10/29 5:49 下午
@Version: python 3.10
@Describle: 假数据生成，由faker包封装
"""
import json
import os
import random
import sys

from faker import Faker


class Fake:

    __faker_cn = Faker("zh_CN")
    __faker_us = Faker()

    @property
    def cn_user_name(self):

        return self.__faker_cn.name()

    @property
    def cn_nick_name(self):

        path = os.getcwd()
        __root_dir = os.path.abspath(os.path.dirname(__file__)).split('wheat')[0] + "wheat/"
        # print(f"当前目录={path}")
        # todo 假数据不应该放utils模块
        with open(__root_dir + r'utils/'+'adjective.json', 'r') as f:
            adjective = json.loads(f.read())

        with open(__root_dir + r'utils/' + 'noun.json') as f:
            noun = json.loads(f.read())

        return adjective[random.randrange(len(adjective) - 1)] + u'的' + noun[random.randrange(len(noun) - 1)]

    @property
    def us_nick_name(self):

        return self.__faker_us.name()[:12]

