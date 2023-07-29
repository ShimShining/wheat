# -*- coding: utf-8 -*-
"""
@Author: shining
@File: proxy.py
@Date: 2022/7/7 10:55 下午
@Version: python 3.9
@Describe: 代理IP获取
"""

import requests
import re
import time
import random
import threading


class Proxy:

    @staticmethod
    def get_cloud_proxy_ips():
        # 爬取网站：云代理
        # http://www.ip3366.net/free/?stype=1&page=1
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400"
        }
        web_site = '云代理'
        url_tmp = 'http://www.ip3366.net/free/?stype=1&page=%d'
        f = open('./ip_list.txt', mode='a', encoding='utf-8')
        for index in range(1, 8):
            try:
                url = url_tmp % index
                print(url)
                response = requests.get(url=url, headers=headers)
                print(response.status_code)
                response.encoding = 'utf-8'
                tr_pattern = r'<tr>(.*?)</tr>'
                trs = re.findall(tr_pattern, response.text, re.S)[1:]
                for tr in trs:
                    td_pattern = r'<td>([\d\.]*)</td>[\s]*' \
                                 '<td>([\d\.]*)</td>[\s]*' \
                                 '<td>.*?</td>[\s]*' \
                                 '<td>([A-Z]*)</td>'  # IP PORT
                    Ip, Port, Type = re.findall(td_pattern, tr, re.S)[0]
                    print(Ip, Port, Type)
                    f.write('%s,%s,%s\n' % (Ip, Port, Type))
            except Exception as e:
                # pass
                with open('./error_log.txt', mode='a', encoding='utf-8') as fp:
                    fp.write('%s\n%s\n%s\n' % (web_site, str(e), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            finally:
                time.sleep(random.randint(1, 3))
        f.close()

    @staticmethod
    def get_quick_proxy_ips():

        # 爬取网站：快代理
        # https://www.kuaidaili.com/free/inha/

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400"
        }
        web_site = '快代理'
        url_tmp = 'https://www.kuaidaili.com/free/inha/%d/'
        f = open('./ip_list.txt', mode='a', encoding='utf-8')
        for index in range(1, 21):
            try:
                url = url_tmp % index
                print(url)
                response = requests.get(url=url, headers=headers)
                print(response.status_code)
                response.encoding = 'utf-8'
                tr_pattern = r'<tr>(.*?)</tr>'
                trs = re.findall(tr_pattern, response.text, re.S)[1:]
                for tr in trs:
                    td_pattern = r'<td data-title=".*?">([\d\.]*)</td>[\s]*<td data-title=".*?">([\d\.]*)</td>[\s]*<td data-title=".*?">([A-Z]*)</td>'  # IP PORT
                    Ip, Port, Type = re.findall(td_pattern, tr, re.S)[0]
                    print(Ip, Port, Type)
                    f.write('%s,%s,%s\n' % (Ip, Port, Type))
            except Exception as e:
                with open('./error_log.txt', mode='a', encoding='utf-8') as fp:
                    fp.write(
                        '%s\n%s\n%s\n' % (web_site, str(e), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            finally:
                time.sleep(random.randint(1, 3))
        f.close()

    @staticmethod
    def verify_proxy(f1, f2):
        fp = f1
        fp2 = f2
        num = 0
        site = '验证代理'
        global num
        while True:
            line = fp.readline().strip('\n')  # 去掉结尾换行符
            if line != '':
                ip, host, protocol = line.split(',')
                # print(ip, host, protocol)
                # 要访问的网站如果是HTTPS，那么代理也要是HTTPS，如果不对应，则不会使用代理，转而使用本地IP
                # 要访问的网站如果是HTTP，那么代理也要是HTTP，如果不对应，则不会使用代理，转而使用本地IP
                url1 = 'http://ip.tool.chinaz.com/'
                url2 = 'https://ip.cn/'
                try:
                    if protocol == 'HTTPS':
                        requests.get(url2, proxies={'https': '%s:%s' % (ip, host)}, timeout=5)
                        print('该 %s ip-> %s:%s 验证通过' % (protocol, ip, host))
                        num += 1
                        fp2.write('%s,%s,%s\n' % (ip, host, protocol))
                    else:
                        requests.get(url1, proxies={'http': '%s:%s' % (ip, host)}, timeout=5)
                        print('该 %s ip-> %s:%s 验证通过' % (protocol, ip, host))
                        num += 1
                        fp2.write('%s,%s,%s\n' % (ip, host, protocol))
                except Exception as e:
                    print('该 %s ip-> %s:%s 验证失败' % (protocol, ip, host))
                    with open('./error_log.txt', mode='a', encoding='utf-8') as fe:
                        fe.write('%s\n%s\n%s\n' % (site, str(e), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            else:
                break
        return num

    @staticmethod
    def visit_site_with_proxy_ip(url):
        with open('./verify_proxies.txt', mode='r', encoding='utf-8') as f:
            proxies = f.readlines()
        print(proxies)  # 一次读取多行，每行作为列表的一项存在，每一项都包括\n在内
        proxies = [proxy.strip('\n').split(",") for proxy in proxies]
        print(proxies)

        ip, host, protocol = random.choice(proxies)  # 在代理池中随机选择一个IP地址
        print(ip, host, protocol.lower())
        response = requests.get(url=url,
                                proxies={'%s' % protocol.lower(): '%s:%s' % (ip, host)})  # 这的协议http必须用小写，如果用大写，则会用本地IP


if __name__ == '__main__':

    fp = open('./ip_list.txt', mode='r', encoding='utf-8')  # 总的iplist
    fp2 = open('./verify_proxies.txt', mode='a', encoding='utf-8')  #
    threads = []
    for i in range(100):
        t = threading.Thread(target=Proxy.verify_proxy)
        t.start()
        threads.append(t)

    # join必须单独写，目的：线程启动
    for t in threads:
        t.join()  # 所有的子线程结束任务，主线程才开始继续执行
    # verify_proxy()
    fp.close()
    fp2.close()
    print('可用ip的数量是%d' % num)