# -*- coding: utf-8 -*-
"""
@Author: shining
@File: base_app.py
@Date: 2022/5/20 2:09 下午
@Version: python 3.9
@Describe:
"""
import sys
import random
from functools import wraps
from typing import Union
import allure
from poco.drivers.unity3d import UnityPoco
from poco.exceptions import PocoNoSuchNodeException, PocoTargetTimeout

from base.UPath import UPath
from config import Config
from utils.log import Logger
from airtest.core.api import *
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

## demo code
# ios连接设备
# auto_setup(__file__)
# connect_device("ios:///x.x.x.x:8100")  # 放到fixture中去做
#
# # 初始化iOS原生poco
# poco = iosPoco()
# # 点击Home键
# keyevent("HOME")
# # 截屏
# snapshot()
# # 滑动操作
# swipe(Template(r"tpl1561985939879.png", record_pos=(0.356, -0.174), resolution=(750.0, 1334.0)),
#       vector=[-0.685, 0.0481])
#
# # 点击app Safari
# poco("Safari").click()
# # 点击浏览器的搜索框
# poco("URL").click()
# # 输入“airtest”
# text("airtest")
#
# # poco的滑动
# poco("People also search for").swipe([-0.0541, -0.4206])
# # 判断是否存在某个截图目标
# exists(Template(r"tpl1560844284543.png", record_pos=(-0.292, 0.688), resolution=(750, 1334)))

try:
    log_file_name = ".".join(sys.argv[1].replace(".py::", ".").replace("::", ".").split(".")[-2:])
except:
    # todo 直接在文件夹下执行，不加参数的pytest，期望是带文件夹的名字作为log_file_name
    log_file_name = "base_app兜底日志文件名"

# print(f"base_api的日志文件名：{log_file_name}")
print(sys.argv)
logger = Logger(log_file_name).logger
logger.info("<== logger 初始化完成，开始收集日志 ==>")
# logger.info(f"sys.argv参数列表={sys.argv}")
logger.info(f"log主文件路径={log_file_name}")


def get_poco(platform='android', device=None):
    if platform == 'android':
        return AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False, device=device)
    if platform == 'ios':
        return iosPoco(device=device)
    if platform == 'u3d':
        return UnityPoco(device=device)
    return AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False, device=device)


