# -*- coding: utf-8 -*-
"""
@Author: shining
@File: big_query.py
@Date: 2022/1/23 5:07 下午
@Version: python 3.10
@Describe: big query封装
"""
from google.cloud import bigquery


class BigQuery:
    AUTH_JSON_FILE_PATH = "../../cred/google_application_credentials.json"
    TIME_OUT = 240
    LIMIT = 100
    SLEEP_SEC = 1

    def __init__(self, auth_json=AUTH_JSON_FILE_PATH):

        self.auth_json = auth_json
        self.client = bigquery.Client.from_service_account_json(self.auth_json)

    def bq_query(self, sql):

        query_job = self.client.query(sql)
        result = query_job.result(timeout=self.TIME_OUT)
        df = result.to_dataframe()
        return df

    def post_enter_room_rate(self, total, success, quit=0):

        success_rate = 0.0
        if int(total) > 0 and quit < total:
            rate = success / (total - quit)
            if rate > 1:
                rate = 1.00
            success_rate = round(float(rate) * 100, 2)
        return success_rate

    def get_click_to_play_pv(self, sql, sql_not_intraday="", is_room_code=False):
        success, total_call_unity, success_rate = 0, 0, 0.0
        android_success_enter, android_total_call_unity, android_success_rate = 0, 0, 0.0
        ios_success_enter, ios_total_call_unity, ios_success_rate = 0, 0, 0.0
        total_quit, android_quit, ios_quit = 0, 0, 0
        exclude_quit_total_success_rate, exclude_quit_android_success_rate, exclude_quit_ios_success_rate = 0, 0, 0
        df = None
        try:
            df = self.bq_query(sql)
        except Exception as e:
            print(f"get_click_to_play_pv查询捕获到异常={e}")
            try:
                df = self.bq_query(sql_not_intraday)
            except Exception as e:
                pass
        try:
            # Loading Page Back
            if not is_room_code:
                # total_quit = df['total_quit'].values[0]
                android_quit = df['android_quit'].values[0]
                ios_quit = df['ios_quit'].values[0]
                total_quit = android_quit + ios_quit
            success = df['success_enter'].values[0]
            total_call_unity = df['total_call_unity'].values[0]
            success_rate = self.post_enter_room_rate(total_call_unity, success)
            if not is_room_code:
                exclude_quit_total_success_rate = self.post_enter_room_rate(total_call_unity, success, total_quit)
            # android
            android_success_enter = df['android_success_enter'].values[0]
            android_total_call_unity = df['android_total_call_unity'].values[0]
            android_success_rate = self.post_enter_room_rate(android_total_call_unity, android_success_enter)
            if not is_room_code:
                exclude_quit_android_success_rate = self.post_enter_room_rate(android_total_call_unity, android_success_enter, android_quit)

            # ios
            ios_success_enter = df['ios_success_enter'].values[0]
            ios_total_call_unity = df['ios_total_call_unity'].values[0]
            ios_success_rate = self.post_enter_room_rate(ios_total_call_unity, ios_success_enter)
            if not is_room_code:
                exclude_quit_ios_success_rate = self.post_enter_room_rate(ios_total_call_unity, ios_success_enter, ios_quit)

            return success_rate, total_call_unity, success, android_success_rate, \
                   android_total_call_unity, android_success_enter, \
                   ios_success_rate, ios_total_call_unity, ios_success_enter, total_quit, android_quit, ios_quit, \
                   exclude_quit_total_success_rate, exclude_quit_android_success_rate, exclude_quit_ios_success_rate

        except Exception as e:
            print(f"get_click_to_play_pv throw exception={e}")
            return success_rate, total_call_unity, success, android_success_rate, \
                   android_total_call_unity, android_success_enter, \
                   ios_success_rate, ios_total_call_unity, ios_success_enter, total_quit, android_quit, ios_quit, \
                   exclude_quit_total_success_rate, exclude_quit_android_success_rate, exclude_quit_ios_success_rate

    def post_calc_pings_distribute(self, pings, total):

        if total < 0:
            return 0.0, 0.0, 0.0, 0.0
        # lt100_ms, gt100_le200_ms, gt200_le300_ms, gt300_ms
        print(f"pings===> {pings}")
        lt100_ms_rate = round((pings[0] / total) * 100, 2)
        if lt100_ms_rate > 100:
            lt100_ms_rate = 100.0
        gt100_le200_ms_rate = round((pings[1] / total) * 100, 2)
        if gt100_le200_ms_rate > 100:
            gt100_le200_ms_rate = 100.0
        gt200_le300_ms_rate = round((pings[2] / total) * 100, 2)
        if gt200_le300_ms_rate > 100:
            gt200_le300_ms_rate = 100.0
        gt300_ms_rate = round((pings[3] / total) * 100, 2)
        if gt300_ms_rate > 100:
            gt300_ms_rate = 100.0
        if (lt100_ms_rate + gt100_le200_ms_rate + gt200_le300_ms_rate + gt300_ms_rate) > 100:
            gt300_ms_rate = round(100 - lt100_ms_rate - gt100_le200_ms_rate - gt200_le300_ms_rate, 2)
        return lt100_ms_rate, gt100_le200_ms_rate, gt200_le300_ms_rate, gt300_ms_rate

    def get_avg_ping_info(self, sql, no_intraday_sql=""):

        # filipino_avg_ping,indonesian_avg_ping,vietnam_avg_ping,mexico_avg_ping,brazil_avg_ping,us_avg_ping

        total, avg_ping = 0, 0.0
        android_total, android_avg_ping = 0, 0.0
        ios_total, ios_avg_ping = 0, 0.0
        # alpha环境不需要
        lt100_ms, gt100_le200_ms, gt200_le300_ms, gt300_ms = 0, 0, 0, 0
        # alpha换不需要
        filipino_avg_ping, indonesian_avg_ping, vietnam_avg_ping, mexico_avg_ping, brazil_avg_ping, us_avg_ping = \
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        ping_value_distribute_rates = (0.0, 0.0, 0.0, 0.0)
        try:
            df = self.bq_query(sql)
        except Exception as e:
            print(f"get_avg_ping_info throws exception = {e}")
            try:
                df = self.bq_query(no_intraday_sql)
            except Exception as e:
                pass
        try:
            total = df['total'].values[0]
            avg_ping = round(df['avg_ping'].values[0], 2)
            android_total = df['android_total'].values[0]
            android_avg_ping = round(df['android_avg_ping'].values[0], 2)
            ios_total = df['ios_total'].values[0]
            ios_avg_ping = round(df['ios_avg_ping'].values[0], 2)

            lt100_ms = df['le100_ms'].values[0]
            gt100_le200_ms = df['gt100_le200_ms'].values[0]
            gt200_le300_ms = df['gt200_le300_ms'].values[0]
            gt300_ms = df['gt300_ms'].values[0]

            ping_value_distribute_rates = self.post_calc_pings_distribute(
                [lt100_ms, gt100_le200_ms, gt200_le300_ms, gt300_ms], total)

            filipino_avg_ping = round(df['filipino_avg_ping'].values[0], 2)
            indonesian_avg_ping = round(df['indonesian_avg_ping'].values[0], 2)
            vietnam_avg_ping = round(df['vietnam_avg_ping'].values[0], 2)
            mexico_avg_ping = round(df['mexico_avg_ping'].values[0], 2)
            brazil_avg_ping = round(df['brazil_avg_ping'].values[0], 2)
            us_avg_ping = round(df['us_avg_ping'].values[0], 2)
            # ping value distribute rate

            return total, avg_ping, android_total, android_avg_ping, ios_total, ios_avg_ping, \
                   ping_value_distribute_rates, filipino_avg_ping, indonesian_avg_ping, vietnam_avg_ping, \
                   mexico_avg_ping, brazil_avg_ping, us_avg_ping

        except Exception as e:
            print(f"get_avg_ping_info throw exception={e}")
            return total, avg_ping, android_total, android_avg_ping, ios_total, ios_avg_ping, \
                   ping_value_distribute_rates, filipino_avg_ping, indonesian_avg_ping, vietnam_avg_ping, \
                   mexico_avg_ping, brazil_avg_ping, us_avg_ping

    def get_ctoe_info(self, sql, sql_not_intraday=""):

        total_success_exit, android_success_exit, ios_success_exit = 0, 0, 0
        try:
            df = self.bq_query(sql)
        except Exception as e:
            print(f"get_ctoe_info throws exception = {e}")
            try:
                df = self.bq_query(sql_not_intraday)
            except Exception as e:
                pass
        try:
            total_success_exit = df['total_success_exit'].values[0]
            android_success_exit = df['android_success_exit'].values[0]
            ios_success_exit = df['ios_success_exit'].values[0]

            return total_success_exit, android_success_exit, ios_success_exit
        except Exception:
            return total_success_exit, android_success_exit, ios_success_exit

    def get_avg_fps_info(self, sql, no_intraday_sql=""):
        avg_fps, total_play_pv = 0, 0
        android_avg_fps, android_total_play_pv = 0, 0
        ios_avg_fps, ios_total_play_pv = 0, 0
        try:
            df = self.bq_query(sql)
        except Exception as e:
            print(f"get_avg_fps_info throws exception = {e}")
            try:
                df = self.bq_query(no_intraday_sql)
            except Exception as e:
                pass
        try:
            avg_fps = df['avg_fps'].values[0]
            total_play_pv = df['total'].values[0]
            avg_fps = self.post_avg_enter_time(total_play_pv, avg_fps)
            # android
            android_avg_fps = df['android_avg_fps'].values[0]
            android_total_play_pv = df['android_total'].values[0]
            android_avg_fps = self.post_avg_enter_time(android_total_play_pv, android_avg_fps)
            # ios
            ios_avg_fps = df['ios_avg_fps'].values[0]
            ios_total_play_pv = df['ios_total'].values[0]
            ios_avg_fps = self.post_avg_enter_time(ios_total_play_pv, ios_avg_fps)
            return avg_fps, total_play_pv, android_avg_fps, android_total_play_pv, ios_avg_fps, ios_total_play_pv
        except Exception:
            return avg_fps, total_play_pv, android_avg_fps, android_total_play_pv, ios_avg_fps, ios_total_play_pv

    def handle_data_to_img(self, sql, x_name, y_name):

        df = self.bq_query(sql)
        x = df[x_name].tolist()
        y = df[y_name].tolist()
        # todo

    def post_avg_enter_time(self, total, avg_time):

        if int(total) <= 0:
            avg_time = 0
            return avg_time
        return avg_time

    def get_avg_enter_room_time(self, sql, no_intraday_sql=""):
        avg_time, total_enter_pv = 0, 0
        android_avg_time, android_total_enter_pv = 0, 0
        ios_avg_time, ios_total_enter_pv = 0, 0
        try:
            df = self.bq_query(sql)
        except Exception as e:
            print(f"get_avg_enter_room_time throws exception = {e}")
            try:
                df = self.bq_query(no_intraday_sql)
            except Exception as e:
                pass
        try:

            avg_time = df['enter_time'].values[0]
            total_enter_pv = df['total_enter'].values[0]
            avg_time = self.post_avg_enter_time(total_enter_pv, avg_time)
            # android
            android_avg_time = df['android_enter_time'].values[0]
            android_total_enter_pv = df['android_total_enter'].values[0]
            android_avg_time = self.post_avg_enter_time(android_total_enter_pv, android_avg_time)
            # ios
            ios_avg_time = df['ios_enter_time'].values[0]
            ios_total_enter_pv = df['ios_total_enter'].values[0]
            ios_avg_time = self.post_avg_enter_time(ios_total_enter_pv, ios_avg_time)
            return avg_time, total_enter_pv, android_avg_time, android_total_enter_pv, ios_avg_time, ios_total_enter_pv
        except Exception:
            return avg_time, total_enter_pv, android_avg_time, android_total_enter_pv, ios_avg_time, ios_total_enter_pv

    def get_avg_ab_cost_time(self, sql, no_intraday_sql=""):
        ab_time, total_ab = 0, 0
        android_ab_time, android_total_ab = 0, 0
        ios_ab_time, ios_total_ab = 0, 0
        try:
            df = self.bq_query(sql)
        except Exception as e:
            print(f"get_avg_ab_cost_time throws exception = {e}")
            try:
                df = self.bq_query(no_intraday_sql)
            except Exception as e:
                print(f"second level get_avg_ab_cost_time throws exception ==> {e}")
        try:
            ab_time = df['ab_time'].values[0]
            total_ab = df['total_ab'].values[0]
            ab_time = self.post_avg_enter_time(total_ab, ab_time)
            # android
            android_ab_time = df['android_ab_time'].values[0]
            android_total_ab = df['android_total_ab'].values[0]
            android_ab_time = self.post_avg_enter_time(android_total_ab, android_ab_time)
            # ios
            ios_ab_time = df['ios_ab_time'].values[0]
            ios_total_ab = df['ios_total_ab'].values[0]
            ios_ab_time = self.post_avg_enter_time(ios_total_ab, ios_ab_time)
            return ab_time, total_ab, android_ab_time, android_total_ab, ios_ab_time, ios_total_ab
        except Exception as e:
            return ab_time, total_ab, android_ab_time, android_total_ab, ios_ab_time, ios_total_ab

    def get_ios_crash_oom_rate(self, sql):
        """
        ios OOM和crash的sql查询返回结果
        :param sql:
        :return:
        """
        reboot_all, normal_crash, foreground_oom = 0, 0, 0
        normal_crash_mobile_and_times, oom_mobile_and_times = "", ""
        try:
            df = self.bq_query(sql)
            reboot_all = df['reboot_all'].values[0]
            normal_crash = df['normal_crash'].values[0]
            foreground_oom = df['foreground_oom'].values[0]
            normal_crash_mobile_and_times = df['normal_crash_mobile_and_times'].values[0]
            oom_mobile_and_times = df['oom_mobile_and_times'].values[0]
            return reboot_all, normal_crash, foreground_oom, normal_crash_mobile_and_times, oom_mobile_and_times
        except Exception as e:
            return reboot_all, normal_crash, foreground_oom, normal_crash_mobile_and_times, oom_mobile_and_times
