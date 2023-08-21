# -*- coding: utf-8 -*-
"""
@Author: shining
@File: get_req_json.py
@Date: 2022/9/13 11:12 下午
@Version: python 3.9
@Describe: 获取请求体参数
"""
import importlib.resources as res
import ast

import proj.BPServiceTest.req_json_body.chat as pkg
from proj.BPServiceTest.utils.req_render import *


class GetReqJson:

    @classmethod
    def get_req_json(cls, package=pkg, file_name=""):
        if "." not in file_name:
            file_name = file_name + ".json"
        text = res.read_text(package, file_name, encoding='utf-8', errors='strict')
        return text

    @classmethod
    def assemble_str_req_body(cls, *args, file_name="", delimiter="$", **kwargs):

        text = cls.get_req_json(file_name=file_name)
        t = ast.literal_eval(text)
        body = REQRender.render(t, *args, delimiter=delimiter, **kwargs)
        return body

    @classmethod
    def assemble_dict_req_body(cls, *args, pkg=pkg, json_file_name="", empty=False, **kwargs):

        j = cls.get_req_json(package=pkg, file_name=json_file_name)
        # print(f"pkg == {pkg}")
        # print(f"json str === > {j}")
        j_dict = ast.literal_eval(j)
        req_dict = REQRender.self_render(j_dict, *args, empty=empty, **kwargs)
        return req_dict


if __name__ == '__main__':
    type_ = 0
    b = "thos is a collection"
    c = "this is a create collection desc"
    # res = GetReqJson.assemble_str_req_body(a, file_name="create_collection", b=b)
    portraitUrl = "aaa"
    res2 = GetReqJson.assemble_dict_req_body(json_file_name="collection_owner", userName="type_",  userNick=b, uid=c, portraitUrl=portraitUrl)
    print(res2)

