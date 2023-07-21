# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/13
Describe:天气预测测试
"""
import datetime
import allure
from app.app_page_obj.app import App


@allure.feature("九天预报模块")
class TestAppForecastPage:

    def setup_class(self):
        self.app = App()

    def setup(self):

        self.home = self.app.start().go_main()

    def teardown(self):

        # 单条case重启app
        self.app.restart()

    def teardown_class(self):
        # kill driver
        self.app.stop()

    def test_enter_forecast_success(self):

        self.home.goto_menu_page().goto_forecast_page().check_elem_exist()

    def test_forecast_list(self):

        forecasts = self.home.goto_menu_page().goto_forecast_page().get_nine_list()
        now_time = datetime.datetime.now()
        next_day = (now_time + datetime.timedelta(days=+1))
        month_en = next_day.strftime("%b")
        month_num = next_day.strftime("%m")
        if month_num[0] == '0':
            month_num = month_num[1]
        day = next_day.strftime("%d")
        # week = next_day.strftime("%a")
        assert (month_en in forecasts[0] or month_num in forecasts[0])
        assert day in forecasts[0]
        # assert week in forecasts[0]
