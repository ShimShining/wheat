# -*- coding: utf-8 -*-
"""
@Author: shining
@File: UPath.py
@Date: 2022/5/25 2:54 下午
@Version: python 3.9
@Describe: 自定义UI控件定位
"""
import copy

from config import Config


class UPath:

    def __init__(self, host=True, *loc, **kwargs):

        if host:
            pre = Config.BUNDLE_ID + ":"
            # 处理元组类型的参数
            list_a = []
            for item in loc:
                item = pre + item
                list_a.append(item)
            # 处理关键字类型的参数
            data = copy.deepcopy(kwargs)
            # resourceId=id/googleBtn&k=com.pointone.BPdyglobal.debug:id/googleBtn
            for k, v in data.items():
                kwargs[k] = pre + v
            self.loc = tuple(list_a)
            self.kwargs = kwargs
        else:
            self.loc = loc
            self.kwargs = kwargs

    @property
    def get_loc(self):
        return self.loc

    @property
    def get_properties(self):

        return self.kwargs

    def __str__(self):
        if self.loc:
            return "locator：" + str(self.loc) + " || kwargs: " + str(self.kwargs)
        return "kwargs: " + str(self.kwargs)

    def __repr__(self):
        if self.loc:
            return "locator：" + str(self.loc) + " || kwargs: " + str(self.kwargs)
        return "kwargs: " + str(self.kwargs)


if __name__ == "__main__":

    a = UPath(host=True, resourceId="id/googleBtn")
    print(a)
    print(a.loc)
    print(a.kwargs)

