# -*- coding: utf-8 -*-
"""
@Author: shining
@File: conftest.py
@Date: 2022/5/20 2:40 下午
@Version: python 3.9
@Describe:
"""
from airtest.core.api import *
from config import Config
from utils.yaml_handler import YAMLHandler
import pytest
from typing import List
import time
from _pytest import terminal
import app_global_variable as agv


agv._init()


def pytest_addoption(parser):
    parser.addoption(
        "--host",
        action='store',
        choices=['dev', 'master', 'alpha', 'prod'],
        help="dev: 开发环境；test：测试环境；alpha：预发布环境；prod：生产环境；默认环境为master"
    )
    parser.addoption(
        "--platform",
        action='store',
        help="执行的平台操作系统"
    )


def pytest_configure(config):
    h = config.getoption('--host')
    p = config.getoption('--platform')
    if h:
        agv._set("RUN_ENV", h)
    if p:
        agv._set("PLATFORM", p)


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List):
    """
    测试用例收集完成之后，将收集到的case的name和title兼容中文显示
    :param items:
    :return:
    """
    for case in items:
        case.name = case.name.encode('utf-8').decode('unicode-escape')
        case._nodeid = case._nodeid.encode("utf-8").decode('unicode-escape')
    return items


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # 获取钩子方法的调用结果
#     out = yield
# print('用例执行结果', out)

# 3. 从钩子方法的调用结果中获取测试报告
# report = out.get_result()
# if report.when == "call":
#     case_num += 1
#     if report.outcome == 'passed':
#         case_pass += 1
#     elif report.outcome == 'failed':
#         case_failed += 1

