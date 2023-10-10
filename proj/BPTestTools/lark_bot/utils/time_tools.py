# -*- coding: utf-8 -*-
"""
@Author: shining
@File: time_tools.py
@Date: 2022/1/25 11:21 下午
@Version: python 3.10
@Describe:时间格式处理
"""
import time
from datetime import timedelta, datetime
import pytz


class TimeTools:

    @staticmethod
    def get_today_ymd():
        """
        :return: 返回年月日的今天
        """
        ts = int(time.time())
        tz = pytz.timezone('Asia/Shanghai')
        dt = pytz.datetime.datetime.fromtimestamp(ts, tz)
        time_str = dt.strftime("%Y%m%d")
        return time_str

    @staticmethod
    def get_yesterday_ymd():
        """
        :return: 返回前一天的年月日
        """
        ts = int(time.time())
        ts = ts - 24 * 60 * 60
        tz = pytz.timezone('Asia/Shanghai')
        dt = pytz.datetime.datetime.fromtimestamp(ts, tz)
        time_str = dt.strftime("%Y%m%d")
        return time_str

    @staticmethod
    def get_now_hour():
        ts = int(time.time())
        tz = pytz.timezone('Asia/Shanghai')
        dt = pytz.datetime.datetime.fromtimestamp(ts, tz)
        time_str = dt.strftime("%H")
        return int(time_str)




if __name__ == "__main__":

    y = TimeTools.get_yesterday_ymd()
    t = TimeTools.get_today_ymd()
    h = TimeTools.get_now_hour()
    print(y)
    print(t)
    print(h)
