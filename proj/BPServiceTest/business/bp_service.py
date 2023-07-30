# -*- coding: utf-8 -*-
"""
@Author: shining
@File: BUDUSApi.py
@Date: 2021/12/23 9:24 下午
@Version: python 3.10
@Describle: 接口自动化基类
"""
from proj.BPServiceTest.base.bud_api import BUDApi
from proj.BPServiceTest.config import Config


class BPService(BUDApi):

    def __init__(self, env=Config.RUN_ENV, version=None, token=None, host=None):
        super(BUDUSApi, self).__init__()
        self.env = env
        self.token = token
        # 获取环境host
        if host:
            self.host = host
            # self.log.info(f"当前服务 [{self.__class__.__name__}] 使用已有Host：【{self.host}】")
        else:
            self.host = Config.get_proj_run_host(self.env)
            self.log.info(f"当前服务 [{self.__class__.__name__}] Api运行环境是：【{self.host}】")
        # 获取运行版本号
        if version:
            self.version = version
            return
        self.version = Config.get_run_env_version()

    def get_token(self, req, **kwargs):
        """
        获取token的方式：
        1. req和关键字参数kwargs直接带有token，不会进入这个method
        2. req带了open_id和provider，使用login获取token
        3. req没带open_id和provider， 关键字参数kwargs带了open_id和provider，使用login接口获取token
        4. req和关键字参数kwargs都没带token，没带open_id和provider，那么使用global_user_info.yml配置的token
        :param req:
        :param kwargs:
        :return:
        """
        if (req and (req.get('provider', None) is None or req.get('open_id', None) is None or req.get('user_token',
                                                                                        None) is None)) or not req:
            token = Config.case_data('global_user_info.yml').token
            # self.log.info(f"使用全局的token变量={token}")
            self.log.info("使用全局的token变量")
            return token
        from proj.BPServiceTest.business.basal.login import Login
        login = Login()
        if req:
            self.log.info("使用login接口获取token")
            provider = req.get('provider', None)
            user_token = req.get('user_token', None)
            # 传入open_id,provider可获取对应用户的token
            r = login.login_v2(open_id=req['open_id'], provider=provider, user_token=user_token)
            token = r['data']['token']
            # self.log.info(f"使用login接口获取的token变量={token}")
            self.log.info("使用login接口获取的token")
            return token
        elif kwargs and kwargs.get('open_id', None) is not None and kwargs.get('provider', None) is not None:
            r = login.login_v2(open_id=kwargs.get('open_id'), provider=kwargs.get('provider'))
            token = r['data']['token']
            # self.log.info(f"使用kwargs参数通过login接口获取的token变量={token}")
            self.log.info("使用kwargs参数通过login接口获取的token")
            return token


if __name__ == "__main__":
    bs = BUDUSApi()


