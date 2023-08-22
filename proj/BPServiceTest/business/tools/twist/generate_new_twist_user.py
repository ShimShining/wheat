# -*- coding: utf-8 -*-
"""
@Author: shining
@File: generate_new_twist_user.py
@Date: 2023/1/9 4:35 下午
@Version: python 3.9
@Describe:
1. 生成新用户
2. 生成钱包，并绑定
3. 充值太空，峡谷，沙漠和地牢扭蛋券
4. 写入csv文件
"""
import uuid
import time
import os
import codecs

from proj.BPServiceTest.utils.csv_handler import *
from proj.BPServiceTest.utils.web3_tools import *
from proj.BPServiceTest.utils.draw import *
from proj.BPServiceTest.business.basal.login import Login
from proj.BPServiceTest.business.dc.my_wallet import MyWallet, MyWalletHostToBUDX
from proj.BPServiceTest.business.pay.pay import Pay


def get_new_user():
    """
    获取新用户
    :return:
    """
    login = Login()
    open_id = uuid.uuid4()
    stmp = str(int(time.time() * 1000))
    tmp = str(open_id).replace('-', '')
    open_id = tmp + "-" + stmp
    # print(open_id)
    info = {
        "provider": "tourist",
        "open_id": open_id
    }
    r = login.login_v2(provider=info["provider"], open_id=info["open_id"], is_finish=False)
    r = login.login_v2(provider=info["provider"], open_id=info["open_id"], is_finish=True)
    uid = r["data"]["userInfo"]["uid"]
    token = r["data"]["token"]
    return uid, token


def bind_wallet():
    """
    创建并绑定钱包
    :return:
    """
    wal = Web3Tools.create_new_ETH_wallet()
    wallet_host_budx = MyWalletHostToBUDX()
    body = {"walletAddress": wal['address'], "walletName": "bud"}
    uid, token = get_new_user()
    time.sleep(3)
    h = {
        "uid": uid,
        "token": token
    }
    r = wallet_host_budx.post_bind_address(body, **h)
    if r['result'] != 0:
        raise Exception(f"uid={uid}绑定钱包address={wal['address']}失败")

    return uid, token, wal


def set_gacha_coupons(uid, token, type_=3, tickets=1, **kwargs):
    pay = Pay()
    r = pay.post_gash_recharge(uid, tickets, type_=type_, token=token, **kwargs)
    # print(r)
    if r['result'] != 0:
        raise Exception(f"uid={uid}充值扭蛋券失败")
    return r


def set_gacha_to_exist_users():
    users = CSVHandler.read_csv(file_path="./result/twist_1000user.csv")[1:]
    for user in users:
        set_gacha_coupons(user[0], user[1], tickets=1000)
        time.sleep(2)


def generate_twist_users(num=1, file_name=None, coupons=1000):
    # users = []
    tmp = str(int(time.time()))
    write_path = f"./result/twist_user{tmp}.csv"
    if file_name:
        write_path = file_name
    key = ["uid", 'token', 'address', 'privateKey', 'publicKey', 'mnemonic', 'coupons']

    for i in range(num):
        tmp = []
        uid, token, wal = bind_wallet()
        # 添加太空扭蛋券
        set_gacha_coupons(uid, token, tickets=coupons, walletAddress=wal['address'])
        # # 添加峡谷扭蛋券
        # set_gacha_coupons(uid, token, type_=4, tickets=coupons, walletAddress=wal['address'])
        # # 添加沙漠扭蛋券
        # set_gacha_coupons(uid, token, type_=5, tickets=coupons, walletAddress=wal['address'])
        # # 添加地牢扭蛋券
        # set_gacha_coupons(uid, token, type_=6, tickets=coupons, walletAddress=wal['address'])
        tmp.append(uid)
        tmp.append(token)
        tmp.append(wal['address'])
        tmp.append(wal['privateKey'])
        tmp.append(wal['publicKey'])
        tmp.append(wal['mnemonic'])
        tmp.append(120)
        # users.append(tmp)

        if not os.path.exists(write_path):
            CSVHandler.write_to_csv([tmp], write_path, key=key)
        else:
            content = CSVHandler.read_csv(write_path)
            if content and content[0] == key:
                CSVHandler.write_to_csv([tmp], write_path)
            else:
                CSVHandler.write_to_csv([tmp], write_path, key=key)


def modify_user_coupons(coupons=100):

    users = CSVHandler.read_csv(file_path="./result/twist_user1673576633.csv")
    for user in users:
        if "uid" in user:
            continue
        user[6] = coupons

    CSVHandler.write_to_csv(users, "./result/twist_1000user.csv")


if __name__ == '__main__':
    start_time = time.time()
    # 生成新用户，并充值3-space gacha 4-vally gasha 5-desert gasha 6-dungeon gasha扭蛋券
    num = 109
    # generate_twist_users(num=num)
    set_gacha_to_exist_users()
    #
    end_time = time.time()
    # modify_user_coupons(coupons=120)
    print(f"===============>生成{num}个user，执行耗时{end_time - start_time}<=========================")
