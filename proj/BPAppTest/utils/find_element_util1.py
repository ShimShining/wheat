__author__ = "liwen"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco#安卓
from faker import Faker
from conf.Home_conf import E_home
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)#安卓
#------------------------------------
from conf.By_Element_conf import *

fk = Faker(locale='zh_CN')
# app启动
def Startapp(包名):
    start_app(包名)
    return Startapp
#关闭app 切换后台
def Stopapp(包名):
    stop_app(包名)
    return Stopapp
#清除数据
def Clearapp(包名):
    clear_app(包名)
    return Clearapp
#卸载包
def Uninstall(包名):
    uninstall(包名)
    return Uninstall
#安装包
def Install(包名):
    install(filepath="要在目标设备上安装的文件的路径")
    return Install

'''
点击操作
截图并且保存到响应的路径下
'''
def Snapshot():
    snapshot(filename='/Users/liwen/UIAirTest/util', msg='是否存在')

"""双击"""
def Doublelick(双击):
    double_click(双击)
    return Doublelick()

'''
#滑动的起点和终点
def Swipe(v1,v2):
    swipe(v1,v2)
'''

"""输入文本"""
def Text():
    text()
    return Text

"""定位元素"""
def Exists(定位元素):
    os.path.exists(定位元素)
    return Exists

"""随机生成一个时间"""
def radom_date_time():
    return fk.date_time()

"""随机生成一个ipv4的地址"""
def random_ipv4():
    return fk.ipv4()
