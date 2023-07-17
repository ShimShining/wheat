# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/7/16
Describe:
"""
import json
from typing import List
import pytest
import yaml


# @pytest.fixture(scope='class')
# def init_class():
#     print("---- class setup ----")
#     clac = Calculator()
#     yield clac
#     print("---- class teardown ----")
#
#
# @pytest.fixture()
# def init_function():
#     print("---- 开始计算 ----")
#     yield
#     print("---- 计算结束 ----")


def get_yaml_datas():
    with open(r'D:\personProc\wheat\proj\ho_magic\datas\test_1th_work.yml', encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        return datas


# 获取企业微信添加成员信息
def get_wework_data():
    with open(r'D:\personProc\wheat\proj\ho_magic\datas\wework_member_info.yml', encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        return datas


# 通过fixture将参数传递给添加企业微信成员用例
@pytest.fixture(params=get_wework_data())
def get_member_info(request):
    return request.param


@pytest.fixture(params=get_yaml_datas()['add_equal'],
                ids=get_yaml_datas()['add_equal_ids'])
def get_add_equal_data(request):
    return request.param


@pytest.fixture(params=get_yaml_datas()["add_unequal"])
def get_add_unequal_data(request):
    return request.param


@pytest.fixture(params=get_yaml_datas()["add_exception"])
def get_add_exception_data(request):
    return request.param


@pytest.fixture(params=get_yaml_datas()['div_equal'])
def get_div_equal_data(request):
    return request.param


@pytest.fixture(params=get_yaml_datas()["div_unequal"])
def get_div_unequal_data(request):
    return request.param


@pytest.fixture(params=get_yaml_datas()["div_exception"])
def get_div_exception_data(request):
    return request.param


# 用例名称支持中文显示
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List
):
    # 随机打乱测试用例执行顺序
    # random.shuffle(items)
    print(f"items的类型={type(items)}")
    for case in items:
        case.name = case.name.encode('utf-8').decode('unicode-escape')
        case._nodeid = case._nodeid.encode("utf-8").decode('unicode-escape')
    return items


# 自定义命令行参数 action=store
# 默认，只存储参数的值，可以存储任何类型的值，此时 default 也可以是任何类型的值，
# 而且命令行参数多次使用也只能生效一个，最后一个值覆盖之前的值
# def pytest_addoption(parser):
#     parser.addoption("--cmd-opt", action="store",
#                      default="None",
#                      help="自定义命令行参数,'--cmdopt' 添加到pytest配置中")

# 自定义命令行参数 action=append,存储一个列表
# def pytest_addoption(parser):
#     parser.addoption("--cmd-opt", action="append",
#                      default=["这是一个默认值"],
#                      help="action=append的命令行参数")


# action=store_const,使用const为命令行参数指定一个常量值,必须和const参数同时使用,使用这个模式
# 后,命令行参数不能赋值
# def pytest_addoption(parser):
#     parser.addoption("--cmd-opt", action='store_const',
#                      default="这是默认参数",
#                      const="命令行参数的常量值",
#                      help="常量命令行参数值")

# action="append_const":存储一个列表,使用const为命令行指定一个常量值,并将DEFAULT
# 和const常量值添加到列表,可同时多次使用自定义参数,不能赋值,只能使用常量
# def pytest_addoption(parser):
#     parser.addoption("--cmd-opt", action="append_const",
#                      default=["DEFAULT_VALUE"],
#                      const="CMD_CONST_VALUE",
#                      help="append_const 命令行参数")


# type:可以适python的基础数据类型,str,int,float,list等,不指定类型,默认为str
# tips:type指定类型时,DEFAULT也需要修改为同样的类型
# def pytest_addoption(parser):
#     parser.addoption("--cmd-opt", action="store",
#                      default=1,
#                      type=int,
#                      help="指定type参数类型")


# # choices:指定几个值,自定义参数必须在这几个值中选择一个,否则会报错
# def pytest_addoption(parser):
#     parser.addoption('--cmd-opt', action='store',
#                      default='100',
#                      choices=["python", "java", "c++"],
#                      help='带choices=[""python", "java", "c++"]的命令行参数')

# @pytest.fixture(scope='session')
# def cmd_opt(pytestconfig):
#     return pytestconfig.getoption('--cmd-opt')
#
#
# @pytest.fixture(autouse=True)
# def input_cmdopt(cmd_opt):
#
#     print(f"===> --cmd-optde = {cmd_opt}")


def pytest_addoption(parser):
    parser.addoption("--case-rank", action="store",
                     default=0,
                     choices=[0, 1],
                     type=int,
                     help="自定义命令行参数,'--case-rank',打印用例执行时的顺序值,\
                          添加到pytest配置中")

# config对象获取cmdopt值
@pytest.fixture(scope='session')
def case_rank(pytestconfig):

    return pytestconfig.getoption('--case-rank')

# @pytest.fixture(autouse=True)
# def get_caserank(case_rank):
#
#     print(case_rank)

#
# def pytest_runtest_logstart(
#     nodeid: str, location
# ) -> None:
#     rank = 1
#     print("这是一个hook函数")
#     print(f"CASE_RANK={rank}")

# 企业微信数据获取
def get_wework_depart():

    with open(r'D:\personProc\wheat\proj\ho_magic\datas\add_department.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas


@pytest.fixture(params=get_wework_depart())
def get_depart(request):
    return request.param


def get_tags_data():

    with open(r'D:\personProc\wheat\proj\ho_magic\datas\tags.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas


@pytest.fixture(params=get_tags_data()["json"])
def get_tags_json(request):

    print(request.param)
    print(f"confetest参数类型={type(request.param)}")
    return request.param


@pytest.fixture(params=get_tags_data()["group_tags"])
def get_tags(request):

    print(request.param)
    print(f"confetest参数类型={type(request.param)}")
    return request.param


@pytest.fixture(params=get_tags_data()["tags_order"])
def get_tags_order(request):

    print(request.param)
    print(f"confetest参数类型={type(request.param)}")
    return request.param


# def get_mustache_data(data):
#     import chevron
#     with open("D:\personProc\hogwarts_shining\homework_test" \
#               "\\test_wework_api_2th_work\\template\\add_member_template.mustache", \
#               encoding="utf-8") as f:
#         temp = f.read()
#     print("=========================")
#     datas = chevron.render(temp, data)
#     print("++++++++++++++++")
#     print(type(datas))
#     print(datas)
#     print("+++++++++++++++++++++")
#     return json.loads(datas)


def get_member():

    with open(r'D:\personProc\wheat\proj\ho_magic\datas\add_member.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas


@pytest.fixture(params=get_member())
def get_member_data(request):

    print(request.param)
    print(f"confetest参数类型={type(request.param)}")
    request.param = get_mustache_data(request.param)
    print(f"confetest+mustache参数类型={type(request.param)}")
    print(request.param)
    return request.param






























