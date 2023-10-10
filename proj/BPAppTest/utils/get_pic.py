# -*- coding: utf-8 -*-
"""
@Author: shining
@File: get_pic.py
@Date: 2022/10/19 5:29 下午
@Version: python 3.9
@Describe:
"""
import importlib.resources as r
import sys

import pic_source.avatar as pkg


class GetPIC:

    @classmethod
    def get_pic(cls, package=pkg, pic_name=""):
        # 返回图片的二进制内容如果此种方式不行，就需要那路径传path了
        if pic_name and "." not in pic_name:
            pic_name = pic_name + r".png"
        if sys.version_info >= (3, 9):
            file_path = r.files(package)
            pic_path = str(file_path) + r"/" + pic_name
            return pic_path
        # 兼容3.8及以下版本无 r.files(package)方法
        with r.path(package, pic_name) as pic_path:
            pic_path = pic_path
        return pic_path


if __name__ == '__main__':

    pic = GetPIC.get_pic(pic_name="avatar_done")
    print(pic)

