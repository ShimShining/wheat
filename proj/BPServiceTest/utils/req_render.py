# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: req_handler.py
@Date: 2022/9/6 9:18 下午
@Version: python 3.9
@Describe:
"""
import json
import re
import string

import jinja2


class REQRender:

    @staticmethod
    def string_template(old, replace):
        """
        Template('姓名: $name, 年龄: $age').safe_substitute(name='Kevin', age=21)
        :param old:
        :param replace:
        :return:
        """
        res = jinja2.Template(old).render(**replace)
        return res

    @staticmethod
    def jinja_template(source_str, info: dict):
        """
        Template('姓名: {{ name }}, 年龄: {{age}}').render(name='Kevin', age=21)
        :param source_str:
        :param info:
        :return:
        """
        target = string.Template(source_str).safe_substitute(**info)
        return target

    @staticmethod
    def render(origin, *args, delimiter="$", **kwargs):
        """
        s = ['性别: $2  年龄: $3\n$a', '$1', {"say": "$a"}]
        print(render(s, 'kevin', 'male', '20', a="hello, world!"))
        支持$1替换第1个参数, 及$a替换参数a
        支持字典/列表/元祖, 以及嵌套字典/列表中变量的替换
        支持指定定界符, 默认为$
        支持多行文本替换
        不完全替换时, 保留原值, 不会报错
        缺点：只能替换字符串
        :return:
        """

        patten = r'\{}(?P<var>[\w|_]+)'.format(delimiter)

        def repl_func(matched):  # 自定义re.sub使用的替换方法
            var = matched.group('var')
            if var.isdigit():  # 如果是数字, 则从args中替换
                index = int(var) - 1
                if index < len(args):
                    return args[index]
                else:
                    return "{}{}".format(delimiter, var)  # 无替换参数则返回原值
            else:
                return kwargs.get(var, None) or "{}{}".format(delimiter, var)  # 返回kwargs参数中值 or 原值

        if isinstance(origin, str):
            return re.sub(patten, repl_func, origin, re.M)
        elif isinstance(origin, (dict, list)):  # 使用json.dumps转为字符串, 替换,然后重新转为dict/list
            return json.loads(re.sub(patten, repl_func, json.dumps(origin), re.M))
        else:
            if isinstance(origin, tuple):
                return tuple(json.loads(re.sub(patten, repl_func, json.dumps(origin), re.M)))

    @staticmethod
    def self_render(source, *args, empty=False, **kwargs):
        """
        遍历字典来实现
        0. 传入的是纯字符串，则通过字符串替换的render实现变量替换
        1. 有位置参数替换对应位置
        2. 有名字的参数替换对应名字
        3. 支持替换变量的类型任意（数字，列表，字典）
        4. 没有传入该替换值，则返回时弹出该参数key
        5. 整个数据结构为空，则返回时弹出该key ToDo --> done
        6. 列表中未匹配到对应的值，则remove相关的占位变量[$1,$name]
        """

        if isinstance(source, str):
            return REQRender.render(source, *args, **kwargs)

        def match_index(v):
            if isinstance(v, str):
                val = re.findall("\$(.*)", v)
                if val:
                    if val[0].isdigit():
                        return int(val[0])
                    return val[0]
            return v

        def replace_dict(origin_dict):
            if not isinstance(origin_dict, dict):
                raise ValueError(
                    f"replace_dict method only support dict data struct, but get a invalid param = {origin_dict}")
            del_keys = []  # 字典中未传入的替换变量值
            for k, v in origin_dict.items():
                if isinstance(v, str) and "$" in v:
                    tmp = match_index(v)
                    if isinstance(tmp, int):
                        if tmp > len(args):
                            del_keys.append(k)
                        else:
                            origin_dict[k] = args[tmp - 1]
                    elif isinstance(tmp, str):
                        if kwargs.get(tmp, None) is None:
                            # origin_dict.pop(k, None)
                            del_keys.append(k)
                        else:
                            origin_dict[k] = kwargs.get(tmp, None)
                elif isinstance(v, str) and v in ['True', 'true']:
                    origin_dict[k] = True
                elif isinstance(v, str) and v in ['false', 'False']:
                    origin_dict[k] = False
                elif isinstance(v, dict):
                    replace_dict(v)
                elif isinstance(v, list):
                    invalid_items = []  # 使用中间列表invalid_items存储没有传的替换值
                    for i, item in enumerate(v):
                        if isinstance(item, dict):
                            replace_dict(item)
                        elif isinstance(item, str) and "$" in item:
                            tmp = match_index(item)
                            if isinstance(tmp, int):
                                if tmp > len(args):
                                    # v.remove(item)
                                    # v.pop(i)
                                    invalid_items.append(item)
                                else:
                                    v[i] = args[tmp - 1]
                            elif isinstance(tmp, str):
                                if kwargs.get(tmp, None):
                                    v[i] = kwargs.get(tmp, None)
                                else:
                                    invalid_items.append(item)
                    if invalid_items:
                        for inval in invalid_items:
                            v.remove(inval)
            for key in del_keys:
                del origin_dict[key]
            return origin_dict

        res = replace_dict(source)
        if empty:
            return REQRender.empty_data_handler(res)
        return res
        # return REQRender.empty_data_handler(res)

    @staticmethod
    def empty_data_handler(data_dict: dict):
        empty_keys = []
        for k, v in data_dict.items():
            if not v:
                empty_keys.append(k)
            elif v and isinstance(v, dict):
                REQRender.empty_data_handler(v)
            elif v and isinstance(v, list):
                for i, item in enumerate(v):
                    if not item:
                        v.remove(item)
                    elif item and isinstance(item, dict):
                        REQRender.empty_data_handler(item)
        for empty_key in empty_keys:
            del data_dict[empty_key]

        return data_dict


if __name__ == '__main__':
    req_handler = REQRender()
    s = ['性别: $2  年龄: $3\n$a', '$1', {"say": "$a"}]
    p4 = {
        "a": "aaaa",
        "b": 2000.01,
        "c": {
            "c": 1000
        }
    }
    # req = req_handler.render(s, 'aaa', 'male', "20", a="hahah")
    d = {'性别': "$2", "年龄": "$3", "a": '$a', "index1": '$1', "rec_dict": ["$4", {"say": "$a"}]}
    req = req_handler.self_render(d, 'aaa', 'male', 20, p4, a="hahah")
    print(req)
