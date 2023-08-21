# -*- coding: utf-8 -*-
"""
@Author: shining
@File: twist_gacha.py
@Date: 2022/12/27 8:07 下午
@Version: python 3.9
@Describe: 扭蛋机
"""
import random
import threading
import time
import os
import codecs

from proj.BPServiceTest.utils.csv_handler import *
from proj.BPServiceTest.utils.web3_tools import *
from proj.BPServiceTest.utils.draw import *
from proj.BPServiceTest.business.lottry.gacha import Gacha
from proj.BPServiceTest.tools.twist.generate_new_twist_user import *
from proj.BPServiceTest.utils.my_thread import MyThread


def twist(user_info, downtown_id="", times=1):
    """
    发起扭蛋
    :return:
    """
    t = Gacha()
    r = t.post_gacha(user_info[0], downtown_id=downtown_id, times=times, token=user_info[1], walletAddress=user_info[2])
    return r


def save(user_info, r, times, save_path=None):
    """
    保存抽奖记录
    :param user_info:
    :param r:
    :param times:
    :param save_path:
    :return:
    """
    if r['result'] != 0:
        return
    key = ['times', 'uid', 'rewardLevel', 'rewardType', "rewardTypeName"]
    reward_list = r['data']['rewardList']
    for reward in reward_list:
        tmp = []
        tmp.append(times)
        times += 1
        tmp.append(user_info[0])
        tmp.append(reward['rewardLevel'])
        tmp.append(reward['rewardType'])
        r_type_name = reward_enum(reward['rewardType'], level=reward['rewardLevel'])
        tmp.append(r_type_name)
        if not save_path:
            save_path = './result/gacha_rsp.csv'
        CSVHandler.write_to_csv([tmp], save_path, key=key)


def run_twist(file_name, downtown_id="", times=1):
    """
    :param file_name:
    :param times:
    :return:
    """
    users = CSVHandler.read_csv(file_name)
    for i, user in enumerate(users):
        if "uid" in user:
            continue
        coupons = int(user[6])
        if times == 1:
            for j in range(coupons):
                r = twist(user, downtown_id=downtown_id, times=times)
                time.sleep(5)
                save(user, r, i * (j + 1))
        else:
            gacha_times = coupons // times
            for j in range(gacha_times):
                r = twist(user, downtown_id=downtown_id, times=times)
                time.sleep(7)
                save(user, r, i * j * times + 1)


def async_twist(user, times=1, complex_gacha=False, ten_times=0, downtown_id=""):
    if "uid" in user:
        return

    coupons = int(user[6])
    if not complex_gacha:
        if times == 1:
            for j in range(coupons):
                twist(user, downtown_id=downtown_id, times=times)
                time.sleep(5)
        else:
            gacha_times = coupons // times
            for j in range(gacha_times):
                twist(user, downtown_id=downtown_id, times=times)
                time.sleep(6)
    else:
        single_gacha = coupons - ten_times * 10
        if ten_times * 10 > coupons:
            ten_times = coupons // 10
        for k in range(ten_times):
            twist(user, downtown_id=downtown_id, times=10)
            time.sleep(6)
        if single_gacha <= 0:
            return
        for j in range(single_gacha):
            twist(user, downtown_id=downtown_id, times=1)
            time.sleep(5)


