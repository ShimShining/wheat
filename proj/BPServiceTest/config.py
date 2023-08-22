# -*- coding: utf-8 -*-
"""
@Author: shining
@File: config.py
@Date: 2021/12/24 11:59 下午
@Version: python 3.10
@Describe: 运行环境，case数据读取配置
"""
import difflib
import pprint
import re
import os
import inspect
from proj.BPServiceTest.utils.data_model import DataModel
from proj.BPServiceTest.utils.read_yaml import ReadYAML
import proj.BPServiceTest.global_variable as ugv

try:
    ugv._get("RUN_ENV")
except Exception:
    ugv._init()


class Config:

    ROOT_DIR = os.path.abspath(os.path.dirname(__file__)).split('wheat')[0] + "wheat"
    # 运行环境配置
    # print("开始进入配置文件")
    RUN_ENV = "MASTER_HOST" if not ugv._get("RUN_ENV") else ugv._get("RUN_ENV")
    # RUN_ENV = "MASTER_HOST"
    # RUN_ENV = "ALPHA_HOST"
    # RUN_ENV = "GREY_HOST"
    # RUN_ENV = "PROD_HOST"
    RUN_SOURCE = "LOCAL" if not ugv._get("RUN_SOURCE") else ugv._get("RUN_SOURCE")
    # 可在此处配置接口的运行version
    MASTER_VERSION = '1.58.0'
    ALPHA_VERSION = '1.57.0'
    GREY_VERSION = "1.56.1"
    PROD_VERSION = '1.56.1'

    # 获取项目根路径
    PROJ_PATH = ROOT_DIR + "r\proj" + r"\BPServiceTest" + "\\"
    DATA_PATH = PROJ_PATH + "data/"

    # 服务配置文件路径
    SERVICE_NAME_FILE_PATH = PROJ_PATH + "service_name.yml"

    # 报告机器人webhook地址
    # DEBUG ==> QA Team
    DEBUG_WEB_HOOK_URL = ""

    # 单独的DEBUG机器人 for GL
    DEBUG = ""

    # 专项测试群
    SPECIAL_WEB_HOOK_URL = ""

    # 工程师群
    ENGINER_WEB_HOOK_URL = ""

    # 联机测试群机器人

    # 联机优化进展sync
    # ENGINE_SYNC_WEB_HOOK_URL = ""
    # 测试群
    ENGINE_SYNC_WEB_HOOK_URL = ""

    @classmethod
    def get_proj_run_host(cls, run_env=None, service_name="BPApi"):
        """
        获取服务的运行host
        :param service_name: 服务名称，取对应业务的基类名称即可
        :param run_env:
        :return:
        """
        services = ReadYAML.read(cls.SERVICE_NAME_FILE_PATH)
        service_names = list(services.keys())

        if service_name not in service_names:
            print(f"Warning: 在service_name.yml 未查找到相关服务的配置，默认使用BPApi服务Host！！！")
            service_name = "BPApi"
        if run_env:
            host = services[service_name]["HOST"][run_env]
            return host
        host = services[service_name]["HOST"][cls.RUN_ENV]
        return host

    @classmethod
    def case_data(cls, yaml_name, case_name=None):
        data_dict = cls.case_data_dict(yaml_name, case_name=case_name)
        return DataModel(data_dict)

    @classmethod
    def case_data_dict(cls, yaml_name, case_name=None):

        case_node = cls.RUN_ENV.split("_")[0]  # 测试数据中的用例环境
        # 灰度host路由到Alpha分支数据，进行验证
        if cls.RUN_ENV == "GREY_HOST":
            case_node = "ALPHA_HOST".split("_")[0]  # 也可以路由到PROD分支
        data_dict = ReadYAML.read_case_data(cls.DATA_PATH + yaml_name, case_node, case_name=case_name)
        return data_dict

    @classmethod
    def get_run_env_version(cls, run_env=None):
        run_host = cls.get_proj_run_host(run_env=run_env)
        run_version = None
        try:
            run_version = ugv._get("RUN_VERSION")
        except NameError:
            ugv._init()

        if run_version:
            if re.match(r'\d+\.\d+\.\d+', run_version):
                return run_version
        if 'test' in run_host:
            return cls.MASTER_VERSION
        if "alpha" in run_host:
            return cls.ALPHA_VERSION
        if "grey" in run_host:    # 灰度分支版本
            return cls.GREY_VERSION
        return cls.PROD_VERSION

    @classmethod
    def get_run_env_name(cls):

        return cls.RUN_ENV.split("_")[0]

    @classmethod
    def get_base_service_name(cls, call_file_name, call_class_var_names):

        # frame = inspect.currentframe()
        # back = frame.f_back
        # # service_name_globals = back.f_globals["__file__"].split("/")[-1].split(".")[0]
        # call_file_name = back.f_code.co_filename.split("/")[-1].split(".")[0]
        # call_class_var_names = []
        # if back.f_code.co_names:
        #     call_class_var_names = call_class_var_names
        # print(f"call_file_name ==== > {call_file_name}")
        # print(f"call_class_var_names ==== > {call_class_var_names}")
        # call_class_name = cls.get_base_service_name(call_file_name, call_class_var_names)
        # print(f"call_class_name >>>>>>>>>> {call_class_name}")
        # # for attr in dir(back.f_code):
        # #     if "__" not in attr:
        # #         print(f"back.{attr} = {getattr(back.f_code, attr)}")
        # level = inspect.stack()[-1]
        # services_class_name = []
        # for k, v in level.frame.f_locals.items():
        #     if inspect.isclass(v) and k in service_names:
        #         services_class_name.append(k)
        # print(f"services_class_name= {services_class_name}")

        if not call_class_var_names:
            return call_file_name

        service_name = call_file_name
        var_names = [v for v in call_class_var_names if
                     v not in ["super", "__init__", "Config", "__name__", "__class__"]]
        similar = 0.0
        for class_var in var_names:
            var_similar = difflib.SequenceMatcher(lambda x: x == "_", call_file_name, class_var).ratio()
            if var_similar >= similar:
                similar = var_similar
                service_name = class_var
        return service_name

    # @classmethod
    # def get_engine_simulation_host(cls):
    #     """
    #     获取联机不同环境的模拟地址
    #     :return:
    #     """
    #     return cls.ENGINE_HOST[cls.get_run_env_name()]


if __name__ == "__main__":
    # print(Config.get_run_env_version())
    # print(Config.get_proj_run_host())
    c = Config()
    # a = "bx_api"
    # b = (,
    # '__name__', 'version', 'get_run_env_version')
    # service = c.get_base_service_name(a, b)
    # print(service)
    print(c.ROOT_DIR)
