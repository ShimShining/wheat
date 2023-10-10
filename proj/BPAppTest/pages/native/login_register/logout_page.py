# -*- coding: utf-8 -*-
"""
@Author: shining
@File: logout_page.py
@Date: 2022/5/25 8:05 下午
@Version: python 3.9
@Describe:
"""
from base.UPath import UPath
from base.BP_app import BPApp
from pages.native.login_register.login_page import LoginPage


class LogoutPage(BPApp):
    # {'android': UPath(host=True, name=""), 'ios': UPath(name="")}$
    __setting = {'android': UPath(host=True, name="id/setting"), 'ios': UPath(name="Image")}  # 设置按钮
    __logout = {'android': UPath(host=True, name="id/logOutLayout"), 'ios': UPath(label="Log out")}  # 退出入口
    #    __confirm = UPath(host=True, name="id/setting")  # 确认按钮弹窗
    __yes_btn = {'android': UPath(host=True, resourceId="confirm"), 'ios': UPath(label="Yes")}  # Yes
    __no_btn = UPath(text="No")  # No
