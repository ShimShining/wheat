# -*- coding: utf-8 -*-
"""
@Author: shining
@File: setup_bot_content.py
@Date: 2022/2/13 10:15 下午
@Version: python 3.10
@Describe:
"""


class SetupBotContent:

    @staticmethod
    def setup_enter_room_rate(info):

        content = f"**总体成功率：\n{info['total_success_rate']} %**\n" \
                  f"**安卓成功率：\n{info['android_success_rate']} %**\n" \
                  f"**iOS 成功率：\n{info['ios_success_rate']} %**"
        if info.get('gap', None) is not None:
            content = f"**总体成功率：\n{info['total_success_rate']} %({info['gap']['total_success_rate']})**\n" \
                      f"**安卓成功率：\n{info['android_success_rate']} %({info['gap']['android_success_rate']})**\n" \
                      f"**iOS 成功率：\n{info['ios_success_rate']} %({info['gap']['ios_success_rate']})**"
        return content

    @staticmethod
    def setup_room_code_to_play_rate(info):

        content = f"**roomCodeToPlay总成功率：**\n**{info['rc_success_rate']} %**\n" \
                  f"**安卓roomCodeToPlay成功率：**\n**{info['android_rc_success_rate']} %**\n"\
                  f"**iOS roomCodeToPlay成功率：**\n**{info['ios_rc_success_rate']} %**"
        if info.get('gap', None) is not None:
            content = f"**总体成功率：\n{info['rc_success_rate']} %({info['gap']['rc_success_rate']})**\n" \
                      f"**安卓成功率：\n{info['android_rc_success_rate']} %({info['gap']['android_rc_success_rate']})**\n" \
                      f"**iOS 成功率：\n{info['android_rc_success_rate']} %({info['gap']['ios_rc_success_rate']})**"
        return content

    @staticmethod
    def setup_click_to_play_latency(info):

        content = f"**clickToPlayLatency平均耗时：**\n**{round(info['ctop_cost'], 2)} 秒**\n"\
                  f"**安卓cToPlayLatency平均耗时：**\n**{round(info['android_ctop_cost'], 2)} 秒**\n"\
                  f"**iOS cToPlayLatency平均耗时：**\n**{round(info['ios_ctop_cost'], 2)} 秒**"
        if info.get('gap', None) is not None:
            content = f"**clickToPlayLatency平均耗时：**\n**{round(info['ctop_cost'], 2)} 秒({info['gap']['ctop_cost']})**\n"\
                  f"**安卓cToPlayLatency平均耗时：**\n**{round(info['android_ctop_cost'], 2)} 秒({info['gap']['android_ctop_cost']})**\n"\
                  f"**iOS cToPlayLatency平均耗时：**\n**{round(info['ios_ctop_cost'], 2)} 秒({info['gap']['ios_ctop_cost']})**"
        return content

    @staticmethod
    def setup_avg_fps(info):

        content = f"**总体成功率：\n{info['total_success_rate']} %**\n" \
                  f"**安卓成功率：\n{info['android_success_rate']} %**\n" \
                  f"**iOS 成功率：\n{info['ios_success_rate']} %**"
        if info.get('gap', None) is not None:
            content = f"**总体成功率：\n{info['total_success_rate']} %({info['gap']['total_success_rate']})**\n" \
                      f"**安卓成功率：\n{info['android_success_rate']} %({info['gap']['android_success_rate']})**\n" \
                      f"**iOS 成功率：\n{info['ios_success_rate']} %({info['gap']['ios_success_rate']})**"
        return content

    @staticmethod
    def setup_enter_room_rate(info):

        content = f"**总体成功率：\n{info['total_success_rate']} %**\n" \
                  f"**安卓成功率：\n{info['android_success_rate']} %**\n" \
                  f"**iOS 成功率：\n{info['ios_success_rate']} %**"
        if info.get('gap', None) is not None:
            content = f"**总体成功率：\n{info['total_success_rate']} %({info['gap']['total_success_rate']})**\n" \
                      f"**安卓成功率：\n{info['android_success_rate']} %({info['gap']['android_success_rate']})**\n" \
                      f"**iOS 成功率：\n{info['ios_success_rate']} %({info['gap']['ios_success_rate']})**"
        return content