def mutil_process_twist(twist_users, complex_gacha=True, ten_times=3, downtown_id=""):

    user_nums = len(twist_users)
    process_nums = 10
    if user_nums < process_nums:
        for user in twist_users:
            async_twist(user, complex_gacha=complex_gacha, ten_times=ten_times)
    else:
        for i in range(user_nums // process_nums):
            threads = []
            twist_user1 = {
                "complex_gacha": True,
                "ten_times": random.randint(5, 10),
                "downtown_id": downtown_id
            }
            twist1 = MyThread(async_twist, args=twist_users[i], kwargs=twist_user1)
            twist1.start()
            threads.append(twist1)
            twist_user2 = {
                "complex_gacha": True,
                "ten_times": random.randint(2, 8),
                "downtown_id": downtown_id
            }
            twist2 = MyThread(async_twist, args=twist_users[i+1], kwargs=twist_user2)
            twist2.start()
            threads.append(twist2)
            twist_user3 = {
                "complex_gacha": True,
                "ten_times": random.randint(4, 7),
                "downtown_id": downtown_id
            }
            twist3 = MyThread(async_twist, args=twist_users[i + 2], kwargs=twist_user3)
            twist3.start()
            threads.append(twist3)
            twist_user4 = {
                "complex_gacha": True,
                "ten_times": random.randint(3, 5),
                "downtown_id": downtown_id
            }
            twist4 = MyThread(async_twist, args=twist_users[i+3], kwargs=twist_user4)
            twist4.start()
            threads.append(twist4)

            twist_user5 = {
                "complex_gacha": True,
                "ten_times": random.randint(1, 5),
                "downtown_id": downtown_id
            }
            twist5 = MyThread(async_twist, args=twist_users[i + 4], kwargs=twist_user5)
            twist5.start()
            threads.append(twist5)

            twist_user6 = {
                "complex_gacha": True,
                "ten_times": random.randint(0, 5),
                "downtown_id": downtown_id
            }
            twist6 = MyThread(async_twist, args=twist_users[i + 5], kwargs=twist_user6)
            twist6.start()
            threads.append(twist6)

            twist_user7 = {
                "complex_gacha": True,
                "ten_times": random.randint(2, 5),
                "downtown_id": downtown_id
            }
            twist7 = MyThread(async_twist, args=twist_users[i + 6], kwargs=twist_user7)
            twist7.start()
            threads.append(twist7)

            twist_user8 = {
                "complex_gacha": True,
                "ten_times": random.randint(3, 5),
                "downtown_id": downtown_id
            }
            twist8 = MyThread(async_twist, args=twist_users[i + 7], kwargs=twist_user8)
            twist8.start()
            threads.append(twist8)

            twist_user9 = {
                "complex_gacha": True,
                "ten_times": random.randint(4, 5),
                "downtown_id": downtown_id
            }
            twist9 = MyThread(async_twist, args=twist_users[i + 8], kwargs=twist_user9)
            twist9.start()
            threads.append(twist9)

            twist_user10 = {
                "complex_gacha": True,
                "ten_times": random.randint(0, 5),
                "downtown_id": downtown_id
            }
            twist10 = MyThread(async_twist, args=twist_users[i + 9], kwargs=twist_user10)
            twist10.start()
            threads.append(twist10)

            # twist_user11 = {
            #     "complex_gacha": True,
            #     "ten_times": random.randint(1, 10),
            #     "downtown_id": downtown_id
            # }
            # twist11 = MyThread(async_twist, args=twist_users[i + 10], kwargs=twist_user11)
            # twist11.start()
            # threads.append(twist11)
            # twist_user12 = {
            #     "complex_gacha": True,
            #     "ten_times": random.randint(1, 8),
            #     "downtown_id": downtown_id
            # }
            # twist12 = MyThread(async_twist, args=twist_users[i + 11], kwargs=twist_user12)
            # twist12.start()
            # threads.append(twist12)
            # twist_user13 = {
            #     "complex_gacha": True,
            #     "ten_times": random.randint(2, 7),
            #     "downtown_id": downtown_id
            # }
            # twist13 = MyThread(async_twist, args=twist_users[i + 12], kwargs=twist_user13)
            # twist13.start()
            # threads.append(twist13)
            # twist_user14 = {
            #     "complex_gacha": True,
            #     "ten_times": random.randint(2, 5),
            #     "downtown_id": downtown_id
            # }
            # twist14 = MyThread(async_twist, args=twist_users[i + 13], kwargs=twist_user14)
            # twist14.start()
            # threads.append(twist14)
            #
            # twist_user15 = {
            #     "complex_gacha": True,
            #     "ten_times": random.randint(3, 5),
            #     "downtown_id": downtown_id
            # }
            # twist15 = MyThread(async_twist, args=twist_users[i + 14], kwargs=twist_user15)
            # twist15.start()
            # threads.append(twist15)
            #
            # twist_user16 = {
            #     "complex_gacha": True,
            #     "ten_times": random.randint(4, 5),
            #     "downtown_id": downtown_id
            # }
            # twist16 = MyThread(async_twist, args=twist_users[i + 15], kwargs=twist_user16)
            # twist16.start()
            # threads.append(twist16)
            #
            # twist_user17 = {
            #     "complex_gacha": True,
            #     "ten_times": random.randint(1, 5),
            #     "downtown_id": downtown_id
            # }
            # twist17 = MyThread(async_twist, args=twist_users[i + 16], kwargs=twist_user17)
            # twist17.start()
            # threads.append(twist17)
            #
            # twist_user18 = {
            #     "complex_gacha": True,
            #     "ten_times": random.randint(1, 5),
            #     "downtown_id": downtown_id
            # }
            # twist18 = MyThread(async_twist, args=twist_users[i + 17], kwargs=twist_user18)
            # twist18.start()
            # threads.append(twist18)
            #
            # twist_user19 = {
            #     "complex_gacha": True,
            #     "ten_times": random.randint(1, 5),
            #     "downtown_id": downtown_id
            # }
            # twist19 = MyThread(async_twist, args=twist_users[i + 18], kwargs=twist_user19)
            # twist19.start()
            # threads.append(twist19)
            #
            # twist_user20 = {
            #     "complex_gacha": True,
            #     "ten_times": random.randint(1, 5),
            #     "downtown_id": downtown_id
            # }
            # twist20 = MyThread(async_twist, args=twist_users[i + 19], kwargs=twist_user20)
            # twist20.start()
            # threads.append(twist20)

            thread_num = len(threading.enumerate())
            print(f">>>>>>>>>>>>>>>>>>Join 前线程数量==【{thread_num}】!!!!")
            for t in threads:
                t.join()

            thread_num = len(threading.enumerate())
            print(f">>>>>>>>>>>>>>>>>>Join后当前线程数量==【{thread_num}】!!!!")
        if user_nums % process_nums != 0:
            mutil_process_twist(twist_users[-(user_nums % process_nums):])


def draw_gacha_rate_trend(file_path=None):
    if not file_path:
        file_path = './result/gacha_res_rate.csv'
    data = CSVHandler.read_csv(file_path)
    html_file_name = file_path.split("/")[-1].split(".")[0] if file_path else "twist_rate"
    dat = data[1:]
    Draw.generate_rate_trend(dat).render(f'./result/{html_file_name}.html')


def draw_color_rate_trend(file_path=None):
    if not file_path:
        file_path = './result/color_rate.csv'
    d = CSVHandler.read_csv(file_path)
    html_file_name = file_path.split("/")[-1].split(".")[0] if file_path else "color_rate"
    dat = d[1:]
    Draw.generate_color_rate_trend(dat).render(f"./result/{html_file_name}.html")


if __name__ == '__main__':

    start_time = time.time()
    # 前置操作，./tools/twist目录下新建目录./result
    # 运行时：
    #     第一步：创建25个user，写入csv 第二步： 开发添加扭蛋券 已剥离出去，可创建新用户+充值扭蛋券一起
    # generate_twist_users(num=1)

    # 第二步：读取user数据
    users = CSVHandler.read_csv(file_path="./result/twist_1000user.csv")[1:]
    # print(users)

    # 第3步：发起扭蛋
    # run_twist("./result/twist_user1672813872.csv")
    # downtown_id:
    # teambud_downtown4_1：太空
    # teambud_downtown5_1：地牢
    # teambud_downtown2_1：山谷
    # teambud_downtown3_1：沙漠
    mutil_process_twist(users, complex_gacha=True, downtown_id="teambud_downtown2_1")
    # mutil_process_twist(users, complex_gacha=True, downtown_id="teambud_downtown5_1")
    # mutil_process_twist(users, complex_gacha=True, downtown_id="teambud_downtown2_1")
    # mutil_process_twist(users, complex_gacha=True, downtown_id="teambud_downtown3_1")


    # 第五步：分析球类成功率
    # calculate_color_rate()
    #
    # color_rate = CSVHandler.read_csv('../result/color_rate.csv')
    # data = color_rate[1:]
    # print(data)
    # Draw.generate_color_rate_trend(data).render("./result/color_rate.html")

    # 计算单uid的成功率
    # uids = classify_uids()
    # res = calculate_uid_rate(uids)
    # write_uid_rate_to_csv(res)
    end_time = time.time()
    print(f"执行耗时{int(end_time - start_time) / 3600} 小时")
