# -*- coding: utf-8 -*-
"""
@Author: shining
@File: analyze.py
@Date: 2023/1/9 8:10 下午
@Version: python 3.9
@Describe: 分析twist结果
"""
from utils.csv_handler import *


def reward_enum(num, level=None):
    if num == 0:
        return "reward_type_no"
    if num == 1:
        return "reward_type_prop"
    if num == 2:
        if level == 2:
            return "reward_type_clothes_purple"
        elif level == 3:
            return "reward_type_clothes_blue"
    if num == 101:
        return "reward_type_gold"
    if num == 102:
        return "reward_type_souvenir"
    if num == 103:
        return "reward_type_potion"
    if num == 104:
        return "reward_type_expcard"


def rate(times, total):
    if total < 1 or times == 0:
        return 0.0
    if times > total:
        return 1.0
    return round(times / total, 2)


def classify_uids(gacha_rsp_path=None):
    """
    计算uid维度各个奖品的rate
    :return:
    """
    if not gacha_rsp_path:
        gacha_rsp_path = './result/gacha_rsp.csv'
    twist_res = CSVHandler.read_csv(gacha_rsp_path)
    res = twist_res[1:]
    uids = dict()
    for t in res:
        if t[1] in uids.keys():
            uids[t[1]].append(t)
        else:
            uids[t[1]] = []
            uids[t[1]].append(t)
    return uids


def calculate_uid_rate(uids):
    gacha_rate = []
    for k, v in uids.items():
        total = len(v)
        reward = {
            "reward_type_no": 0,
            "reward_type_prop": 0,
            "reward_type_clothes_purple": 0,
            "reward_type_clothes_blue": 0,
            "reward_type_gold": 0,
            "reward_type_souvenir": 0,
            "reward_type_potion": 0,
        }
        tmp = list()
        tmp.append(k)
        tmp.append(total)
        if v:
            for i, item in enumerate(v):
                reward[item[4]] += 1

        reward_type_no_rate = rate(reward['reward_type_no'], total)
        tmp.append(reward_type_no_rate)

        reward_type_prop_rate = rate(reward['reward_type_prop'], total)
        tmp.append(reward_type_prop_rate)

        reward_type_clothes_purple_rate = rate(reward['reward_type_clothes_purple'], total)
        tmp.append(reward_type_clothes_purple_rate)

        reward_type_clothes_blue_rate = rate(reward['reward_type_clothes_blue'], total)
        tmp.append(reward_type_clothes_blue_rate)

        reward_type_gold_rate = rate(reward['reward_type_gold'], total)
        tmp.append(reward_type_gold_rate)

        reward_type_souvenir_rate = rate(reward['reward_type_souvenir'], total)
        tmp.append(reward_type_souvenir_rate)

        reward_type_potion_rate = rate(reward['reward_type_potion'], total)
        tmp.append(reward_type_potion_rate)
        gacha_rate.append(tmp)

    return gacha_rate


def write_uid_rate_to_csv(rate, uid_rate_file_path=None):
    key = ['uid', 'times', "reward_type_no_rate", "reward_type_prop_rate", "reward_type_clothes_purple_rate",
           "reward_type_clothes_blue_rate", "reward_type_gold_rate",
           "reward_type_souvenir_rate", "reward_type_potion_rate"]
    if not uid_rate_file_path:
        uid_rate_file_path = './result/uid_rate.csv'
    CSVHandler.write_to_csv(rate, uid_rate_file_path, key=key)


def calculate_uid_rate_save_to_csv(gacha_rsp_path=None, uid_rate_file_path=None):
    """
    计算uid维度各个奖品的爆率
    :param gacha_rsp_path:
    :param uid_rate_file_path:
    :return:
    """
    uids = classify_uids(gacha_rsp_path=gacha_rsp_path)
    uid_gacha_rate = calculate_uid_rate(uids)
    write_uid_rate_to_csv(uid_gacha_rate, uid_rate_file_path=uid_rate_file_path)


