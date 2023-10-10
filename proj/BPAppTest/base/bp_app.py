# -*- coding: utf-8 -*-
"""
@Author: shining
@File: BP_app.py
@Date: 2022/5/20 2:18 下午
@Version: python 3.9
@Describe:
"""
from base.UPath import UPath
from base.app import App


class BPApp(App):
    # 首页弹窗黑名单，有新的处理弹窗，将UPath加入这个列表就行，底层会自动处理
    # 已加入，1. daily check in弹窗
    popup_black_lists = [
                        # (UPath(name="id/ib_core_lyt_onboarding_pager_fragment"), ''),
                        (UPath(name='id/title'), ''),
                        # (UPath(name='id/tvTapToCreatePopup'), "")
    ]

    def __init__(self, po=None, platform=None, mutil_device=None):
        super(BPApp, self).__init__(po=po, platform=platform, mutil_device=mutil_device)
