# -*- coding: utf-8 -*-
""""
@Author: xieguanglin
@File: log.py
@Date: 2021/10/26 10:54 下午
@Version: python 3.10
@Describle: 日志模块初步封装
"""

import logging
import os.path
import sys
import time
from functools import wraps


class Logger:

    def __init__(self, logger_name=__name__, level="INFO"):
        # 使用logging模块产生logger对象
        logging.basicConfig(datefmt='%Y-%m-%d%I:%M:%s %p')
        # 创建一个日志对象，这个参数可以随便填写，这个参数唯一标识了这个日志对象
        self.logger = logging.getLogger(logger_name)
        # 设置日志级别
        self.logger.setLevel(getattr(logging, level))
        # 设置日志路径
        # # 绝对路径-不推荐
        # log_abs_path = "/Users/shining/PycharmProjects/BUDTest/log/"
        dt = time.strftime("%Y_%m_%d_%H_%M", time.localtime(time.time()))
        # 日志文件名
        # log_file_name = log_abs_path + str(loggername) + '-' + str(dt) + '.log'
        # 相对执行位置的下新建/logs/文件夹
        current_path = os.path.dirname(os.path.realpath(__file__))
        # 获取项目的根路径
        root_dir = os.path.abspath(os.path.dirname(__file__)).split('BUDTest')[0] + "BUDTest/"
        print(f"root_dir = {root_dir}")
        # base_dir = os.path.join(sys.path[1], '')
        # print(f"base_dir = {base_dir}")
        log_real_path = os.path.join(root_dir, 'log/')
        # print(f"log_real_path = {log_real_path}")
        # base_real_dir = os.path.dirname(os.path.dirname(__file__))
        # print(f"当前路径的相对路径base_real_dir = {base_real_dir}")
        # log_path = current_path + "/logs/"
        # if not os.path.exists(log_path):
        #     os.makedirs(log_path)

        # 日志文件名
        # todo 分布式运行支持，1 随机字符 2 线程ID
        # log_file_name = log_real_path + str(logger_name) + '_' + str(dt) + '.log'
        log_file_name = log_real_path + str(logger_name) + '_' + 'us_api_auto_test' + '.log'
        # 创建Handler，用于写入日志文件，a表示追加，encoding默认为ASCII，中文会显示乱码
        file_handler = logging.FileHandler(log_file_name, 'w', encoding='utf-8')
        # 为logger添加日志处理器
        self.logger.addHandler(file_handler)
        # 设置日志输出格式
        formatter = logging.Formatter('%(asctime)s => %(filename)s[line:%(lineno)d] * %(levelname)s : %(message)s')
        file_handler.setFormatter(formatter)

    def fun(self):

        self.logger.error("this is err log.")
        self.logger.info("this is info log.")
        self.logger.debug("this is debug log.")
        self.logger.warning("this is waring log.")


def log_api_cost(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        from base import logger
        start = 1000 * time.time()
        logger.info(f"=============  Begin func.__name__: {func.__name__}  =============")
        # logger.info(f"Args: {args}\n kwargs: {kwargs}")
        try:
            rsp = func(*args, **kwargs)
            # logger.info(f"Response: {rsp}")
            end = 1000 * time.time()
            logger.info(f"Api Time Cost: {end - start}ms")
            logger.info(f"=============   End func.__name__: {func.__name__}   =============\n")
            return rsp
        except Exception as e:
            logger.error(repr(e))
            raise e
    return wrapper

@log_api_cost
def tes(name: str):
    logger = Logger("test_logger")
    time.sleep(2)
    return {"ret_code": 0, "ret_msg": "success", "ret_data": {"name": name}}


if __name__ == "__main__":

    test_logger = Logger("test_logger")
    test_logger.fun()
    tes("aaa")


