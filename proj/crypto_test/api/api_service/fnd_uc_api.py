# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/13
Describe:9天预测接口数据
"""
from api.api_service.base_api import BaseApi


class FudUcApi(BaseApi):

    base_url = "https://pda.weather.gov.hk"
    __forecast_path = "/locspc/android_data/fnd_uc.xml"

    def get_forecast(self):

        data = {
            "url": self.base_url + self.__forecast_path,
            "method": "get"
        }

        r = self.request(data)
        return r

