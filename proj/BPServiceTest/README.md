![]()
- [1.BPServiceTest](#1-BPServiceTest)
  - [2 使用](#2-使用)
    - [3 源码拉取](#3-源码拉取)
    - [4 运行](#4-运行)
  - [5 公共模块](#5-公共模块)
  - [6 框架介绍](#6-框架介绍)
  - [7 快速上手](#7-快速上手)
  - [8 联系作者](#8-联系作者)

# 1 BPServiceTest
- API自动化仓库
## 2 使用
### 3 源码拉取
- 项目拉取
```angular2html
git clone 
```
- 依赖安装
```angular2html
cd BPServiceTest
pip3 install -r requirements.txt
```
- 开发规范
  - 主分支拉取到本地后，新建自己的分支进行开发，禁止直接在master分支开发
  - 本地开发后需调试通过所有的测试case，才能上传到远程仓库
  - python开发遵循[PEP8规范](http://c.biancheng.net/view/4184.html)
  - 合并到master需通过远程进行pull request
```angular2html
# own_branch_name是指自己的分支名字
git checkout -b own_branch_name
# 查看是否在自己新建的分支上
git branch
```
### 4 运行
- 国外
```angular2html
cd BPServiceTest
pytest testcase
```
## 5 公共模块
- base
  - 封装http请求基类
  - 封装业务基类
  - 封装测试基类
- utils
  - 封装各类工具
- notification
  - 存放测试报告发送所需要的数据
- log
  - 存放本地运行log日志文件
## 6 框架介绍
- 项目结构
```angular2html
├── base
│   ├── __init__.py
│   ├── base_api.py
│   ├── base_api_test.py
│   ├── base_app_page.py
│   ├── base_test.py
│   └── bp_api.py
├── log
├── notification
│   ├── __init__.py
│   ├── lark.py
│   └── u_api_report.yml
├── u_api_test
│   ├── __init__.py
│   ├── business
│   ├── config.py
│   ├── conftest.py
│   ├── data
│   ├── flow
│   ├── test_engine_server_case
│   ├── testcase
│   ├── tools
│   └── u_global_variable.py
├── utils
│   ├── __init__.py
│   ├── data_model.py
│   ├── decorator.py
│   ├── fake.py
│   ├── json_handler.py
│   ├── log.py
│   ├── my_thread.py
│   ├── proxy.py
│   ├── pytest_auto_parametrize.py
│   ├── read_config.py
│   ├── read_yaml.py
│   ├── time_tools.py
│   └── uuid_random.py
├── README.md
├── pytest.ini
├── requirements.txt
├── send_engine_report_to_lark.py
├── send_lark_report.py
└── send_lark_report_with_params.py
```
## 7 快速上手
- [从零到一编写一个接口自动化case最佳实践]()

## 8 联系作者
- 有任何问题请联系@shining