class BaseApp:
    popup_black_lists = []

    def __init__(self, po=None, platform=None, mutil_device=None):
        self.log = logger
        if platform:
            self.platform = platform
        else:
            self.platform = Config.PLATFORM
        if po:
            self.poco = po
            return
        self.poco = get_poco(self.platform, device=mutil_device)

    # @abc.abstractmethod
    # def get_locator(self):
    #
    #     pass

    def __getattr__(self, item):
        """
        __getattribute__: 是无条件被调用。对任何对象的属性访问时,都会隐式的调用
        _getattr_(self, item) 获取实例的属性时，仅当实例属性中不包括item时，才被调用
        :param item:
        :return:
        """
        return self.get_locator()[item]

    def popup_handler(func, times=3):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            flag = False
            for i in range(times):
                # print(f'type(self)=={type(self)}')
                # print(dir(self))
                self.log.info(f"base_app尝试第{i + 1}次查找并点击元素kwargs={kwargs}, args={args}")
                try:
                    func(self, *args, **kwargs)
                    flag = True
                    break
                except Exception as e:
                    self.log.info(f"捕获异常{e}")
                    self.popup_click(times=i + 1)

            if not flag:
                self.log.info(f"元素{times}次查找未找到，flag={flag},尝试最后一次操作")
                func(self, *args, **kwargs)

        return wrapper

    def popup_click(self, times=1):
        # self.log.info(f"base_app 第{times}次查找元素捕获异常[PocoNoSuchNodeException]，进入弹窗处理逻辑")
        for popup in self.popup_black_lists:
            # self.log.info(f"处理popup = {repr(popup)}")
            if self.is_exist(popup):
                self.random_click(0.1, 0.1)
                # self.log.info(f"base_app 第{times}次查找元素捕获异常[PocoNoSuchNodeException]，弹窗={repr(popup)}处理成功")

    def find(self, u: Union[dict, list, tuple, UPath], timeout=5):
        """
        #TODO  加入等待时长
        # select by node name
        poco('bg_mission')
        # select by name and other properties
        poco('bg_mission', type='Button')
        poco(textMatches='^据点.*$', type='Button', enable=True)
        :return:
        """
        if isinstance(u, UPath):
            u = u
        elif isinstance(u, (list, tuple)):
            if self.platform == 'android':
                u = u[0]
            elif self.platform == 'ios':
                u = u[1]
            else:
                u = u[0]
        else:
            u = u.get(self.platform, None)
        if not u:
            raise ValueError("")

        if isinstance(u, (iosPoco, AndroidUiautomationPoco, UnityPoco)):
            return u
        loc = u.loc
        kwargs = u.kwargs
        if not kwargs:
            return self.poco(*loc)
        if loc and kwargs:
            return self.poco(*loc, **kwargs)
        if not loc and kwargs:
            return self.poco(**kwargs)

    @popup_handler
    def find_and_click(self, u: Union[dict, list, tuple, UPath], timeout=10):

        self.popup_click()
        self.wait_for_visible(u, timeout=timeout)
        self.find(u).click()

    @popup_handler
    def input_text(self, u, content="default"):

        # self.find_and_click(u)
        self.find(u).set_text(content)

    @popup_handler
    def find_by_relative_selector(self, u: Union[dict, list, tuple, UPath]):

        u = u.get(self.platform, None)
        if not u:
            raise ValueError("")
        if u.loc and len(u.loc) == 3:
            node, child, offspring = u.loc
            return self.poco(node).child(child).offspring(offspring)
        elif u.kwargs:
            params = u.kwargs
            node = params.get('node', None)
            child = params.get('node', None)
            offspring = params.get('node', None)
            if not node:
                raise ValueError("相对选择器定位传入的参数不正确,需要传入参数node")
            if child and not offspring:
                return self.poco(node).child(child)
            if offspring and not child:
                return self.poco(node).offspring(offspring)
            if not child and not offspring:
                return self.poco(node)
            return self.poco(node).child(child).offspring(offspring)
        else:
            raise ValueError('相对选择器定位传入的参数不正确，loc或者kwargs必传一个')

    @popup_handler
    def finds(self, u: Union[dict, list, tuple, UPath]):

        items = self.find(u)
        return items

    @popup_handler
    def swipe_find_by_text(self, text, limit=5):
        '''
        滑动查找text
        :param text:
        :param limit:
        :return:
        '''
        for i in range(limit):
            try:
                element = self.poco(textMatches=f'^{text}.*$', type='Button', enable=True)
                element.wait_for_appearance(timeout=10)
                self.log.info(f"查找包含文本={text}元素成功")
                return element
            except PocoTargetTimeout:
                self.log.info(f"未找到{text}文本,继续滑动查找")
                # 滑动
            if i == limit - 1:
                self.log.error(f"查找包含文本={text}元素失败")
                raise PocoNoSuchNodeException(f"查找包含文本={text}的元素[{i + 1}]次后未找到.")

    @popup_handler
    def swipe_up(self, u: dict, **kwargs):

        elem = self.find(u)
        elem.swipe('up', **kwargs)

    def swipe_left(self, u: dict, **kwargs):
        elem = self.find(u)
        elem.swipe('left', **kwargs)

    def swipe_right(self, u: dict, **kwargs):
        elem = self.find(u)
        elem.swipe('right', **kwargs)

    def swipe_down(self, u: dict, **kwargs):
        elem = self.find(u)
        elem.swipe('down', **kwargs)

    def swipe_by_vector(self, v, **kwargs):
        self.poco.swipe(v, **kwargs)

    def drag(self, u1: dict, u2: dict):

        elem1 = self.find(u1)
        elem2 = self.find(u2)
        elem1.drag_to(elem2)

    def find_element_center(self, u: dict):
        elem = self.find(u)
        return elem.focus('center')

    def is_exist(self, u: Union[dict, list, tuple, UPath], timeout=15):
        """
        判断元素是否存在
        :param u:
        :param timeout:
        :return: True False
        """
        return self.find(u, timeout=timeout).exists()

    # def is_visible(self, u: Union[dict, list, tuple, UPath], timeout=5):
    #     """
    #     元素是否可见 exist就是通过visible来判断的
    #     :param u:
    #     :param timeout:
    #     :return:
    #     """
    #     elem = self.find(u, timeout=timeout)
    #     return elem.visible

    def wait_for_exist(self, u: Union[dict, list, tuple, UPath], timeout=5):
        elem = self.find(u)
        return elem.wait(timeout=timeout).exists()

    def wait_for_visible(self, u: Union[dict, list, tuple, UPath], timeout=15):
        elem = self.find(u)
        if elem.wait(timeout=timeout).exists():
            return elem.wait_for_appearance(timeout=timeout)

    def wait_for_invisible(self, u: dict, timeout=5):
        elem = self.find(u)
        if elem.wait(timeout=timeout).exists():
            return elem.wait_for_disappearance(timeout=timeout)

    def random_click(self, x=None, y=None):
        x = x if x else random.randint(10, 500)
        y = y if y else random.randint(10, 1000)

        self.poco.click((x, y))

    def save_screenshot(self, src_des):
        """
        截图
        :param src_des:截图说明
        :return:
        """
        OUTPUTS_DIR = 'D:\\personProc\\crypto_test\\logs'
        file_name = OUTPUTS_DIR + "\\{}_{}.png".format(time.strftime("%Y%m%d%H%M", time.localtime(time.time())),
                                                       src_des)
        self.poco.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
            allure.attach(file, src_des, allure.attachment_type.PNG)
        self.log.info("页面截图文件保存在：{}".format(file_name))

    def clear_env(self):

        pass

    def air_touch(self, image, times=3, **kwargs):
        for i in range(times):
            try:
                if isinstance(image, tuple):
                    if not self.air_exist(Template(*image), **kwargs):
                        self.air_wait(Template(*image), **kwargs)
                    return touch(Template(*image), **kwargs)
                if not self.air_exist(image, **kwargs):
                    self.air_wait(image, **kwargs)
                touch(image, **kwargs)
                return
            except TargetNotFoundError:
                if i + 1 >= times:
                    raise TargetNotFoundError(f"查找图片元素{image},{times}次失败")

    def air_wait(self, image, **kwargs):

        wait(image, **kwargs)

    def air_swipe(self, iamge_a, image_b=None, vector=None, **kwargs):

        swipe(iamge_a, v2=image_b, vector=vector, **kwargs)

    def air_exist(self, image):

        return exists(image)

    def air_text(self, content, **kwargs):

        text(content, **kwargs)

    def air_keyboard(self, keyname, **kwargs):

        keyevent(keyname, **kwargs)

    def air_snapshot(self, filename=None, msg='默认截图'):

        snapshot(filename=filename, msg=msg)

    def air_assert_exists(self, image, msg='断言存在'):

        assert_exists(image, msg)

    def air_assert_not_exists(self, image, msg='断言不存在'):

        assert_not_exists(image, msg)

    def air_assert_equal(self, actual, expect, msg='断言相等'):

        assert_equal(actual, expect, msg)

    def air_assert_not_equal(self, actual, expect, msg='断言不相等'):

        assert_not_equal(actual, expect, msg)

    def start_app_by_pkg(self, pkg):

        start_app(package=pkg)

    def sleep(self, sec):

        time.sleep(sec)

    def change_device(self, device=0):

        set_current(device)

    @property
    def cur_device(self):

        return device()


if __name__ == '__main__':
    b = BaseApp()
    b.find_and_click(UPath(name="aaa"))
