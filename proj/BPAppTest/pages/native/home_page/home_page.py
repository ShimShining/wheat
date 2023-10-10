# -*- coding: utf-8 -*-
"""
@Author: shining
@File: home_page.py
@Date: 2022/5/25 8:06 下午
@Version: python 3.9
@Describe:
"""
from base.UPath import UPath
from base.BP_app import BPApp
import app_global_variable as agv


class HomePage(BPApp):
    # 首页头部展示
    __head_image = {'android': UPath(host=True, name="id/headImage"), 'ios': ""}  # 头像
    __enter_code = (UPath(name="id/enterRoomCode"), "")  # 房间码进房按钮
    __search = (UPath(name="id/iv_homepage_search"), "")  # 搜索
    __friend = (UPath(name="id/friendIcon"), "")  # 首页添加好友
    __notification = UPath(name="id/notificationIcon")  # 通知
    # __explore = UPath(host=False, text="Explore")  # Explore  todo text文本抽象为多语言的key
    # __for_you = (UPath(host=False, text="For You"), "")  # For You todo text文本抽象为多语言的key

    __home_to = {'android': UPath(text="Tap to create"), 'ios': ""}

    # 首页底部tab
    __home_tab = (UPath(name="id/homeIcon"), "")  # 首页home按钮
    __props_tab = (UPath(name="id/propsStoreIcon"), "")  # 素材按钮
    __feed_tab = (UPath(name="id/studioIcon"), "")  # Feed tab
    __chat_tab = (UPath(name="id/chatIcon"), "")  # DM
    __group_server_tab = (UPath(name="id/groupIcon"), "")  # Group server
    # 弹窗
    __check_in_rewards = (UPath(name='id/title'), '')  # 奖励弹窗

    # 大世界相关
    __create_private_server = (UPath(host=False, text="Create Private Server"), "")
    __join_public_server = (UPath(name="id/joinPublicRoom"), "")
    __public_servers = (UPath(name="id/publicServerLayout"), '')

    # 故事模式入口
    __story = (UPath(name='id/storyCreate'), '')

    __avatar = (UPath(name="id/avatarImg"), '')
    __hangout = (UPath(name='id/hangoutImg'), '')
    __wallet = (UPath(name='id/walletImg'), '')

    # 首页浮窗
    __airdrops = (UPath(name="id/cslRoot"), "")  # index=0 grnd, index=1 pass card, index=2 daily rewards

    # 关联页面元素
    __back = (UPath(name="id/back"), '')
    __claim = (UPath(name="id/claimBtn"), "")
    __claim_title = (UPath(name="id/collaboration"), "")
    __get_it_pass = (UPath(name="id/getBtn"), "")
    __pass_title = (UPath(name="id/title"), "")
    __rewards_back = (UPath(name="id/ivClockInBack"), "")

    def home_clike_image(self):
        self.find_and_click(self.__head_images)

    def is_home_page(self):
        self.handle_home_page_popup()
        return self.is_exist(self.__home_tab) and self.is_exist(self.__enter_code) and self.is_exist(self.__story)

    def assert_is_home_page(self):

        """
        断言是否在首页
        :return: True and False
        """
        self.handle_home_page_popup()
        # self.log.info(f"self.is_exist(self.__home_tab)= {self.is_exist(self.__home_tab)}")
        # self.log.info(f"self.is_exist(self.__enter_code)= {self.is_exist(self.__enter_code)}")
        # self.log.info(f"self.is_exist(self.__story)= {self.is_exist(self.__story)}")
        # self.log.info(f"is_home_page == {self.is_exist(self.__home_tab) and self.is_exist(self.__enter_code) and \
        # self.is_exist(self.__story)}")
        assert self.is_exist(self.__home_tab) and self.is_exist(self.__story)

    def goto_personal_page(self):
        """
        进入个人主页管理
        :return:
        """
        # self.handle_home_page_popup()
        self.find_and_click(self.__head_image)
        from pages.native.self_profie_manage.self_profile_manage import SelfProfileManage
        return SelfProfileManage(self.poco)

    def handle_daily_check_in_popup(self):
        if agv._get('check_in'):
            return
        self.wait_for_visible(self.__check_in_rewards, timeout=5)

        if self.is_exist(self.__check_in_rewards):
            self.find_and_click(self.__home_tab)
            agv._set('check_in', True)

    def handle_home_page_popup(self, check_times=2):
        """
        处理首页中弹出的弹窗
        :param check_times:
        :return:
        """

        for i in range(check_times):
            self.handle_daily_check_in_popup()
            # self.handle_tap_to_create_popup()

    def goto_odyssey_server(self, server_type='public'):
        """
        进入大世界房间
        默认进入公共房间
        传入其他值创建私人房间
        :param server_type:
        :return:
        """

        if server_type == 'public':
            self.find_and_click(self.__join_public_server)
        else:
            self.find_and_click(self.__create_private_server)
        from pages.u3d.engine.odyssey_room_page import OdysseyRoomPage
        ody = OdysseyRoomPage(self.poco)
        ody.wait_for_join_odyssey_server_success()
        return ody

    def goto_public_servers_list(self):
        """
        有Public Servers入口时，进入大世界Public Servers 列表
        :return:
        """

        self.find_and_click(self.__public_servers)
        from pages.native.home_page.public_servers_page import PublicServersPage
        return PublicServersPage(self.poco)

    def claim_airdrop(self, index=0):
        """
        点击领取首页的AirDrop
        index=0：grnd
        index=1：pass卡
        index=2：rewards
        :param index:
        :return:
        """

        self.finds(self.__airdrops)[index].click()
        if index == 0:
            return self.is_exist(self.__claim) and self.is_exist(self.__claim_title)
        if index == 1:
            return self.is_exist(self.__get_it_pass) and self.is_exist(self.__pass_title)
        if index == 2:
            from pages.native.home_page.check_in_rewards_page import CheckInRewardsPage
            return CheckInRewardsPage(self.poco)
        else:
            self.log.error(f"获取首页的AirDrops传入的index不符合预期，传入index={index}, 预期范围[0, 2]!!!")

    def goto_story_model(self):
        """
        进入首页故事模式
        :return:
        """
        self.find_and_click(self.__story)
        from pages.u3d.u3d_editor.story_model_page import StoryModelPage
        return StoryModelPage(self.poco)

    def goto_avatar(self):
        """
        进入首页Avatar界面
        :return:
        """

        self.find_and_click(self.__avatar)
        from pages.u3d.avatar.vertical_avatar_page import VerticalAvatarPage
        return VerticalAvatarPage(self.poco)

    def goto_hangout(self):
        """
        进入首页Hangout界面
        :return:
        """

        self.find_and_click(self.__hangout)
        from pages.native.home_page.hangout_page import HangoutPage
        return HangoutPage(self.poco)

    def goto_wallet_page(self, method="direct"):
        """
        create: 创建钱包
        import：导入钱包
        direct:已有钱包，进入钱包页
        :return:
        """

        pass

    def enter_tab(self, tab_name="home"):
        """
        切换tab
        :param tab_name:
        home  ——> 首页
        store  ——> 商城
        feed  ——> feed
        im  ——> 单聊、群聊
        gs  ——> 超级群
        默认  ——> 首页
        :return:
        """
        if tab_name == "home":
            self.find_and_click(self.__home_tab)
            return self
        if tab_name == 'store':
            self.find_and_click(self.__props_tab)
            from pages.native.store_page.ugc_experience_page import UGCExperiencePage
            return UGCExperiencePage(self.poco)
        if tab_name == 'feed':
            self.find_and_click(self.__feed_tab)
            from pages.native.feed.feed_for_you_page import FeedForYouPage
            return FeedForYouPage(self.poco)
        if tab_name == "im":
            self.find_and_click(self.__chat_tab)
            from pages.native.im.chat_page import ChatPage
            return ChatPage(self.poco)
        if tab_name == 'gs':
            self.find_and_click(self.__group_server_tab)
            from pages.native.group_server.group_server_page import GroupServerPage
            return GroupServerPage(self.poco)
        else:
            self.find_and_click(self.__home_tab)
            return self

    def goto_search_input_page(self):
        """
        首页点击搜索按钮进入搜索输入页
        :return:
        """
        self.find_and_click(self.__search)
        from pages.native.search.search_input_page import SearchInputPage
        return SearchInputPage(self.poco)


if __name__ == '__main__':
    h = HomePage(mutil_device="aaa")
    print(h)
