# -*- coding: utf-8 -*-
"""
@Author: shining
@File: app.py
@Date: 2022/5/20 2:18 下午
@Version: python 3.8
@Describe:
"""
from base.base_app import BaseApp
from airtest.core.api import *

from config import Config


class App(BaseApp):
    bundle_id = Config.BUNDLE_ID

    def __init__(self, po=None, platform=None, mutil_device=None):

        super(App, self).__init__(po=po, platform=platform, mutil_device=mutil_device)

    def start_app(self):

        start_app(self.bundle_id)

    def restart_app(self):

        self.kill_app()
        self.sleep(2)
        self.start_app()

    def kill_app(self):

        stop_app(self.bundle_id)

    def clear_app(self):

        clear_app(self.bundle_id)

    def goto_home_page(self):

        self.restart_app()

