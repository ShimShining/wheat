# -*- coding: utf-8 -*-
"""
@Author: shining
@File: handle_query.py
@Date: 2022/2/13 10:16 下午
@Version: python 3.10
@Describe:
"""
# import sys
import time

import requests

from config import Config
from online_monitor.big_query.big_query import BigQuery
# sys.path.append("../")
from online_monitor.handle_sql.handle_sql import HandleSql


class HandleQuery:
    big_query = BigQuery(r"./cred/google_application_credentials.json")

    def __init__(self, big_query=None):
        if big_query:
            self.big_query = big_query

    @staticmethod
    def handle_version_name(info, ctop):
        if int(ctop) >= 2000:
            info['env'] = "prod"
        else:
            info['env'] = 'alpha'
        return info

    def handle_week_query(self, prod_version, alpha_version):
        """
        版本每周汇总数据
        :param prod_version:
        :param alpha_version:
        :return:
        """

    @classmethod
    def handle_offline_index_single_version(cls, offline_version_and_date):
        # 查询游玩平均Fps数量
        offline_intraday_info = cls.post_google_query_dataset_table(offline_version_and_date)
        offline_no_intraday_info = cls.post_google_query_dataset_table(offline_version_and_date, intraday=False)

        fps_sql = HandleSql.handle_avg_fps(offline_intraday_info)
        no_intraday_fps_sql = HandleSql.handle_avg_fps(offline_no_intraday_info)
        avg_fps = cls.big_query.get_avg_fps_info(fps_sql, no_intraday_sql=no_intraday_fps_sql)
        # 查询满帧=30的平均fps数据
        fps_sql_30 = HandleSql.handle_30_60_avg_fps(offline_intraday_info)
        no_intraday_fps_sql_30 = HandleSql.handle_30_60_avg_fps(offline_no_intraday_info)
        avg_fps_30full = cls.big_query.get_avg_fps_info(fps_sql_30, no_intraday_sql=no_intraday_fps_sql_30)
        # 查询满帧=60的平均fps数据
        fps_sql_60 = HandleSql.handle_30_60_avg_fps(offline_intraday_info, full_fps=60)
        no_intraday_fps_sql_60 = HandleSql.handle_30_60_avg_fps(offline_no_intraday_info, full_fps=60)
        avg_fps_60full = cls.big_query.get_avg_fps_info(fps_sql_60, no_intraday_sql=no_intraday_fps_sql_60)
        # Editor 平均fps
        editor_fps_sql = HandleSql.handle_editor_avg_fps_sql(offline_intraday_info)
        no_intraday_editor_fps_sql = HandleSql.handle_editor_avg_fps_sql(offline_no_intraday_info)
        edit_avg_fps = cls.big_query.get_avg_fps_info(editor_fps_sql, no_intraday_sql=no_intraday_editor_fps_sql)
        # 查询平均进房时间
        enter_sql = HandleSql.handle_enter_time(offline_intraday_info)
        no_intraday_enter_sql = HandleSql.handle_enter_time(offline_no_intraday_info)
        avg_enter = cls.big_query.get_avg_enter_room_time(enter_sql, no_intraday_sql=no_intraday_enter_sql)
        # 查询平均ab替换耗时 ab耗时不再同步
        # ab_sql = HandleSql.handle_ab_cost(offline_intraday_info)
        # no_intraday_ab_sql = HandleSql.handle_ab_cost(offline_no_intraday_info)
        # avg_ab = cls.big_query.get_avg_ab_cost_time(ab_sql, no_intraday_sql=no_intraday_ab_sql)
        # avg_ab = 0, 0, 0, 0, 0, 0
        offline_version = offline_version_and_date[1] if "%" not in offline_version_and_date[1] else \
        offline_version_and_date[1][:-1] + ".0"
        offline_info = dict(dat=offline_version_and_date[0], version=offline_version,
                            avg_fps=round(avg_fps[0], 2), total_fps=avg_fps[1],
                            android_avg_fps=round(avg_fps[2], 2), android_total_fps=avg_fps[3],
                            ios_avg_fps=round(avg_fps[4], 2), ios_total_fps=avg_fps[5],
                            avg_fps30=round(avg_fps_30full[0], 2), total_fps30=avg_fps_30full[1],
                            android_avg_fps30=round(avg_fps_30full[2], 2), android_total_fps30=avg_fps_30full[3],
                            ios_avg_fp30s=round(avg_fps_30full[4], 2), ios_total_fps30=avg_fps_30full[5],
                            avg_fps60=round(avg_fps_60full[0], 2), total_fps60=avg_fps_60full[1],
                            android_avg_fps60=round(avg_fps_60full[2], 2), android_total_fps60=avg_fps_60full[3],
                            ios_avg_fp60s=round(avg_fps_60full[4], 2), ios_total_fps60=avg_fps_60full[5],
                            editor_avg_fps=round(edit_avg_fps[0], 2), editor_total_fps=edit_avg_fps[1],
                            editor_android_avg_fps=round(edit_avg_fps[2], 2), editor_android_total_fps=edit_avg_fps[3],
                            editor_ios_avg_fps=round(edit_avg_fps[4], 2), editor_ios_total_fps=edit_avg_fps[5],
                            enter_time=round(avg_enter[0], 2), total_enter=avg_enter[1],
                            android_enter_time=round(avg_enter[2], 2), android_total_enter=avg_enter[3],
                            ios_enter_time=round(avg_enter[4], 2), ios_total_enter=avg_enter[5]
                            # ab_time=round(avg_ab[0], 2), total_ab=avg_ab[1],
                            # android_ab_time=round(avg_ab[2], 2), android_total_ab=avg_ab[3],
                            # ios_ab_time=round(avg_ab[4], 2), ios_total_ab=avg_ab[5]
                            )
        offline_info = cls.handle_version_name(offline_info, avg_fps[1])
        return offline_info

    @classmethod
    def handle_offline_query(cls, dat, prod_version, alpha_version):

        prod_info = [dat, prod_version, ""]
        alpha_info = [dat, alpha_version, ""]

        prod_offline_info = cls.handle_offline_index_single_version(prod_info)
        alpha_offline_info = cls.handle_offline_index_single_version(alpha_info)

        return prod_offline_info, alpha_offline_info

    @staticmethod
    def post_ctoe_rate(ctoe, ctop):

        total_success_exit_rate, android_success_exit_rate, ios_success_exit_rate = 0.0, 0.0, 0.0
        if int(ctop[1]) <= 0:
            return total_success_exit_rate, android_success_exit_rate, ios_success_exit_rate
        try:
            total_success_exit_rate = round(ctoe[0] / ctop[1], 5)
            if int(ctop[4]) <= 0:
                android_success_exit_rate = 0.0
            else:
                android_success_exit_rate = round(ctoe[1] / ctop[4], 5)
            if int(ctop[7]) <= 0:
                ios_success_exit_rate = 0.0
            else:
                ios_success_exit_rate = round(ctoe[2] / ctop[7], 5)
            if total_success_exit_rate > 1:
                total_success_exit_rate = 1.0
            if android_success_exit_rate > 1:
                android_success_exit_rate = 1.0
            if ios_success_exit_rate > 1:
                ios_success_exit_rate = 1.0
        except Exception:
            pass
        return round(float(total_success_exit_rate) * 100, 2), round(float(android_success_exit_rate) * 100, 2), \
               round(float(ios_success_exit_rate) * 100, 2)

    @staticmethod
    def post_google_query_dataset_table(info, intraday=True):
        i = info[:]
        table_prefix = Config.GOOGLE_BIGQUERY_DATASET_PREFIX
        d = i[0]
        if intraday:
            table = table_prefix + f"intraday_{d}"
        else:
            table = table_prefix + f"{d}"
        i[2] = table
        return i

    @classmethod
    def handle_engine_index_single_version(cls, info):
        """
        查询联机相关的指标数据，支持非当日数据查询
        :param info:
        :return:
        """
        # 用拼接好的sql，使用big query进行查询
        # 查询总进房数据
        info_intraday = cls.post_google_query_dataset_table(info)
        info_not_intraday = cls.post_google_query_dataset_table(info, intraday=False)

        ctop_sql_intraday = HandleSql.handle_ctop_params(info_intraday)
        # print(ctop_sql_intraday)
        ctop_sql_not_intraday = HandleSql.handle_ctop_params(info_not_intraday)
        # print(ctop_sql_intraday)
        ctop = cls.big_query.get_click_to_play_pv(ctop_sql_intraday, sql_not_intraday=ctop_sql_not_intraday)

        # 查询roomcode进房数据
        room_sql_intrady = HandleSql.handle_rc_sql(info_intraday)
        room_sql_not_intraday = HandleSql.handle_rc_sql(info_not_intraday)
        rc = cls.big_query.get_click_to_play_pv(room_sql_intrady, sql_not_intraday=room_sql_not_intraday,
                                                is_room_code=True)

        # ctop_latency = HandleSql.handle_enter_time(info)
        # 查询点击进入房间的耗时数据
        # click_cost = cls.big_query.get_avg_enter_room_time(ctop_latency)
        ctoe_sql = HandleSql.handle_ctoe_sql(info_intraday)
        ctoe_sql_not_intraday = HandleSql.handle_ctoe_sql(info_not_intraday)
        # 查询退出房间数据
        ctoe = cls.big_query.get_ctoe_info(ctoe_sql, sql_not_intraday=ctoe_sql_not_intraday)
        ctoe_rate = cls.post_ctoe_rate(ctoe, ctop)

        # exclude_quit_total_success_rate, exclude_quit_android_success_rate, exclude_quit_ios_success_rate
        engine_info = {
            'dat': info[0],
            "version": info[1],
            "total_success_rate": round(ctop[0], 2),
            "total_enter": ctop[1],
            "success_enter": ctop[2],
            "android_success_rate": round(ctop[3], 2),
            "android_total_enter": ctop[4],
            "android_success_enter": ctop[5],
            "ios_success_rate": round(ctop[6], 2),
            "ios_total_enter": ctop[7],
            "ios_success_enter": ctop[8],
            "total_quit": ctop[9],
            "android_quit": ctop[10],
            "ios_quit": ctop[11],
            "exclude_quit_total_success_rate": ctop[12],
            "exclude_quit_android_success_rate": ctop[13],
            "exclude_quit_ios_success_rate": ctop[14],
            "total_success_exit_rate": ctoe_rate[0],
            "android_success_exit_rate": ctoe_rate[1],
            "ios_success_exit_rate": ctoe_rate[2],
            "rc_success_rate": rc[0],
            "total_room_enter": rc[1],
            "room_success_enter": rc[2],
            "android_rc_success_rate": rc[3],
            "android_total_room_enter": rc[4],
            "android_room_success_enter": rc[5],
            "ios_rc_success_rate": rc[6],
            "ios_total_room_enter": rc[7],
            "ios_room_success_enter": rc[8],
            "exit_success_rate": ctoe[0],
            "total_exit": ctoe[1],
            "click_success_exit": ctoe[2]
        }
        engine_info = cls.handle_version_name(engine_info, ctop[1])
        # if engine_info['env'] == 'prod':
        # 查询平均ping值 + ping值区间分布 + SA地区分布
        avg_ping_sql = HandleSql.handle_avg_ping_sql(info_intraday)
        avg_ping_no_intraday_sql = HandleSql.handle_avg_ping_sql(info_not_intraday)
        avg_pings = cls.big_query.get_avg_ping_info(avg_ping_sql, no_intraday_sql=avg_ping_no_intraday_sql)
        engine_info['total'] = avg_pings[0]
        engine_info['avg_ping'] = avg_pings[1]
        engine_info['android_total'] = avg_pings[2]
        engine_info['android_avg_ping'] = avg_pings[3]
        engine_info['ios_total'] = avg_pings[4]
        engine_info['ios_avg_ping'] = avg_pings[5]
        engine_info['lt100_ms_rate'] = avg_pings[6][0]
        engine_info['gt100_le200_ms_rate'] = avg_pings[6][1]
        engine_info['gt200_le300_ms_rate'] = avg_pings[6][2]
        engine_info['gt300_ms_rate'] = avg_pings[6][3]
        engine_info['filipino_avg_ping'] = avg_pings[7]
        engine_info['indonesian_avg_ping'] = avg_pings[8]
        engine_info['vietnam_avg_ping'] = avg_pings[9]
        engine_info['mexico_avg_ping'] = avg_pings[10]
        engine_info['brazil_avg_ping'] = avg_pings[11]
        engine_info['us_avg_ping'] = avg_pings[12]
        if engine_info['env'] == 'prod':
            engine_health_res = cls.get_engine_health_and_prop_success_rate(Config.ENGINE_HEALTH_PROP_GET_PROD_URL)
            engine_health = cls.post_engine_health_rate(engine_health_res)
            # health_rate, prop_success_rate, total_game_count, bad_game_count, total_prop_count, failed_prop_count
            engine_info['health_rate'] = engine_health[0]
            engine_info['prop_success_rate'] = engine_health[1]
            engine_info['total_game_count'] = engine_health[2]
            engine_info['bad_game_count'] = engine_health[3]
            engine_info['total_prop_count'] = engine_health[4]
            engine_info['failed_prop_count'] = engine_health[5]
        return engine_info

    @classmethod
    def handle_engine_query(cls, dat, prod_version, alpha_version):

        prod_info = [dat, prod_version, ""]
        alpha_info = [dat, alpha_version, ""]

        prod_engine_info = cls.handle_engine_index_single_version(prod_info)
        alpha_engine_info = cls.handle_engine_index_single_version(alpha_info)

        return prod_engine_info, alpha_engine_info

    @classmethod
    def handle_ios_crash_oom_rate_query(cls, crash_date, version=None):

        if not version:
            sql = HandleSql.handle_ios_crash_and_oom_sql(crash_date)
        else:
            sql = HandleSql.handle_ios_crash_and_oom_sql(crash_date, version=version)
        res = cls.big_query.get_ios_crash_oom_rate(sql)
        print(res)

        ooms = dict()
        ooms['dat'] = crash_date
        ooms['reboot_all'] = res[0]
        ooms['normal_crash'] = res[1]
        ooms['foreground_oom'] = res[2]
        crash_mobiles = res[3]
        ooms = cls.post_mobile_and_times(ooms, crash_mobiles, "crashs")
        oom_mobiles = res[4]
        ooms = cls.post_mobile_and_times(ooms, oom_mobiles, "ooms")
        normal_crash_rate, foreground_oom_rate = cls.post_crash_oom_rate(res[0], res[1], res[2])
        ooms['normal_crash_rate'] = normal_crash_rate
        ooms['foreground_oom_rate'] = foreground_oom_rate
        return ooms

    @staticmethod
    def post_mobile_and_times(r, crashs: str, key):
        """
        前置处理前5的crash和oom机型和崩溃次数
        :param r:
        :param crashs:
        :return:
        """
        temp = crashs.split('+')
        result = []
        for item in temp:
            print(item)
            mobile, times = item.split(":")
            result.append([mobile, times])
        r[key] = result
        return r

    @staticmethod
    def post_crash_oom_rate(total, crash, oom):

        crash_rate, oom_rate = 0.0, 0.0
        if total <= 0:
            return crash_rate, oom_rate
        crash_rate = round((crash / total) * 100, 2)
        oom_rate = round((oom / total) * 100, 2)
        if crash_rate > 100:
            crash_rate = 100.0
        if oom_rate > 100:
            oom_rate = 100.0
        return crash_rate, oom_rate

    @staticmethod
    def get_engine_health_and_prop_success_rate(url, start_time=None, end_time=None):
        """
        :param url:
        :param start_time: 秒级时间戳
        :param end_time: 秒级时间戳
        :return: {"result": 0,"rmsg": "","total_game_count": 7561,"bad_game_count": 45,"total_prop_count": 115243,
                "failed_prop_count": 1562
                }
        """
        params = dict()
        res = dict()
        if start_time and end_time:
            params['start_time'] = start_time
            params['end_time'] = end_time
            try:
                res = requests.get(url=url, params=params).json()
            except Exception as e:
                return res
            return res
        end_time = int(time.time())
        start_time = end_time - 24 * 60 * 60
        params['start_time'] = start_time
        params['end_time'] = end_time
        try:
            res = requests.get(url=url, params=params).json()
        except Exception as e:
            return res
        return res

    @classmethod
    def post_engine_health_rate(cls, res: dict):

        total_game_count, bad_game_count, total_prop_count, failed_prop_count, = 0, 0, 0, 0
        health_rate, prop_success_rate = 0.0, 0.0
        res_code = res.get("result", None)
        if res_code != 0:
            return health_rate, prop_success_rate, total_game_count, bad_game_count, total_prop_count, failed_prop_count
        try:
            total_game_count = res['total_game_count']
            bad_game_count = res['bad_game_count']
            total_prop_count = res['total_prop_count']
            failed_prop_count = res['failed_prop_count']
        except Exception as e:
            return health_rate, prop_success_rate, total_game_count, bad_game_count, total_prop_count, failed_prop_count
        health_rate = cls.calc_success_rate(bad_game_count, total_game_count)
        prop_success_rate = cls.calc_success_rate(failed_prop_count, total_prop_count)
        return health_rate, prop_success_rate, total_game_count, bad_game_count, total_prop_count, failed_prop_count

    @staticmethod
    def calc_success_rate(fail_num, total):

        if total <= 0:
            success_rate = 0.0
        else:
            bad_rate = fail_num / total
            if bad_rate > 1:
                bad_rate = 1.0
            success_rate = round((1 - bad_rate) * 100, 2)
        return success_rate


if __name__ == "__main__":
    info = ["20220711", "1.34.0", ""]
    HandleQuery.handle_engine_index_single_version(info)
