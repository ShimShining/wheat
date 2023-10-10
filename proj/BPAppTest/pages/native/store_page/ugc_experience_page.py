# -*- coding: utf-8 -*-
"""
@Author: shining
@File: ugc_experience_page.py
@Date: 2022/11/23 3:28 下午
@Version: python 3.9
@Describe: 商场tab -> Experience page
"""
from base.UPath import UPath
from base.BP_app import BPApp
from pages.native.home_page.map_detail_page import MapDetailPage
from pages.native.self_profie_manage.self_profile_manage import SelfProfileManage
import app_global_variable as agv


class UGCExperiencePage(BPApp):
    # 地图banner [{'android':UPath(host=True, name=""),'ios':UPath(name="")}$]
    __banner_view_btn = {'android': UPath(host=False, text="View"), 'ios': ""}  # 进入到地图详情
    __drafts_home = {'android': UPath(name="id/back"), 'ios': ""}  # 草稿箱返回到首页

    # __friend = (UPath(name="id/friendIcon"), "")  # 首页添加好友
    # __notification = UPath(name="id/notificationIcon")  # 通知
    # __explore = UPath(host=False, text="Explore")  # Explore  todo text文本抽象为多语言的key
    # __for_you = (UPath(host=False, text="For You"), "")  # For You todo text文本抽象为多语言的key

    # 中间部分
    __banner_view = (UPath(name="id/view"), '')
    __maps = (UPath(name="id/cslRoot"), '')  # 每一个地图卡片的poco
    __view_alls = (UPath(), '')

    # 弹窗
    __check_in_rewards = (UPath(name='id/title'), '')

    # 关联页面元素
    __join_public_server = (UPath(name="id/joinPublicRoom"), '')
    __back = (UPath(name="id/back"), '')
    __ugc_detail_back = (UPath(name='id/ugcClothDetailBack'), '')
    __ugc_prop_back = (UPath(name='id/ugcPropDetailBack'), '')
    __dc_exclusive = (UPath(name='id/cardTopView'), '')  # 需要某dc才能进入地图

    def is_home_page(self):

        """
        根据元素判断是否是首页
        :return: True and False
        """
        self.handle_home_page_popup()
        # self.handle_daily_check_in_popup()
        return self.is_exist(self.__home_tab) and self.is_exist(self.__enter_code) and self.is_exist(self.__explore)

    def enter_banner_map_detail(self, times=7, dc_need=True):
        """
        进入banner 地图详情页: 循环查找banner里符合要求的地图详情页
        :return:
        """
        t = 0
        while True:
            self.log.info(f"这是第{t + 1}次查找")
            if t > times:
                break
            t += 1
            if self.is_exist(self.__banner_view_btn):
                self.find_and_click(self.__banner_view_btn)
                if self.is_exist(self.__join_public_server):
                    if (dc_need and self.is_exist(self.__dc_exclusive)) or (
                            not dc_need and not self.is_exist(self.__dc_exclusive)):
                        break
                    else:
                        self.log.info("inner __banner_view_btn back....")
                        self.air_keyboard("BACK")
                        # self.air_swipe((50, 900), (150, 980))
                        self.sleep(4)
                else:
                    self.log.info("__banner_view_btn back....")
                    self.air_keyboard("BACK")
                    # self.air_swipe((50, 900), (150, 980))
                    self.sleep(4)
            elif self.is_exist(self.__banner_view):
                if self.is_exist(self.__join_public_server):
                    if (dc_need and self.is_exist(self.__dc_exclusive)) or (
                            not dc_need and not self.is_exist(self.__dc_exclusive)):
                        break
                    else:
                        self.log.info("inner __banner_view back....")
                        self.air_keyboard("BACK")
                        # self.air_swipe((50, 900), (150, 980))
                        self.sleep(4)
                else:
                    self.log.info("__banner_view back....")
                    self.air_keyboard("BACK")
                    # self.air_swipe((50, 900), (150, 980))
                    self.sleep(4)
        return MapDetailPage(self.poco)

    def goto_personal_page(self):
        """
        进入个人主页管理
        :return:
        """
        self.handle_home_page_popup()
        self.find_and_click(self.__head_image)
        self.sleep(1)
        return SelfProfileManage()

    def assert_tap_to_create_exists(self):

        assert self.wait_for_exist(self.__tap_to)
        return self

    def handle_daily_check_in_popup(self):
        if agv._get('check_in'):
            return
        self.wait_for_visible(self.__check_in_rewards, timeout=5)

        if self.is_exist(self.__check_in_rewards):
            self.find_and_click(self.__home_tab)
            agv._set('check_in', True)

    def handle_tap_to_create_popup(self):
        if agv._get('tap_to_create'):
            return
        self.wait_for_visible(self.__tap_to, timeout=5)
        if self.is_exist(self.__tap_to):
            self.find_and_click(self.__home_tab)
            agv._set('tap_to_create', True)

    def handle_home_page_popup(self, check_times=2):

        for i in range(check_times):
            self.handle_daily_check_in_popup()
            self.handle_tap_to_create_popup()

    def goto_first_section_first_map(self):
        """
        进入第一个section，第一个地图
        :return:
        """
        maps = self.finds(self.__maps)
        print(maps)
        print(maps[0])
        print(type(maps[0]))


if __name__ == '__main__':
    h = UGCExperiencePage(mutil_device="aaa")
    print(h)

