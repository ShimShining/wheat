"""
@Author: shining
@File: base_api.py
@Date: 2021/10/25 9:10 下午
@Version: python 3.10
@Describle: api 基类封装
"""
import json
import os.path
import sys
from datetime import datetime
from json import JSONDecodeError
import requests
# from websocket import create_connection, WebSocketTimeoutException
from proj.BPServiceTest.utils.log import Logger, log_api_cost
import copy

try:
    log_file_name = ".".join(sys.argv[1].replace(".py::", ".").replace("::", ".").split(".")[-2:])
except:
    # todo 直接在文件夹下执行，不加参数的pytest，期望是带文件夹的名字作为log_file_name
    log_file_name = "base_api.py默认日志文件名"

# print(f"base_api的日志文件名：{log_file_name}")
# print(sys.argv)
# 日志级别设置：DEBUG  INFO  WARN   ERROR   CRITICAL 如果不想输出INFO的日志，可以将日志级别设置为：WARN ERROR CRITICAL
logger = Logger(log_file_name, level="INFO").logger
logger.info("<== logger 初始化完成，开始收集日志 ==>")
# logger.info(f"sys.argv参数列表={sys.argv}")
logger.info(f"log主文件路径={log_file_name}")


def cast_param_to_req_body_key(param: str):
    """
    转换接口业务层函数的传入参数，变为请求体的key
    :param param:
    :return:
    """

    if "_" not in param:
        return param

    res = []

    for i in range(len(param)):

        if i == 0:
            temp = param[i]
        elif param[i] == "_":
            continue
        elif param[i - 1] == "_" and i < len(param) and param[i].isalpha():
            temp = param[i].upper()
        else:
            temp = param[i]
        res.append(temp)

    return "".join(res)


def get_req_body(req: dict, is_tp_uid=False):
    """
    获取Http业务接口req参数
    :param req:
    :param is_tp_uid:
    :return:
    """
    req_data = {}
    body = {}

    for k, v in req.items():
        if k in ["self", 'kwargs', 'version'] or v is None or v == "":
            continue
        elif k in ["h", "header", "headers"]:
            req_data["headers"] = v
        elif k in ["path", 'p']:
            req_data["path"] = v
        elif k == "name":
            req_data[k] = v
        elif not is_tp_uid and k == 'uid':
            continue
        else:
            req_key = cast_param_to_req_body_key(k)
            body[req_key] = v
    if req_data.get("headers", None) is None:
        uid = req.get("uid", None)
        if uid is None:
            pass
            # raise ValueError("传入handle_req_params的locals()中既未传入headers相关，也未传入uid参数！！！")
        else:
            req_data["headers"] = {"uid": uid}
    req_data["params"] = body
    return req_data


