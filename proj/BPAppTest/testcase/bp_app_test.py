# -*- coding: utf-8 -*-
"""
@Author: shining
@File: base_app_test.py
@Date: 2022/10/20 1:50 下午
@Version: python 3.9
@Describe: APP测试基类，初始状态预期：未登录，已登录
1. 已登录不需要登录
2. 未登录
    a. 登录
    b. 注册新账号
3. 弹窗处理
    a. 循环
    b. 异常捕获
    c. 底层异常捕获 弹窗独立封装黑名单 拿到pageSource判断是否包含，包含则点掉（可以实现）
    d. 观察者模式（推荐）
"""
from base.base_test import BaseTest


class BPAppTest(BaseTest):

    pass
