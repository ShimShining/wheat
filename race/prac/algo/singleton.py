# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/8
Describe:单例
"""
from threading import Lock


class SingletonHungry:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


class SingletonLazy:
    __instance = None
    __instance_lock = Lock()

    @classmethod
    def get_instance(cls):
        with cls.__instance_lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)

        return cls.__instance


if __name__ == "__main__":
    hs1 = SingletonHungry()
    hs2 = SingletonHungry()

    assert id(hs1) == id(hs2)

    ls1 = SingletonLazy.get_instance()
    ls2 = SingletonLazy.get_instance()

    assert id(ls1) == id(ls2)
