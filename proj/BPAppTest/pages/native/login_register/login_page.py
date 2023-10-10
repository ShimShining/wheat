# -*- coding: utf-8 -*-
"""
@Author: shining
@File: login_page.py
@Date: 2022/5/25 8:03 下午
@Version: python 3.9
@Describe:
"""
from base.UPath import UPath
from base.BP_app import BPApp
from pages.native.home_page.home_page import HomePage
from pages.native.login_register.birthday_page import BirthdayPage


class LoginPage(BPApp):
    # logo图标
    __BP_logo = {'android': UPath(name="id/BPLogo"), 'ios': ""}
    # 登录 {'android':UPath(host=True, name=""),'ios':UPath(name="")}$
    # 游客注册按钮
    __sign_up = {'android': UPath(name="id/signUpBtn")}
    # 隐私和服务说明
    __term_of_services = {'android': UPath(name='id/termOfServices')}
    # 已拥有账号
    __already_have_acc = {'android': UPath(name="id/alreadyHaveAnAccount")}
    # 退出登录后 直接登录按钮
    __log_in = (UPath(name="id/loginBtn"), None)
    __user_other_account = (UPath(name="id/userOtherAccount"), None)
    __create_new_account = (UPath(name="id/userOtherAccount"), None)

    # install bug popup
    __install_bug_popup = (UPath(name="id/ib_core_lyt_onboarding_pager_fragment"), '')

    def sign_up_new_user(self):
        """
        注册新用户
        :return:
        """
        # self.handle_install_bug_popup()
        try:
            self.find_and_click(self.__sign_up)
            return BirthdayPage(self.poco)
        except Exception as e:
            self.find_and_click(self.__create_new_account)
        return BirthdayPage(self.poco)

    def goto_account_page(self):
        """
        进入已有账号三方登录界面
        :return:
        """
        if self.is_exist(self.__already_have_acc):
            self.find_and_click(self.__already_have_acc)
        else:
            self.find_and_click(self.__user_other_account)
        from pages.native.login_register.account_choose_page import AccountChoosePage
        return AccountChoosePage(self.poco)

    def remember_log_in_same_acc(self):
        """
        已帮点三方的账号，退出再次登录
        :return:
        """
        # self.handle_install_bug_popup()
        self.find_and_click(self.__log_in)
        return HomePage(self.poco)

    def assert_in_login_page(self):
        self.wait_for_visible(self.__already_have_acc, timeout=10)

        assert self.is_exist(self.__already_have_acc) or self.is_exist(self.__user_other_account)

    def is_login_page(self):

        return (self.is_exist(self.__already_have_acc) or self.is_exist(self.__user_other_account))\
               and self.is_exist(self.__term_of_services)

    def handle_install_bug_popup(self):

        self.log.info("开始处理弹窗")
        self.sleep(13)
        self.log.info("等待结束")
        if self.is_exist(self.__install_bug_popup):
            self.random_click(0.1, 0.1)
            self.log.info("已经处理弹窗")
