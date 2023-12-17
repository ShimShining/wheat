# -*- coding: utf-8 -*-
"""
Author : shining
Date: 2023/7/15
Describe:单例
单例模式定义: 具有该模式的类只能生成一个实例对象
饿汉式单例;懒汉式单例
"""
from threading import Lock


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
class LazyIdMaker:
    __instance = None
    __id = 1
    __instance_lock = Lock()

    def __new__(cls):
        pass

    @classmethod
    def get_instance(cls):
        # 避免多线程同时创建多个实例,创建的时候加锁
        with cls.__instance_lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance

    def get_id(self):
        self.__id += 1
        return self.__id


def test_lazy_id_maker():
    # IdMaker 是单例类，只允许有一个实例

    a = LazyIdMaker.get_instance()
    b = LazyIdMaker.get_instance()
    c = LazyIdMaker.get_instance()

    id1 = a.get_id()

    id2 = b.get_id()

    id3 = c.get_id()

    print(id1, id2, id3)
    assert id(a) == id(b)
    assert id(b) == id(c)


# 饿汉式单例
class HungryIdMaker:
    __instance = None
    __id = -1

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def get_id(self):
        self.__id += 1
        return self.__id


def test_hungry_id_maker():
    # IdMaker 是单例类，只允许有一个实例

    a = HungryIdMaker()
    b = HungryIdMaker()
    c = HungryIdMaker()

    id1 = a.get_id()

    id2 = b.get_id()

    id3 = c.get_id()

    print(id1, id2, id3)
    assert id(a) == id(b)
    assert id(b) == id(c)


# metaclass 实现单例
class SingtonType(type):
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingtonType._lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingtonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=SingtonType):
    def __init__(self, name):
        self.name = name


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

    test_lazy_id_maker()
    test_hungry_id_maker()

    f1 = Foo('obj_a')
    f2 = Foo("obj_b")
    print(id(f1), id(f2))
