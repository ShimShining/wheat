# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/6/13
Describe:
"""
import json
import requests
import os
import sys
from utils.log import Logger

log_filename = os.path.realpath(sys.argv[1]).split("\\")[-1]. \
    replace(".py::", "_").replace("::", ".") \
    if sys.argv[1] else None
# log_filename = os.path.basename(__file__)
print(f"日志主文件路径={log_filename}")
print(f"Sys.argv参数列表={sys.argv}")
logger = Logger(log_filename).logger


class BaseApi:

    def __init__(self):

        self.logger = logger

    def request(self, request: dict):

        if request.get("protocol") == "rpc":
            return self.rpc_request(**request)

        if request.get("protocol") == "tcp":
            return self.tcp_request(**request)

        return self.http_request(request)

    def http_request(self, request):

        r = requests.request(**request)
        r.encoding = 'utf-8'

        self.logger.info(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def rpc_request(self, request):

        pass

    def tcp_request(self, request):

        pass

