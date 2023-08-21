# -*- coding: utf-8 -*-
"""
@Author: shining
@File: bp_api.py
@Date: 2021/12/24 11:12 上午
@Version: python 3.10
@Describe: business base api
"""
import json
import re

from proj.BPServiceTest.base.base_api import BaseApi


class BPApi(BaseApi):

    def __init__(self, env=None, host=None, token=None, version=None):
        super(BPApi, self).__init__()
        self.env = env
        self.host = host
        self.token = token
        self.version = version

    def bp_get(self, req: dict = None, path=None, params=None, headers=None, **kwargs):

        # 处理自定义传入的一些参数，比如token
        req, headers = self.handle_headers(req, path, headers, **kwargs)
        if req:
            url = self.host + req['path']
        elif not req and path and params:
            req = {"path": path, "params": params, "headers": headers}
            url = self.host + path
        else:
            raise ValueError("cn_get的传入参数有误！！！")
        req['url'] = url
        req.pop("path")
        return self.get(req)

    def bp_post(self, req: dict = None, path: str = None, j: dict = None, headers: dict = None, **kwargs):

        # 处理自定义传入的一些参数，比如token
        req, headers = self.handle_headers(req, path, headers, **kwargs)
        if req:
            url = self.host + req['path']
            params = req.get("params", None)
            if params:
                req['json'] = params
                req.pop("params")
        elif not req and path and j:
            req = {"path": path, "json": j, "headers": headers}
            url = self.host + path
        else:
            raise ValueError("bud_post传入参数不正确！！！")
        req['url'] = url
        req.pop("path")
        return self.post(req)

    def bp_head(self, req: dict = None, path=None, **kwargs):
        """
        todo: 参考cn_get和cn_post方式优化传参方式
        :param req:
        :param path:
        :return:
        """
        # 处理自定义传入的一些参数，比如token
        if req and kwargs:
            for k, v in kwargs.items():
                req[k] = v
        self.handle_token(req=req, path=path, **kwargs)
        url = self.host + req['path']
        req['url'] = url
        req.pop("path")
        return self.head(req)

    def bp_delete(self, req: dict = None, path: str = None, j: dict = None, headers: dict = None, **kwargs):

        # 处理自定义传入的一些参数，比如token
        req, headers = self.handle_headers(req, path, headers, **kwargs)
        if req:
            url = self.host + req['path']
        elif not req and path and j:
            req = {"path": path, "json": j, "headers": headers}
            url = self.host + path
        else:
            raise ValueError("bud_delete 参数传入不正确！！！")
        req['url'] = url
        req.pop("path")
        return self.delete(req)

    def bp_options(self):
        pass

    def bp_handle_headers(self, req=None, headers=None, **kwargs):
        """
        处理headers里的参数
        :param req:
        :param headers:
        :param kwargs:
        :return:
        """
        headers_handle_flag = False
        m = r'.*/login[a-zA-Z0-9_]*$'
        environment = None
        try:
            environment = self.env.split("_")[0].lower()
            if environment == 'alpha':
                environment = 'pr'
        except Exception as e:
            self.log.error(f"获取headers字段environment值throw 异常，exception={e}")
        if req:
            # if not re.findall(m, req.get('path', None)):
            # 兼容req请求体中，带了headers参数
            if req.get("headers", None) is None:
                req['headers'] = dict()
                req['headers']['version'] = self.version
                req['headers'].update(dict(kwargs))
                if environment:
                    req['headers']['environment'] = environment
                # headers_handle_flag = True
            else:
                if not req['headers'].get('version',None):
                    req['headers']['version'] = self.version
                for k, v in kwargs.items():
                    req['headers'][k] = v
                if environment:
                    req['headers']['environment'] = environment
                # headers_handle_flag = True
            if req.get('method', None) == "POST":
                req['headers']['Content-Type'] = 'application/json'   # 如果是走子参数，post请求不会添加这个头信息 放在底层去了
            if re.findall(m, req.get('path', None)):
                req['headers'].pop('token', None)
        elif not headers_handle_flag and headers:
            # 在headers里加入API访问的版本字段version
            headers['version'] = self.version
            if environment:
                headers['environment'] = environment
            for k, v in kwargs.items():
                headers[k] = v
            headers_handle_flag = True
        elif not headers_handle_flag:
            headers = dict()
            headers['environment'] = environment
            headers['version'] = self.version
            headers.update(dict(kwargs))

        return req, headers

    def get_token(self, req, **kwargs):
        pass

    def handle_token(self, req=None, path=None, **kwargs):

        # req中带了token，直接使用
        match_login = r'.*/login[a-zA-Z0-9_]*$'
        if req and req.get('token', None) is not None:
            self.token = req.get('token')
            req.pop('token', None)
            # self.log.info(f"获取接口直接传入token成功，token={self.token}")
            self.log.info("获取接口直接传入token成功")
            return
        # kwargs额外传入token
        if kwargs and kwargs.get('token', None) is not None:
            self.token = kwargs.get('token')
            # self.log.info(f'kwargs中传入Token={self.token}')
            self.log.info('使用kwargs中传入Token')
            return
        flag = False
        if req and not re.findall(match_login, req.get('path', None)):
            flag = True
        elif path and not re.findall(match_login, path):
            flag = True
        # 需要通过login接口获取，这个时候，req参数需要传入provider，open_id，user_token
        if flag:
            # self.log.info("非login，需要进入获取Token流程==>")
            self.token = self.get_token(req, **kwargs)
        # 本身是login接口，不需要获取
        else:
            self.log.info("login相关接口不需要获取Token")

    def handle_headers(self, req=None, path=None, headers=None, **kwargs):
        """
        前置处理headers 和kwargs传入的参数
        :param req:
        :param path:
        :param headers:
        :param kwargs:
        :return:
        """
        if req and kwargs:
            for k, v in kwargs.items():
                req[k] = v
        self.handle_token(req=req, path=path, **kwargs)
        if kwargs.get('token', None) is None:
            kwargs['token'] = self.token
        req, headers = self.bp_handle_headers(req, headers, **kwargs)
        return req, headers