def color_enum(num):
    if num == 1:
        return "orange"
    if num == 2:
        return "purple"
    if num == 3:
        return "blue"


def calculate_color_rate(file_name=None, result_file_path=None):
    """
    各颜色球概率
    :return:
    """
    color = {
        "orange": 0,
        "purple": 0,
        "blue": 0
    }
    if not file_name:
        file_name = './result/gacha_rsp.csv'
    twist_res = CSVHandler.read_csv(file_name)
    res = twist_res[1:]

    color_res = []
    if res:
        for i, item in enumerate(res):
            tmp = list()
            i = i + 1
            tmp.append(i)
            color[color_enum(int(item[2]))] += 1
            orange_rate = rate(color['orange'], i)
            tmp.append(orange_rate)

            purple_rate = rate(color['purple'], i)
            tmp.append(purple_rate)

            blue_rate = rate(color['blue'], i)
            tmp.append(blue_rate)
            color_res.append(tmp)

    if not result_file_path:
        result_file_path = './result/color_rate.csv'
    CSVHandler.write_to_csv(color_res, result_file_path, key=["times", "orange", "purple", "blue"])


def read_twist_res(file_path=None):
    gacha_rsp = './result/gacha_rsp.csv'
    if file_path:
        gacha_rsp = file_path
    twist_res = CSVHandler.read_csv(gacha_rsp)
    res = twist_res[1:]
    return res


def calculate(res):
    """
    计算概率
    :return:
    """

    reward = {
        "reward_type_no": 0,
        "reward_type_prop": 0,
        "reward_type_clothes_purple": 0,
        "reward_type_clothes_blue": 0,
        "reward_type_gold": 0,
        "reward_type_souvenir": 0,
        "reward_type_potion": 0,
    }
    gacha_rate = []
    if res:
        for i, item in enumerate(res):
            tmp = list()
            i = i + 1
            tmp.append(i)
            reward[item[4]] += 1
            reward_type_no_rate = rate(reward['reward_type_no'], i)
            tmp.append(reward_type_no_rate)

            reward_type_prop_rate = rate(reward['reward_type_prop'], i)
            tmp.append(reward_type_prop_rate)

            reward_type_clothes_purple_rate = rate(reward['reward_type_clothes_purple'], i)
            tmp.append(reward_type_clothes_purple_rate)

            reward_type_clothes_blue_rate = rate(reward['reward_type_clothes_blue'], i)
            tmp.append(reward_type_clothes_blue_rate)

            reward_type_gold_rate = rate(reward['reward_type_gold'], i)
            tmp.append(reward_type_gold_rate)

            reward_type_souvenir_rate = rate(reward['reward_type_souvenir'], i)
            tmp.append(reward_type_souvenir_rate)

            reward_type_potion_rate = rate(reward['reward_type_potion'], i)
            tmp.append(reward_type_potion_rate)
            gacha_rate.append(tmp)
    return gacha_rate


def write_gacha_rate_res(gacha_re, gacha_res_rate_path=None):
    key = ["times", "reward_type_no_rate", "reward_type_prop_rate", "reward_type_clothes_purple_rate",
           "reward_type_clothes_blue_rate", "reward_type_gold_rate",
           "reward_type_souvenir_rate", "reward_type_potion_rate"]
    if not gacha_res_rate_path:
        gacha_res_rate_path = './result/gacha_res_rate.csv'
    CSVHandler.write_to_csv(gacha_re, gacha_res_rate_path, key=key)


def calculate_gacha_prize_rate_to_csv(gacha_rsp_path=None, gacha_res_rate_path=None):
    """
    计算各个品类的爆率，并写入csv文件gacha_res_rate_path
    :param gacha_rsp_path:
    :param gacha_res_rate_path:
    :return:
    """
    res = read_twist_res(file_path=gacha_rsp_path)
    gacha_prize_rate = calculate(res)
    write_gacha_rate_res(gacha_prize_rate, gacha_res_rate_path=gacha_res_rate_path)
