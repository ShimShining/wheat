# -*- coding: utf-8 -*-
"""
@Author: shining
@File: account_choose_page.py
@Date: 2022/10/19 4:25 下午
@Version: python 3.9
@Describe: 登录三方账号选择页
"""
from base.UPath import UPath
from base.BP_app import BPApp
from config import Config
from pages.native.home_page.home_page import HomePage


class AccountChoosePage(BPApp):

    __back = {'android': UPath(name="id/header_back")}

    __facebook_login = {'android': UPath(host=True, name="id/facebookBtn"),
                        'ios': UPath(name="Continue with Facebook")}  # facebookBtn

    __google_login = {'android': UPath(host=True, resourceId="id/googleBtn"),
                      'ios': UPath(name="Continue with Google")}  # googleBtn

    __snapcha_login = {'android': UPath(host=True, name="id/snapchatBtn"),
                       'ios': UPath(name="Continue with Snapchat")}  # snapchatBtn

    __tiktok_login = UPath(host=True, name="id/tiktokBtn")  # tiktokBtn

    __google_account = {"android": UPath(host=False, text=Config.GOOGLE_ACCOUNT), "ios": ""}  # 添加google账号
    __google_testto = {'android': "", 'ios': UPath(name="Other")}  # "继续"点master环境击googol登录，在登录页第一次确认登录弹窗
    __login_text = {'android': UPath(host=False, text="选择帐号"), 'ios': UPath(name="选择帐号")}  # google登录选择账号二级确认页面goolge选择帐号

    def login_with_google(self, acc=None):
        """
        使用谷歌登录
        :param acc: 谷歌账号，传入后使用这个账号登录
        """
        if acc:
            self.__google_account.text = acc
        self.sleep(3)
        self.find_and_click(self.__google_login, timeout=7)
        self.find_and_click(self.__google_account, timeout=12)
        # todo 需要判断是否需要注册，是否需要选择账号
        return HomePage(self.poco)
