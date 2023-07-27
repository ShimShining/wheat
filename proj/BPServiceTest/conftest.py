# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: conftest.py
@Date: 2021/12/25 12:00 上午
@Version: python 3.10
@Describe:
"""
import time
from typing import List
import datetime
import os
from jinja2 import Environment, FileSystemLoader

import pytest

import proj.BPServiceTest.global_variable as ugv
from proj.BPServiceTest.utils.global_config import GlobalConfig
from proj.BPServiceTest.utils.read_yaml import ReadYAML


ugv._init()

hosts = {
    'dev': "",
    'master': "MASTER_HOST",
    "alpha": "ALPHA_HOST",
    "grey": "GREY_HOST",    # 后端灰度分支
    "prod": "PROD_HOST"
}

test_result = {
    "title": "",
    "tester": "",
    "desc": "",
    "cases": {},
    'rerun': 0,
    "failed": 0,
    "passed": 0,
    "skipped": 0,
    "error": 0,
    "start_time": 0,
    "run_time": 0,
    "begin_time": "",
    "all": 0,
    "testModules": set()
}


def pytest_make_parametrize_id(config, val, argname):
    if isinstance(val, dict):
        return val.get('title') or val.get('desc')


def pytest_runtest_logreport(report):
    report.duration = '{:.6f}'.format(report.duration)
    test_result['testModules'].add(report.fileName)
    if report.when == 'call':
        test_result[report.outcome] += 1
        test_result["cases"][report.nodeid] = report
    elif report.outcome == 'failed':
        report.outcome = 'error'
        test_result['error'] += 1
        test_result["cases"][report.nodeid] = report
    elif report.outcome == 'skipped':
        test_result[report.outcome] += 1
        test_result["cases"][report.nodeid] = report


def pytest_sessionstart(session):
    start_ts = datetime.datetime.now()
    test_result["start_time"] = start_ts.timestamp()
    test_result["begin_time"] = start_ts.strftime("%Y-%m-%d %H:%M:%S")


from configparser import ConfigParser


def pytest_sessionfinish(session):
    """在整个测试运行完成之后调用的钩子函数,可以在此处生成测试报告"""
    report2 = session.config.getoption('--report')
    # -----------------配置文件的支持------------------------------
    # conf = ConfigParser()
    # name = 'report.html'
    # if session.config.inifile:
    #     conf.read(session.config.inifile,encoding='utf-8')
    # if 'report' in conf.sections():
    #     if 'title' in conf.options('report'):
    #         test_result['title'] = conf.get('report', 'title')
    #     else:
    #         test_result['title'] = '测试报告'
    #     if 'tester' in conf.options('report'):
    #         test_result['tester'] = conf.get('report', 'tester')
    #     else:
    #         test_result['tester'] = '测试员'
    #     if 'desc' in conf.options('report'):
    #         test_result['desc'] = conf.get('report', 'desc')
    #     else:
    #         test_result['tester'] = '无'
    #     if 'file_name' in conf.options('report'):
    #         name = conf.get('report', 'file_name')
    # elif report2:
    #     test_result['title'] = session.config.getoption('--title') or '测试报告'
    #     test_result['tester'] = session.config.getoption('--tester') or '小测试'
    #     test_result['desc'] = session.config.getoption('--desc') or '无'
    #     name = report2
    # else:
    #     return
    # -----------------配置文件的支持------------------------------

    if report2:
        test_result['title'] = session.config.getoption('--title') or '测试报告'
        test_result['tester'] = session.config.getoption('--tester') or '测试'
        test_result['desc'] = session.config.getoption('--desc') or '无'
        name = report2
    else:
        return

    if not name.endswith('.html'):
        file_name = time.strftime("%Y-%m-%d_%H_%M_%S") + name + '.html'
    elif "BUD" in name or 'bud' in name:
        file_name = name
    else:
        file_name = time.strftime("%Y-%m-%d_%H_%M_%S") + name

    if os.path.isdir('reports'):
        pass
    else:
        os.mkdir('reports')
    file_name = os.path.join('reports', file_name)
    test_result["run_time"] = '{:.6f} S'.format(time.time() - test_result["start_time"])
    test_result['all'] = len(test_result['cases'])
    if test_result['all'] != 0:
        test_result['pass_rate'] = '{:.2f}'.format(test_result['passed'] / test_result['all'] * 100)
    else:
        test_result['pass_rate'] = 0
    template_path = os.path.join(os.path.dirname(__file__), './templates')
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('templates.html')
    report = template.render(test_result)
    with open(file_name, 'wb') as f:
        f.write(report.encode('utf8'))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    # for att in dir(report):
    #     if "__" not in att:
    #         print(f"{att}属性值={getattr(report, att)}")
    # print(f"dir pytest_runtest_makereport的report={dir(report)}")
    fixture_extras = getattr(item.config, "extras", [])
    plugin_extras = getattr(report, "extra", [])
    # plugin_extras = getattr(report, "sections", [])
    report.extra = fixture_extras + plugin_extras
    # print(f"report.extra==== {report.extra}")
    report.fileName = item.location[0]
    if hasattr(item, 'callspec'):
        # print(f"item.callspec.id or item._obj.__doc__ = {item.callspec.id or item._obj.__doc__}")
        report.desc = item.callspec.id or item._obj.__doc__
    else:
        report.desc = item._obj.__doc__

    if report.desc:
        report.desc = report.desc.encode('utf-8').decode('unicode-escape')
    report.method = item.location[2].split('[')[0]


def pytest_addoption(parser):
    # group = parser.getgroup("testreport")
    parser.addoption(
        "--report",
        action="store",
        metavar="path",
        default=None,
        help="create html report file at given path.",
    )
    parser.addoption(
        "--title",
        action="store",
        metavar="path",
        default=None,
        help="pytest-testreport Generate a title of the repor",
    )
    parser.addoption(
        "--tester",
        action="store",
        metavar="path",
        default=None,
        help="pytest-testreport Generate a tester of the report",
    )
    parser.addoption(
        "--desc",
        action="store",
        metavar="path",
        default=None,
        help="pytest-testreport Generate a description of the report",
    )
    parser.addoption(
        "--host",
        action='store',
        choices=['dev', 'master', 'alpha', 'grey', 'prod'],
        help="dev: 开发环境；test：测试环境；alpha：预发布环境；grey: 灰度环境；prod：生产环境；默认环境为master"
    )
    parser.addoption(
        "--runversion",
        action='store',
        help="执行的版本"
    )
    parser.addoption(
        "--run-source",
        action='store',
        help="执行的自动化任务来源"
    )


# def pytest_addoption(parser):
#     parser.addoption(
#         "--host",
#         action='store',
#         choices=['dev', 'master', 'alpha', 'grey', 'prod'],
#         help="dev: 开发环境；test：测试环境；alpha：预发布环境；grey: 灰度环境；prod：生产环境；默认环境为master"
#     )
#     parser.addoption(
#         "--runversion",
#         action='store',
#         help="执行的版本"
#     )
#     parser.addoption(
#         "--run-source",
#         action='store',
#         help="执行的自动化任务来源"
#     )


def pytest_configure(config):
    h = hosts.get(config.getoption('--host'), None)
    v = config.getoption('--runversion')
    s = config.getoption('--run-source')
    if h:
        ugv._set("RUN_ENV", h)
    if v:
        ugv._set("RUN_VERSION", v)
    if s:
        ugv._set("RUN_SOURCE", s)


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List):
    """
    测试用例收集完成之后，将收集到的case的name和title兼容中文显示
    :param items:
    :return:
    """
    for case in items:
        case.name = case.name.encode('utf-8').decode('unicode-escape')
        # print(f"开始执行用例{case.name}")
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
    from proj.BPServiceTest.config import Config
    host = Config.get_run_env_name()
    version = Config.get_run_env_version()
    source = Config.RUN_SOURCE
    res["host"] = host
    res['version'] = version
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
    res['source'] = source

    yaml_path = GlobalConfig.ROOT_DIR + "notification/us_api_report.yml"
    ReadYAML.write_yaml(yaml_path, res)
    # print(res)


@pytest.fixture(scope='session')  # session是大家全局共享变量，其他仅限于各自范围内有影响
def BPGlobalArgs():
    return {}
