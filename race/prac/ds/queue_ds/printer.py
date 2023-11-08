# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/11/8
Describe: 打印机模拟
"""
import random

from race.prac.ds.queue_ds.queue_ds import Queue


class Printer:

    def __init__(self, ppm):  # ppm 打印速度
        self.pagerate = ppm
        self.cur_task = None  # 打印任务
        self.time_remaining = 0   # 任务倒计时

    def tick(self):
        if self.cur_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.cur_task = None

    def busy(self):

        if self.cur_task is not None:
            return True
        return False

    def start_next(self, newtask):
        self.cur_task = newtask
        self.time_remaining = newtask.get_pages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time   # 作业生成时间戳
        self.pages = random.randrange(1, 21)  # 作业需要打印的页数

    def get_stamp(self):

        return self.timestamp

    def get_pages(self):

        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp  # 作业等待时间


def new_print_task():
    num = random.randrange(1, 181)
    if num == 2:
        return True
    return False


def simulation(num_seconds, ppm):
    lab_p = Printer(ppm)   # 实例打印机
    print_queue = Queue()  # 打印任务队列
    wait_times = []        # 任务等待时间列表
    # 模拟时间流逝
    for current_second in range(num_seconds):
        # 新任务生成
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)
        # 开启打印任务
        if not lab_p.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            wait_times.append(next_task.wait_time(current_second))
            lab_p.start_next(next_task)

        lab_p.tick()

    average_wait = sum(wait_times) / len(wait_times)

    print(f"Average Wait {average_wait} sec {print_queue.size()} tasks remaining.")


if __name__ == '__main__':

    for i in range(10):
        simulation(3600, 10)

