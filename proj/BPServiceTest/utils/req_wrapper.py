# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: req_wrapper.py
@Date: 2022/8/29 3:52 下午
@Version: python 3.9
@Describe: 拼装接口请求参数 req
"""
import inspect
from functools import wraps
from inspect import signature


def req_wrapper(func, *args, **kwargs):
    """
    废弃
    :param func:
    :param args:
    :param kwargs:
    :return:
    """
    data = {}
    @wraps(func)
    def wrapper(*args, **kwargs):

        args = inspect.getcallargs(func, *args, **kwargs)
        members = inspect.getmembers(func)
        print(f"members={members}")
        print(f"args={args}")
        # argspec = inspect.getfullargspec(func)
        # doc_str = func.__doc__
        # for attr in dir(func.__doc__):
        #     print(f"{attr} ==> {getattr(func.__doc__, attr)}")
        # print(f"doc_str=={doc_str}")
        print(f"locals() = {locals()}")
        # return
        for k, v in args.items():
            if k not in ["kwargs", "self"] and v is not None:
                req_key = cast_param_to_req_body_key(k)
                data[req_key] = v
        print(data)
        # print(argspec)
        # sig = signature(func)
        # print(str(sig))
        # print(sig)

        # args = locals()
        # print(args)
        # func_vars = func.__code__.co_varnames
        # print(func_vars)
        # print(dir(func.__code__.co_consts.count))
        # print(func.__code__.co_consts.count)

    return wrapper


def cast_param_to_req_body_key(p: str):
    if "_" not in p:
        return p
    res = []

    for i in range(len(p)):

        if i == 0:
            temp = p[i]
        elif p[i] == "_":
            continue
        elif p[i - 1] == "_" and i < len(p) and p[i].isalpha():
            temp = p[i].upper()
        else:
            temp = p[i]
        res.append(temp)
    return "".join(res)


@req_wrapper
def http_get(provider="1", open_id=None, first_name=None, **kwargs):
    """
    path = "/user/login"
    name = "登录接口"
    """

    # __data = {
    #     "provider": provider,  # snapchat,facebook,apple,google,twitter,tiktok,tourist
    #     "openId": open_id,
    #     "firstName": first_name
    # }


if __name__ == "__main__":
    token = ""
    http_get(token=token)
    user_id = "user_id"
    a = cast_param_to_req_body_key(user_id)
    print(a)
