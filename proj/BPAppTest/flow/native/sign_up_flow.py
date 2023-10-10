# -*- coding: utf-8 -*-
"""
@Author: shining
@File: sign_up_flow.py
@Date: 2022/10/24 3:16 下午
@Version: python 3.9
@Describe: 注册新账号流程
"""
from pages.native.login_register.login_page import LoginPage


class SignUpFlow:

    @staticmethod
    def sign_up(device=None):

        lp = LoginPage(mutil_device=device)
        lp.sign_up_new_user().goto_gender_choose_page().choose_gender_to_avatar().goto_profile_picture().\
            goto_follow_creator_page().goto_finish_page().goto_create_wallet_page().goto_new_user_group_server()

        lp.restart_app()
