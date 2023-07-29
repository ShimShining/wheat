# -*- coding: utf-8 -*-
"""
@Author: shining
@File: my_thread.py
@Date: 2022/6/23 5:22 下午
@Version: python 3.9
@Describe: 自定义多线程类
"""
import threading
from threading import Lock


class MyThread(threading.Thread):
    lock = Lock()  # 初始化线程锁

    def __init__(self, func,with_lock=False, args=(), kwargs={}):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = None
        self.with_lock = with_lock

    def run(self):
        # 对线程进行加锁，防止多线程下数据访问混乱
        if self.with_lock:
            with self.lock:
                self.result = self.func(self.args, **self.kwargs)
                # self.result = self.func(self.kwargs)
                # print(self.result)
        # 无锁模式，运行更快
        else:
            self.func(self.args, **self.kwargs)  # 不加锁试试
            self.result = self.func(self.kwargs)
            # print(self.result)

    def get_result(self):

        try:
            return self.result
        except Exception as e:
            return None


def print_i(info):
    print(i)
    return info['host']


if __name__ == "__main__":
    result = []
    threads = []

    for i in range(10):
        info = {}
        info['host'] = i
        t = MyThread(print_i, kwargs=info)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()  # 一定执行join,等待子进程执行结束，主进程再往下执行
        result.append(t.get_result())
    print(result)
