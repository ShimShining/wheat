# -*- codeing = utf-8 -*-
# @Time :2022/11/14 3:18 下午
# @Author :liuliwen
# @File : test_my_public_profile.py
# @Software :个人主页模块

from pages.native.home_page.home_page import HomePage
from pages.native.self_profie_manage.self_change_picture import ChangeProfilePicture, Choose_a_selfie
from pages.native.self_profie_manage.self_my_public_profile import PublicHomepaga
from base.base_app import BaseApp

#切换头像
class TestMyHomepage():
    home = HomePage()
    exists = BaseApp()

    def setup(self):
        self.image = HomePage()
        self.picture = ChangeProfilePicture()
        self.profile = PublicHomepaga()
        self.selfie = Choose_a_selfie()

    # 个人公共主页更换头像todo 断言
    def test_change_avatar(self):
        """
        "从首页进入到个人主页-点击头像-切换头像"
        """
        # 首页-点击头像
        self.image.is_home_page()
        # # 进入个人主页点击头像
        self.image.goto_personal_page()
        # #点击更换头像按钮-更换posest
        self.profile.goto_my_avatar().goto_Change_picture_button()
        # #选择形象-保存
        self.picture.goto_poses()
        self.home.log.info("============> 开始进入avatar")
        self.selfie.choose_a_selfie()
        #assert self.exists.air_assert_exists(self.selfie.exists_selfie_finish(), msg="人物动作展示正常")
        self.selfie.fenish_button()
        self.home.log.info("============> 切换头像成功")