# print('测试报告：%s' % report)
# print('步骤：%s' % report.when)
# print('nodeid：%s' % report.nodeid)
# print('dir(report)：%s' % dir(report))
# print('description:%s' % str(item.function.__doc__))
# print(('运行结果: %s' % report.outcome))
# print(case_num)
# print(case_pass)
# print(case_failed)
#
# def pytest_report_teststatus(report, config):
#
#     print(report)
#     print(config)

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''
    收集测试结果
    case.keywords={'BUDTest': 1, 'test_get_chat_list': 1, 'chat': 1, 'test_chat.py': 1,
    'pytestmark': 1, 'us_api_test/testcase/test_social/__init__.py': 1,
    'smoking': 1, '()': 1, 'allure_label': 1, 'TestChat': 1}
    case.nodeid=us_api_test/testcase/test_social/test_chat.py::TestChat::test_get_chat_list
    case.head_line=TestChat.test_get_chat_list
    '''
    res = {}
    host = Config.RUN_ENV
    platform = Config.PLATFORM
    res["host"] = host
    res['platform'] = platform
    duration = time.time() - terminalreporter._sessionstarttime
    res['duration'] = round(duration, 2)
    res['total'] = terminalreporter._numcollected
    res["deselected"] = len(terminalreporter.stats.get('deselected', []))
    if res["deselected"]:
        res['total'] = res['total'] - res["deselected"]
    res['passed'] = len(terminalreporter.stats.get('passed', []))
    case_fail_list = terminalreporter.stats.get('failed', [])
    case_error_list = terminalreporter.stats.get('error', [])
    res['failed'] = len(case_fail_list)
    res['error'] = len(case_error_list)
    res['skipped'] = len(terminalreporter.stats.get('skipped', []))
    if (res['total'] - res['skipped']) > 0:
        res['success_rate'] = round(res['passed'] / (res['total'] - res['skipped']) * 100, 2)
    else:
        res['success_rate'] = 0.00
    res['recall_rate'] = 0
    res['fail_mod'] = []
    res['error_mod'] = []
    if case_fail_list:
        for case in case_fail_list:
            mod = case.head_line.split('.')[0][4:]
            if mod not in res['fail_mod']:
                res['fail_mod'].append(mod)
    if case_error_list:
        for case in case_error_list:
            mod = case.head_line.split('.')[0][4:]
            if mod not in res['error_mod']:
                res['error_mod'].append(mod)

    yaml_path = Config.ROOT_DIR + "notification/us_api_report.yml"
    YAMLHandler.write_yaml(yaml_path, res)
    # print(res)


def log_setting():

    import logging
    logger = logging.getLogger("airtest")
    logger.setLevel(getattr(logging, Config.AIRTEST_LOGGING_LEVEL))


def app_init(dev=None):

    platform = Config.PLATFORM
    if platform == 'android':
        # 使用auto_setup
        if not dev:
            auto_setup(__file__, devices=Config.PACKAGE_LIST['android']['devices_list'])
        # 使用connect_device
        # connect_device("Android:///SJE5T17B17?cap_method=javacap&touch_method=adb")
        # 使用init_device
        # init_device(platform="Android", uuid="SJE5T17B17", cap_method="JAVACAP")
        else:
            connect_device(dev)
        start_app(Config.BUNDLE_ID)
    elif platform == 'ios':
        # 连接本机部署的iOS真机
        # iOS: // / http: // 127.0.0.1:8100
        # 使用tidevice连接的iOS设备，DeviceIdentifier可以在启动的信息中查看
        # http + usbmux: // DeviceIdentifier
        # 使用auto_setup
        if dev:
            auto_setup(__file__, devices=["iOS:///http://127.0.0.1:8100"])
        else:
            connect_device(dev)
        start_app(Config.BUNDLE_ID)
        # 使用connect_device
        # connect_device("iOS:///http://127.0.0.1:8100")
        # 使用init_device
        # init_device(platform="IOS", uuid="http://127.0.0.1:8100")
    else:
        # 连接安卓
        auto_setup(__file__)
        start_app(Config.BUNDLE_ID)


@pytest.fixture(scope='session', autouse=True)
def device_init():
    """
    根据运行的platform和环境，连接运行设备，初始化环境
    :return:
    """
    # 设置airtest的日志等级
    log_setting()
    app_init()
    yield
    # 整个session结束后，清理运行app的数据
    # clear_app(Config.BUNDLE_ID)


@pytest.fixture(scope='function', autouse=True)
def stop_run_app():
    """
    每次case运行后，停止App运行
    :return:
    """
    yield
    #stop_app(Config.BUNDLE_ID)
#选择本地化语言
def Sttings_language():
   '''stop_app(Config.BUNDLE_ID)'''


@pytest.fixture()
def login():
    """
    用例执行前，是登录态
    1. 已登录，直接返回
    2. 未登录，stop app，再次进入，走登录流程
    :return:
    """
    try:
        stop_app(Config.BUNDLE_ID)
    except Exception as e:
        pass
    app_init()
    from pages.native.home_page.home_page import HomePage
    hm = HomePage()
    if hm.is_home_page():
        hm.handle_home_page_popup()
        return hm

    # stop_app(Config.BUNDLE_ID)
    # app_init()
    from flow.native.login_with_exsist_account_flow import LoginWithExistAccFlow
    login_flow = LoginWithExistAccFlow()
    return login_flow.login_in()


@pytest.fixture()
def no_login():
    """
    用例执行前，是非登录态
    1. 已登录
        a. 非临时账号，退出登录
        b. 临时账号，注销账号
    2. 未登录，stop app，再次进入
    """
    # stop_app(Config.BUNDLE_ID)
    # app_init()
    from pages.native.login_register.login_page import LoginPage
    lp = LoginPage()
    if lp.is_login_page():
        return lp
    # stop_app(Config.BUNDLE_ID)
    # app_init()
    from pages.native.home_page.home_page import HomePage
    hm = HomePage()
    # hm.handle_home_page_popup()
    pp = hm.goto_personal_page()
    bind_status = pp.is_bind_account()
    pp.back_to_home_page()
    if bind_status:   # 如果是三方账号  直接走注销流程
        from flow.native.delete_account_flow import DeleteAccountFlow
        daf = DeleteAccountFlow()
        daf.del_acc_flow()
    else:
        from flow.native.logout_flow import LogoutFlow
        lf = LogoutFlow()
        lf.logout_form_home_page()
        try:
            stop_app(Config.BUNDLE_ID)
        except Exception as e:
            pass
        app_init()
    return lp


@pytest.fixture()
def clear_app_data():
    clear_app(Config.BUNDLE_ID)
    app_init()
    # from pages.native.login_register.login_page import LoginPage
    # return LoginPage()


@pytest.fixture()
def start_another_devices():

    another_device = Config.PACKAGE_LIST['android']['another_devices'][0]
    # print(f"another_device = {another_device}")
    app_init(dev=another_device)
    # idx = another_device.split('///')[1]
    # print(f"G.DEVICE_LIST[1]= {G.DEVICE_LIST[1]}")
    return G.DEVICE_LIST[1]


@pytest.fixture()
def another_device_login(start_another_devices):

    pass


@pytest.fixture()
def another_device_no_login(start_another_devices):

    pass


@pytest.fixture()
def another_devices_clear_data(start_another_devices):

    pass

