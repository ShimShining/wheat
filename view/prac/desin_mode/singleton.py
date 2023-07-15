# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/7/15
Describe:单例
单例模式定义: 具有该模式的类只能生成一个实例对象
"""


# 1.装饰器方式1实现单例
def singleton(cls, *args, **kwargs):

    instance = {}

    def get_instance(*args, **kwargs):

        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


# 2.装饰器方式2实现单例
def wrapper(cls):
    def inner(*args, **kwargs):
        if not hasattr(cls, 'ins'):
            ins_obj = cls(*args, **kwargs)
            setattr(cls, "ins", ins_obj)
        return getattr(cls, "ins")
    return inner


@singleton
class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age


@wrapper
class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color


# 懒汉式单例


# 饿汉式单例


if __name__ == '__main__':
    p1 = People("lily", 19)
    p2 = People("Tom", 20)
    assert id(p1) == id(p2)
    print(f"p1.name = {p1.name},p1.age = {p1.age}")
    print(f"p2.name = {p2.name},p2.age = {p2.age}")

    a1 = Animal('cat', 'gray')
    a2 = Animal("dog", "yellow")
    assert id(a1) == id(a2)
    print(f"a1.name = {a1.name},a1.color = {a1.color}")
    print(f"a2.name = {a2.name},a2.color = {a2.color}")

