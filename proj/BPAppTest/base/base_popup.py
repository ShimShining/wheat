# -*- coding: utf-8 -*-
"""
@Author: shining
@File: base_popup.py
@Date: 2022/10/26 5:46 下午
@Version: python 3.9
@Describe: 弹窗基类
"""
import time
from abc import ABC, abstractmethod


# class BasePopHandler(ABC):
#
#     """
#     被观察者
#     """
#     @abstractmethod
#     def handler(self, popup: 'BasePopUp'):
#
#         pass


class BasePopUp(ABC):
    """
    观察者
    """
    @abstractmethod
    def check(self, elem):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observe(ABC):

    @abstractmethod
    def update(self, notice):
        pass


class Notice(ABC):

    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def notify(self):
        pass


class BasePopHandler(Notice):

    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for obs in self.__observers:
            obs.update(self)


class PopupHandler(BasePopHandler):

    def __init__(self, popup=None):
        super().__init__()
        self.__popup = popup

    @property
    def popup(self):
        return self.__popup

    @popup.setter
    def popup(self, pop_up):
        self.__popup = pop_up
        self.notify()


class CheckInPopup(Observe):

    def __init__(self):
        self.popup = None

    def update(self, notice):
        self.popup = notice.popup


class TapToCreatePopup(Observe):

    def __init__(self):
        self.popup = None

    def update(self, notice):
        self.popup = notice.popup


class InstallBugPopup(Observe):

    def __init__(self):
        self.popup = None

    def update(self, notice):
        self.popup = notice.popup

"""
说明：利用子进程对页面元素进行监控，发元素后，自动操作。

适用场景：多用于不可预测的弹窗或元素

用法：watcher(text=None, textMatches=None, timeout=10, poco=None)
"""
def loop_watcher(find_element, timeout):
    """
    循环查找函数：每隔一秒，循环查找元素是否存在. 如果元素存在，click操作
    :param find_element: 要查找元素，需要是poco对象
    :param timeout: 超时时间，单位：秒
    :return:
    """
    start_time = time.time()
    while True:
        # find_element.invalidate()
        if find_element.exists():
            find_element.click()
            print("观察者：发现元素")
            break
        elif (time.time() - start_time) < timeout:
            print("--------------------观察者：等待1秒")
            time.sleep(1)
        else:
            print("观察者：超时未发现")
            break


def watcher(text=None, textMatches=None, timeout=10, poco=None):
    """
    观察者函数: 根据text或textMatches定位元素，用子进程的方式循环查找元素，直到超时或找到元素
    :param text: 元素的text
    :param textMatches: 元素的textMatches，正则表达式
    :param timeout: 超时时间
    :param poco: poco实例
    :return:
    """
    print("观察者：启动")
    # 目标元素
    find_element = None
    if poco is None:
        raise Exception("poco is None")
    if text or textMatches:
        if text:
            find_element = poco(text=text)
        elif textMatches:
            find_element = poco(textMatches=textMatches)

    # 定义子线程: 循环查找目标元素
    from multiprocessing import Process
    p = Process(target=loop_watcher, args=(find_element, timeout,))
    p.start()
"=========================================="
# ToDo 弹窗作为被观察者，处理弹窗作为观察者 实现
"=========================================="
if __name__ == '__main__':
    hand = PopupHandler("this is a  popup a")
    p1 = CheckInPopup()
    p2 = TapToCreatePopup()
    p3 = InstallBugPopup()
    hand.attach(p1)
    hand.attach(p2)
    hand.attach(p3)
    hand.popup = "处理弹窗"
    print(p1.popup)
    print(p2.popup)
    print(p3.popup)
    hand.detach(p2)
    hand.popup = "再次处理两个弹窗"
    print(p1.popup)
    print(p2.popup)
    print(p3.popup)
