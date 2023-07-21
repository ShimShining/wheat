# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/13
Describe:
"""
from api.api_service.fnd_uc_api import FudUcApi


class TestForecastApi:

    def setup_class(self):

        self.fnd_api = FudUcApi()

    def test_get_nine_forecast_weather(self):

        r = self.fnd_api.get_forecast()
        assert r.status_code == 200

    def test_get_tdat_humidity(self):

        r = self.fnd_api.get_forecast()
        r.encoding = 'utf-8'
        assert r.status_code == 200
        forecast_detail = r.json()['forecast_detail']
        tdat_min_rh = forecast_detail[1]['min_rh']
        tdat_max_rh = forecast_detail[1]['max_rh']
        assert tdat_min_rh is not None
        assert tdat_max_rh is not None
        self.fnd_api.logger.info("the day after tomorrow is " + str(tdat_min_rh) + "-" + str(tdat_max_rh) + "%.")

