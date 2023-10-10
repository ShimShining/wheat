# -*- coding: utf-8 -*-
"""
@Author: shining
@File: work_date.py
@Date: 2022/9/20 8:58 下午
@Version: python 3.9
@Describe:
"""
start_day = '2022-04-11'
end_day = '2022-09-20'
import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay


def count_businessday(start_day, end_day):
    b = CustomBusinessDay(holidays=['2020-04-06', '2020-05-01', '2020-05-04', '2020-05-05', '2020-06-25', '2020-10-01',
                                    '2020-10-05', '2020-10-06', '2020-10-07', '2020-10-08'])
    bus_day = pd.date_range(start=start_day, end=end_day, freq=b)
    length = len(bus_day)

    extra_work_day = ['2020-04-26', '2020-05-09', '2020-06-28', '2020-09-27', '2020-10-10']
    extra_len = 0
    for i in extra_work_day:
        if i >= start_day and i <= end_day:
            extra_len = extra_len + 1

    print(length + extra_len)


def count_days(a, b):
    import datetime
    d1 = datetime.datetime(*a)  # 第一个日期
    d2 = datetime.datetime(*b)  # 第二个日期
    interval = d2 - d1  # 两日期差距
    print(interval.days)


if __name__ == '__main__':
    # count_businessday(start_day, end_day)
    s = (2022, 9, 13)
    e = (2022, 9, 20)
    count_days(s, e)