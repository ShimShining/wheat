#!/usr/bin/env python3.8
import csv
import json
import logging
import re

import requests


class Obj(dict):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [Obj(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, Obj(b) if isinstance(b, dict) else b)


def dict_2_obj(d: dict):
    return Obj(d)


def message_handler(text_content, msg_id):
    """
    处理群聊接受到的消息
    :param content:
    :return:
    """
    hanlder_msg_ids = read_csv_data("./msg_id.csv")
    # print(f"hanlder_msg_ids={hanlder_msg_ids}")
    if [msg_id] in hanlder_msg_ids:
        return None
    content = eval("'{}'".format(text_content))
    logging.info(f"content:{content}")
    msg = json.loads(content)
    text = msg['text']
    if "@_user_1 " in text:
        text = text.replace("@_user_1 ", "")
    version = ''
    mark = ''
    mark_list = re.findall(r"(?<=mark=)[a-zA-Z | s]+", text)
    if mark_list:
        mark = mark_list[0]
    version_list = re.findall(r'\d+\.\d+\.\d+', text)
    if version_list:
        version = version_list[0]
    write_to_csv([msg_id], './msg_id.csv')
    if "运行" in text or "run" in text:
        if "接口" in text or "API" in text or 'api' in text or 'Api' in text:
            host = host_handler(text)
            if version:
                if mark:
                    return api_jenkins_trigger_with_params(host=host, version=version, mark=mark)
                else:
                    return api_jenkins_trigger_with_params(host=host, version=version)
            else:
                if 'alpha' in text:
                    return alpha_api_jenkins_trigger()
                if 'prod' in text:
                    return prod_api_jenkins_trigger()
                return master_api_jenkins_trigger()
    if "/help" in text:
        return "输入指令动作包含：\n运行或者run之一；\n 其他内容包含关键词: 接口或者API或者api或者Api之一；\n " \
               "包含: master，alpha，prod会运行对应环境自动化，默认master \n 包含: 版本号，譬如1.28.0\n会运行对应版本的api自动化" \
               "\n添加运行用例标志：mark,例如mark=login social,会运行login和social模块用例" \
               "\n例如：运行master环境接口自动化，会触发运行master环境的接口自动化测试任务"

    return f"👉 小Q默认reply：{text}" + " ==>如需获取相关指令，请输入：/help"


def host_handler(context):
    host = "master"
    if 'alpha' in context:
        host = 'alpha'
    elif 'prod' in context:
        host = 'prod'
    return host


def master_api_jenkins_trigger():
    """
    :return:
    """
    jenkins_trigger_url = ""
    res = requests.get(jenkins_trigger_url)
    reply = "👉 小Q已触发Jenkins运行master环境接口自动化测试任务...请耐心等待测试结果通知"
    reply = check_jenkins_rsp(res, reply)
    return reply


def alpha_api_jenkins_trigger():
    jenkins_trigger_url = ""
    res = requests.get(jenkins_trigger_url)
    reply = "👉 小Q已触发Jenkins运行alpha环境接口自动化测试任务...请耐心等待测试结果通知"
    reply = check_jenkins_rsp(res, reply)
    return reply


def prod_api_jenkins_trigger():
    jenkins_trigger_url = ""
    res = requests.get(jenkins_trigger_url)
    reply = "👉 小Q已触发Jenkins运行prod环境接口自动化测试任务...请耐心等待测试结果通知"
    reply = check_jenkins_rsp(res, reply)
    return reply


def api_jenkins_trigger_with_params(host=None, version=None, mark=None):
    jenkins_trigger_url = ""
    reply = f"👉 小Q已触发Jenkins运行{host}环境版本{version} 接口自动化测试任务...请耐心等待测试结果通知"
    if mark:
        mark = mark.strip()
        mark = " or ".join(mark.split(" "))
        jenkins_trigger_url = jenkins_trigger_url + f"&mark={mark}"
        reply = f"👉 小Q已触发Jenkins运行{host}环境版本{version} Mark={mark}的接口自动化测试任务...请耐心等待测试结果通知"
    res = requests.get(jenkins_trigger_url)
    reply = check_jenkins_rsp(res, reply)
    return reply


def check_jenkins_rsp(res, reply):
    code = res.status_code
    rsp = res.json().get("jobs", None)
    if code != 200 or not rsp:
        reply = "Jenkins 触发自动化任务失败...请重试或前往Jenkins查看！！！"
    return reply


def write_to_csv(data, file_path):
    write_rows = None
    with open(file_path, 'a+') as f:
        f.seek(0)
        file_lines = len(f.readlines())
        # print(file_lines)
        f.seek(0)
        reader = csv.reader(f)
        lines = []
        if file_lines < 10:
            writer = csv.writer(f)
            writer.writerow(data)
        else:
            for line in reader:
                print(line)
                lines.append(line)
            lines.append(data)
            write_rows = lines[-10:]
    if lines and write_rows:
        print("重新写入")
        print(f"lines={lines}")
        print(f"写入的数据={write_rows}")
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(write_rows)


def read_csv_data(file_path, length=10):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = list(csv.reader(f))

    return data[-length:]

