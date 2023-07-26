# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: uuid_random.py
@Date: 2021/10/29 5:25 下午
@Version: python 3.10
@Describle: 根据时间戳+线程，生成唯一的id
"""
import random
import threading
import time


class UUID_Random:

    @classmethod
    def unionid(cls):
        cur_time_stamp = int(round(time.time() * 1000))
        thread = threading.current_thread()
        thread_id = thread.ident
        random_char = cls.random_char(3)
        return str(cur_time_stamp) + str(thread_id) + random_char

    @staticmethod
    def random_char(k):

        char_list = [chr(ord("a") + i) for i in range(26)] + [chr(ord("A") + i) for i in range(26)]
        return "".join(random.choices(char_list, k=k))