class BaseApi:

    def __init__(self):
        self.log = logger

    @log_api_cost
    def request(self, req: dict):

        if req.get("protocol", None) == "websocket":
            return self.websocket_request(req)

        return self.http_request(req)

    def http_request(self, req: dict):

        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log.info(f"------------------接口请求开始, 开始时间=【{t}】------------------")
        self.log.info(f"接口名称：{req.get('name', 'not setting api name')}")
        self.log.info(f"请求方式：{req.get('method')}")
        self.log.info(f"请求路径：{req.get('url')}")
        # self.log.info(f"请求头：{req.get('headers', {})}")

        req.pop("name", None)
        tmp = []
        for k in req.keys():
            if k not in ['method', 'json', 'params', 'method', 'url', 'data', 'headers', 'cookies', 'files', 'auth',
                         'timeout', 'allow_redirects', 'proxies', 'hooks', 'stream' 'verify', 'cert']:
                tmp.append(k)
        for k in tmp:
            req.pop(k, None)
        # 再次处理错误SSLError(MaxRetryError("HTTPSConnectionPool(host='', port=443)
        req['verify'] = False
        data = copy.deepcopy(req)
        data.pop("method")
        data.pop("url")
        data.pop("header", None)
        data.pop("name", None)
        self.log.info(f"REQ ==> 请求参数：{json.dumps(data, indent=4, ensure_ascii=False)}")
        # self.log.info(f"被json.dumps后的请求REQ={req}")
        r = requests.request(**req)
        # self.log.info(f"返回Response的类型：【{type(r)}】")
        self.log.info(f"返回状态码:【{r.status_code}】")
        if r.status_code in (500, 501, 502, 503):
            self.log.error(f"ServerRSPError: 服务器返回状态码={r.status_code}, 服务器出错")
            from proj.BPServiceTest.base.b import ServerRSPError
            raise ServerRSPError(f"ServerRSPError: 服务器返回状态码={r.status_code}, 服务器出错")
        try:
            rsp = r.json()
            r.encoding = 'utf-8'
            self.log.info(f"RSP ==> 返回响应: {json.dumps(rsp, indent=4, ensure_ascii=False)}")
        except JSONDecodeError:
            self.log.error(f"捕获JSONDecodeError ==> 返回体不能转换为json体 r.content = {r.content}")
            self.log.error(f"捕获JSONDecodeError ==> 返回体不能转换为json体 r.text = {r.text}")
            raise JSONDecodeError(f"返回体捕获JSONDecodeError，r.text === {r.text}", f"r.content = {r.content}", "line 148")
        self.log.info("----------------------- 接口请求结束 -----------------------")
        return r

    def websocket_request(self, **kwargs):

        pass

    def get(self, req: dict):

        req['method'] = 'GET'
        return self.request(req)

    def post(self, req: dict):

        req['method'] = 'POST'
        req['headers']['Content-Type'] = 'application/json'
        return self.request(req)

    def head(self, req: dict):

        req['method'] = 'HEAD'
        return self.request(req)

    def delete(self, req: dict):

        req['method'] = 'DELETE'
        return self.request(req)

    def options(self, req: dict):
        req['method'] = 'OPTIONS'
        return self.request(req)

    def conn(self, uri, timeout=3):
        """
        连接web服务器
        :param uri:
        :param timeout:
        :return:
        """
        self.wss = create_connection(uri, timeout=timeout)

    def send(self, message):
        """
        发送websocket请求数据体
        :param message:
        :return:
        """
        if not isinstance(message, str):
            message = json.dumps(message)
        self.log.info(f"发送的message={message}")
        return self.wss.send(message)

    def handle_json(self, base_req):

        if isinstance(base_req, str):
            try:
                res = json.loads(base_req)
                return self.handle_json(res)
            except JSONDecodeError:
                return base_req
        elif isinstance(base_req, list):
            res = []
            for i in base_req:
                res.append(self.handle_json(i))
            return res
        elif isinstance(base_req, dict):
            for k, v in base_req.items():
                base_req[k] = self.handle_json(v)
            return base_req
        return base_req

    def recv(self, timeout=3):
        """
        接受websocket的数据体信息
        :param timeout:
        :return:
        """
        if isinstance(timeout, dict):
            timeout = timeout['timeout']
        try:
            self.set_timeout(timeout)
            recv_json = self.wss.recv()
            all_json_recv = self.handle_json(recv_json)
            self._set_response(all_json_recv)
            return all_json_recv
        except WebSocketTimeoutException:
            self.log.error(f"超过{timeout}秒没有接收数据！！！")

    def set_timeout(self, timeout):

        self.wss.settimeout(timeout)

    def recv_all(self, timeout=3):
        """
        接收多个数据体信息，并调用数据体处理方法处理响应体
        :param timeout:
        :return:
        """
        if isinstance(timeout, dict):
            timeout = timeout['timeout']
        recv_list = []
        while True:
            try:
                self.set_timeout(timeout)
                recv_json = self.wss.recv()
                all_recv_json = self.handle_json(recv_json)
                recv_list.append(all_recv_json)
                self.log.info(f"收到的所有数据 ===> {all_recv_json}")
            except WebSocketTimeoutException:
                self.log.error(f"超过{timeout}秒没有接收到数据！！！")
                break
        self._set_response(recv_list)
        return recv_list

    def close(self):
        """
        关闭连接
        :return:
        """
        return self.wss.close()

    def _set_response(self, rsp):
        self.response = rsp

    def _get_response(self, rsp):
        return self.response

    def handle_req_params(self, params: dict, is_tp_uid=False):
        """
        处理请求参数
        Todo 处理嵌套参数的能力{"a": {'b': type_b}}
        :param is_tp_uid:
        :param params:
        :return:
        """
        args = params.get("args", None)
        if not args:
            if isinstance(params, dict):
                return get_req_body(params, is_tp_uid=is_tp_uid)
            else:
                raise ValueError(f"传入解析的参数不是字典！！！ params = {params}")
        return get_req_body(args, is_tp_uid=is_tp_uid)

