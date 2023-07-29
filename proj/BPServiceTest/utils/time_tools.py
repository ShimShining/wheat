# -*- coding: utf-8 -*-
"""
@Author: shining
@File: time_tools.py
@Date: 2021/12/30 5:31 下午
@Version: python 3.10
@Describe: 时间工具
"""
import time


class TimeTools:

    @staticmethod
    def str_to_timestamp(tm_str=None):
        """
        时间格式20211230转换为秒的时间戳
        :param tm_str: 20211230
        :return:
        """
        if not tm_str:
            return int(time.time())
        length = len(tm_str)
        if length == 8:
            y, m, d = tm_str[:4], tm_str[4:6], tm_str[6:]
        elif length == 6:
            y, m, d = tm_str[:4], tm_str[4:5], tm_str[5:]
            m = "0" + m
            d = "0" + d
        else:
            raise ValueError("tm_str 参数不正确！！！")

        str_time = "-".join([y, m, d]) + " 00:00:00"
        time_list = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(time_list))
        return timestamp

    @staticmethod
    def get_now_sec_timestamp(value_type="str"):

        if value_type == "int":
            return int(time.time())
        return str(int(time.time()))


if __name__ == "__main__":

    tl = TimeTools()
    t = "20211230"
    tp = tl.str_to_timestamp(t)
    print(tp)
