![]()
- [BPUITest](#BPUITest)
  - [使用](#使用)
    - [源码拉取](#源码拉取)
    - [虚拟环境及依赖安装](#虚拟环境及依赖安装)
    - [开发规范](#开发规范)
    - [运行](#运行)
  - [项目结构介绍](#项目结构介绍)
  - [快速上手](#快速上手)
  - [联系作者](#联系作者)
# BPUITest
- UI自动化仓库
    
## 使用
### 源码拉取
```angular2html
git clone 
```

### 虚拟环境及依赖安装

```angular2html
# 进入本地项目根目录
cd BPUITest

# 创建UI自动化虚拟环境
# mac
python3 -m venv venv
. venv/bin/activate

# windows
python3 -m venv venv
venv\Scripts\activate
# 激活后，终端会显示虚拟环境的名称venv，如下示例：
(venv) 用户名 BPUITest % 

# 安装依赖
pip3 install -r requirements.txt
```
### 开发规范
- 开发规范
  - 主分支拉取到本地后，新建自己的分支进行开发，禁止直接在master分支开发
    - master分支只会做一个操作：git pull
  - 本地开发后需调试通过所有的测试case，才能上传到远程仓库
  - python开发遵循[PEP8规范](http://c.biancheng.net/view/4184.html)
  - 提交规范
    - 提交时，先在自己的分支commit后
    - 再切换到master分支git pull
    - 再切换到自己的分支：git merge master（此处可能会有冲突，需在本地解决）
    - 再进行推送到远程自己的分支
    - 在github上提交pull request，向master提交，需要指定***code reviewer***
  - 自己分支的代码合并到master，必须通过github进行pull request，**禁止**本地分支直接合并到master
```angular2html
# own_branch_name是指自己的分支名字
git checkout -b own_branch_name
# 查看是否在自己新建的分支上
git branch
```
### 运行
- 直接点击用例左边的绿色按钮运行
- 通过命令行运行
```angular2html
cd testcase
pytest
```
- 通过case文件的main函数运行
```angular2html
if __name__ == '__main__':
    pytest.main(["-s", "-v"])    # 运行所有用例:
    pytest.main(["-s", "-v", "mod.py"])   # 运行对应模块的用例 
```
## 项目结构介绍

- base：基础模块
- pages： 页面封装
- pic_source: u3d界面图片资源
- flow： 业务流
- log: 日志文件存储目录
- testcase：测试用例目录
- data：测试数据
- notification： 通知模块
- pkg_manage：测试包管理
- utils： 工具模块
- tools：测试场景工具
- 其他（配置，环境变量，依赖等）
```angular2html
├── base
│   ├── UPath.py
│   ├── app.py
│   ├── base_app.py
│   ├── base_popup.py
│   ├── base_test.py
│   └── bp_app.py
├── flow
│   ├── native
│   └── u3d
├── log
├── notification
│   ├── lark.py
│   └── us_api_report.yml
├── page
│   ├── Explore_PropsClothing_page.py
│   ├── Home_page.py
│   └── Personal_Center_page.py
├── pages
│   ├── native
│   ├── popup.py
│   └── u3d
├── pic_source
│   ├── avatar
│   ├── editor
│   ├── emote
│   └── room
├── pkg_manage
├── resource
├── send_report_to_lark.py
├── testcase
│   ├── bp_app_test.py
│   ├── test_home_page
│   ├── test_login_register
│   ├── test_self_profie_manage
│   └── test_u3d_engine
├── data
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
├── app_global_variable.py
├── tools
│   └── join_odyssey.py
└── utils
    ├── datetim_util1e.py
    ├── excel_util1.py
    ├── find_element_util1.py
    ├── get_pic.py
    ├── ini_parser.py
    ├── log.py
    ├── log_util1.py
    ├── screenshot_util1.py
    └── yaml_handler.py
```

## 快速上手
- [从零到一编写一个UI自动化case最佳实践]()
## 联系作者
- 有任何问题请联系@shining 


