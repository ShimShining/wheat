# -*- coding: utf-8 -*-
"""
@Author: shining
@File: jira.py
@Date: 2021/11/30 11:17 下午
@Version: python 3.10
@Describle: jira 实例返回
"""
import datetime
import re
import time
from jira import JIRA
from jira_lark_bot.config import *


class JiraOperation:

    def __init__(self, server, username, token):

        self.jira = JIRA(server=server, basic_auth=(username, token))

    def get_project(self):

        return self.jira.projects()

    def get_project_key(self, project_name):

        projs = self.get_project()
        for proj in projs:
            if proj.name == project_name:
                return proj.key
        return None

    def get_project_name(self, key):

        projs = self.get_project()
        for proj in projs:
            if proj.key == key:
                return proj.name
        return None

    def get_boards(self):

        return self.jira.boards()

    def get_board_id_by_name(self, board_name):
        """
        根据看板名字获取看板id
        :param board_name: 建立看板名称尽量保持与项目名称一致
        :return:
        """
        boards = self.get_boards()
        if boards:
            for board in boards:
                if board.name == board_name:
                    return board.id
        return None

    def get_sprints_by_name(self, project_name):

        board_id = self.get_board_id_by_name(project_name)
        if board_id:
            return self.jira.sprints(board_id, state="active")
        return []

    def get_current_sprint(self, project_name):

        sprint_name = ''
        sprints = self.get_sprints_by_name(project_name)
        if sprints:
            for s in sprints:
                if s.state == "active":
                    sprint_name = s.name
        return sprint_name

    def get_active_sprints(self, proj):
        s = []
        sprints = self.get_sprints_by_name(proj)
        if sprints:
            for sprint in sprints:
                # print(f"sprint.name={sprint.name}, sprint.state={sprint.state}")
                if sprint.state == "active":
                    s.append([sprint.id, sprint.name])
        # print(s)
        return s

    def get_active_sprints_versions(self, proj):
        proj_name = self.get_project_name(proj)
        sps = self.get_active_sprints(proj_name)
        versions = []
        sprints = []
        pat = r"\d+\.\d+\.\d+"
        for s in sps:
            v = re.findall(pat, s[1])
            if v:
                sprints.append(s)
                versions.append(v[0])
        return sprints, versions

    def get_app_version(self, proj):
        """
        根据jira的迭代版本来确定当前prod和alpha的版本号
        返回1.14.0或1.15.0版本号
        :param proj:
        :return: 返回1.14.0或1.15.0版本号 prod，alpha
        """
        sps, _ = self.get_active_sprints_versions(proj)  # sps = [[93, 'BP-US-1.36.0'], [94, 'BP-US-1.37.0']]
        if not sps:
            return None
        if sps and len(sps) < 2:
            alpha = sps[0][1].split('-')[2]
        # elif int(sps[0][0]) < int(sps[1][0]):
        #     alpha = sps[0][1].split('-')[2]
        # else:
        #     alpha = sps[1][1].split('-')[2]
        else:
            alpha = self.get_alpha_version(sps)
        # todo 最新prod version = alpha version中间版本减 1 暂时不兼容跨大版本 例如1.99.0 到2.0.0
        if ".1" in alpha:
            prod = alpha[:-2] + ".0"
        else:
            prod = alpha.replace(alpha.split(".")[1], str(int(alpha.split(".")[1]) - 1))
            prod = prod[:-2] + ".1"
        return prod, alpha

    def get_alpha_version(self, sprints):
        """
        从多个sprint中返回alpha 的version,通过sprint的id判断
        :param sprints: [93, 'BP-US-1.36.0'], [94, 'BP-US-1.37.0']
        :return: 1.36.0 or None
        """
        if not sprints:
            return None
        s = sprints[:]
        # sorted_s = sorted(s, key=lambda i: i[0])  # 通过sprint ID进行排序，不清楚风险，暂时不用
        # 通过版本号判断 比如1.36.0，1.37.0 比较的key值为1+36 和 1+37 进行排序
        sorted_s = sorted(s, key=lambda i: int(i[1].split("-")[2].split('.')[0]) + int(i[1].split("-")[2].split('.')[1]))
        alpha_sprint = sorted_s[0]
        alpha_version = alpha_sprint[1].split("-")[2]
        return alpha_version

    def search_issues_by_project_key(self, project_key):

        jql = f'project = "{project_key}"'
        try:
            issues = self.jira.search_issues(jql, maxResults=200)
            return issues
        except Exception as e:
            print(e)

    def search_issues(self, jql, max_results=0, fields="summary,customfield_10044,customfield_10048,"
                                                       "customfield_10043,assignee,status,customfield_10044,"
                                                       "created,updated,components"):
        """
        根据JQL搜索问题
        @:param jql:JQL,str
        customfield_10043: 打开
        customfield_10044: Unity 3D issue.fields.customfield_10044.value:{'Backend', 'iOS', 'Unity 3D', 'Android'}
        customfield_10048: PR环境
        summary: 适配有问题 到刘海去了 集体偏左
        status: 待办
        project: BC
        @:param max_results: max results,int,default 100
        """
        try:
            issues = self.jira.search_issues(jql, fields=fields, maxResults=max_results)
            # print(f"获取的issue总数={len(issues)}")
            # 默认返回指定的字段，且最大结果行为5000
            return issues
        except Exception as e:
            print(e)

    def get_to_do_issues(self, project_key):

        jql = f'project = {project_key} AND sprint is EMPTY'
        return self.search_issues(jql)

    def get_current_sprint_issues(self, project_name):
        sprint_name = self.get_current_sprint(project_name)
        project_key = self.get_project_key(project_name)
        if sprint_name and project_key:
            jql = f"project = {project_key} AND sprint in openSprints('{project_name}')"
            return self.search_issues(jql)
        return None

    def get_sprint_issues(self, project_key, sprint_id):
        """
        获取指定sprint id的问题集合
        :param project_key:
        :param sprint_id:
        :return:
        """
        if project_key and sprint_id:
            jql = f"project = {project_key} AND Sprint = {sprint_id} ORDER BY created DESC"
            return self.search_issues(jql)
        return []

    def analyse_result(self, issues):

        summarys = {}
        components = {}
        custom_fields = {}
        reason_bugs = {}
        for item in issues:
            summary = str(item.fields.summary)
            if not item.fields.components:
                com = None
            else:
                com = str(item.fields.components[0])  # 模块 返回的是一个jira的components对象
            reason = str(item.fields.customfield_10903)  # 归因分析
            key = str(item.key)  # 项目key值
            label = str(item.fields.labels[0])
            summarys.setdefault(key, summary)  # {项目key：概要}
            components.setdefault(com, 0)  # {模块： 出现次数}
            if com in components.keys():
                components[com] += 1
            custom_fields.setdefault(reason, 0)  # {bug原因： 出现次数}
            if reason in custom_fields.keys():
                custom_fields[reason] += 1

            reason_bugs.setdefault((key + summary), reason)  # {proj_key jira概要： jira归因分析}
            labels = label
        return summarys, components, custom_fields, reason_bugs, labels

    def get_total_issues_info(self, issues):
        """
        issue.fields.status.name:{'正在进行', '已完成', 'In Review', '待办'}
        返回当前版本的缺陷总体情况
        版本缺陷总数：num
        代办缺陷数量：num
        处理中缺陷： num
        REview缺陷：num
        已关闭缺陷： num
        :param issues:
        :return:
        """
        cur_total, todo_num, progress_num, review_num, closed_num = 0, 0, 0, 0, 0
        # status = set()
        if issues:
            cur_total = len(issues)
            for issue in issues:
                # status.add(issue.fields.status.name)
                if issue.fields.status.name == "待办":
                    todo_num += 1
                if issue.fields.status.name in ("正在进行", "处理中"):
                    progress_num += 1
                if issue.fields.status.name == "In Review":
                    review_num += 1
                if issue.fields.status.name == "已完成":
                    closed_num += 1
        # print(status)
        return {
            "cur_total": cur_total,
            "todo_num": todo_num,
            "progress_num": progress_num,
            "review_num": review_num,
            "closed_num": closed_num
        }

    def get_today_issues_info(self, issues):
        """
        今日新增缺陷：num
        今日处理缺陷：num
        今日修复缺陷：num
        今日关闭缺陷：num
        :param issues:
        :return:
        """
        today_issues = {
            "today_create": 0,
            "today_progress": 0,
            "today_fix": 0,
            "today_closed": 0
        }
        for issue in issues:
            if self.is_today(issue.fields.created):
                today_issues["today_create"] += 1
            if self.is_today(issue.fields.updated) and issue.fields.status.name in ("正在进行", "处理中"):
                today_issues["today_progress"] += 1
            if self.is_today(issue.fields.updated) and issue.fields.status.name == "In Review":
                today_issues["today_fix"] += 1
            if self.is_today(issue.fields.updated) and issue.fields.status.name == "已完成":
                today_issues["today_closed"] += 1
        return today_issues

    def is_yesterday(self, days):

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        return str(yesterday) in days

    def is_today(self, utc_time_str):

        today = time.strftime("%Y-%m-%d")
        return today in utc_time_str or (self.is_yesterday(utc_time_str) and
                                         int(utc_time_str[11:13]) > 18)

    def get_end_issues_info(self, issues):
        """
        安卓端缺陷：代办：num，处理中：num，review：num，已关闭：num，今日新增：num，今日关闭：num
        iOS端缺陷：代办：num，处理中：num，review：num，已关闭：num，今日新增：num，今日关闭：num
        U3D端缺陷：代办：num，处理中：num，review：num，已关闭：num，今日新增：num，今日关闭：num
        Backend缺陷：代办：num，处理中：num，review：num，已关闭：num，今日新增：num，今日关闭：num
        未分配端：代办：num，处理中：num，review：num，已关闭：num，今日新增：num，今日关闭：num
        :param issues:
        :return:
        """
        end_info = {'Backend': 'backend', 'iOS': 'ios', 'Unity 3D': 'u3d', 'Android': 'android',
                    '其他': 'oth', 'engine': 'engine', None: 'default'}
        end_issues = {
            "android": {
                "total": 0,
                "todo": 0,
                "progress": 0,
                "review": 0,
                "closed": 0,
                "today_create": 0,
                "today_closed": 0
            },
            "ios": {
                "total": 0,
                "todo": 0,
                "progress": 0,
                "review": 0,
                "closed": 0,
                "today_create": 0,
                "today_closed": 0
            },
            "u3d": {
                "total": 0,
                "todo": 0,
                "progress": 0,
                "review": 0,
                "closed": 0,
                "today_create": 0,
                "today_closed": 0
            },
            "backend": {
                "total": 0,
                "todo": 0,
                "progress": 0,
                "review": 0,
                "closed": 0,
                "today_create": 0,
                "today_closed": 0
            },
            "engine": {
                "total": 0,
                "todo": 0,
                "progress": 0,
                "review": 0,
                "closed": 0,
                "today_create": 0,
                "today_closed": 0
            },
            "oth": {
                "total": 0,
                "todo": 0,
                "progress": 0,
                "review": 0,
                "closed": 0,
                "today_create": 0,
                "today_closed": 0
            },
            "default": {
                "total": 0,
                "todo": 0,
                "progress": 0,
                "review": 0,
                "closed": 0,
                "today_create": 0,
                "today_closed": 0
            },
        }
        for issue in issues:
            # if issue.fields.customfield_10044.value == "Android":
            end_issues[end_info[issue.fields.customfield_10044.value]]["total"] += 1
            if issue.fields.status.name == "待办":
                end_issues[end_info[issue.fields.customfield_10044.value]]["todo"] += 1
            if issue.fields.status.name in ("正在进行", "处理中"):
                end_issues[end_info[issue.fields.customfield_10044.value]]["progress"] += 1
            if issue.fields.status.name == "In Review":
                end_issues[end_info[issue.fields.customfield_10044.value]]["review"] += 1
            if issue.fields.status.name == "已完成":
                end_issues[end_info[issue.fields.customfield_10044.value]]["closed"] += 1
                if self.is_today(issue.fields.updated):
                    end_issues[end_info[issue.fields.customfield_10044.value]]["today_closed"] += 1
            if self.is_today(issue.fields.created):
                end_issues[end_info[issue.fields.customfield_10044.value]]["today_create"] += 1
        return end_issues

    def handle_current_sprint_info(self, project_key="BC", sprint_id=None, sprint_name=None):

        current_sprint = {}
        todo = {}
        proj_name = self.get_project_name(project_key)
        if project_key == "BC":
            current_sprint.setdefault("board_url", Config.CN_BOARD_URL)
        else:
            current_sprint.setdefault("board_url", Config.US_BOARD_URL)
            current_sprint.setdefault("statistics_analysis_board", Config.US_STATISTICAL_ANALYSIS_URL)
        # current_sprint_name = self.get_current_sprint(proj_name)
        # if current_sprint_name:
        #     current_sprint_issues = self.get_current_sprint_issues(proj_name)
        #     for s in current_sprint_issues:
        #         print(dir(s.fields))
        #         print(dir(s))
        #         break
        current_sprint_issues = self.get_sprint_issues(project_key, sprint_id)
        if current_sprint_issues:
            total_issues_info = self.get_total_issues_info(current_sprint_issues)
            today_issues_info = self.get_today_issues_info(current_sprint_issues)
            end_issues_info = self.get_end_issues_info(current_sprint_issues)
            current_sprint.setdefault("project_name", proj_name)
            current_sprint.setdefault("sprint_name", sprint_name)
            current_sprint.setdefault("total_issues_info", total_issues_info)
            current_sprint.setdefault("today_issues_info", today_issues_info)
            current_sprint.setdefault("end_issues_info", end_issues_info)
            current_sprint.setdefault('issues', current_sprint_issues)
        todo_list = self.get_to_do_issues(project_key)
        todo_num = len(todo_list)
        todo.setdefault("todo_issues", todo_list)
        todo.setdefault("todo_num", todo_num)
        return current_sprint, todo

    def handle_active_issues(self, project_key="BD"):

        res = []
        proj_name = self.get_project_name(project_key)
        sprints = self.get_active_sprints(proj_name)
        # print(f"Line 431 sprints={sprints}")
        if len(sprints) == 2:
            if int(sprints[0][0]) < int(sprints[1][0]):
                sprints[0][1] = "Alpha " + sprints[0][1]
                sprints[1][1] = "Master " + sprints[1][1]
            else:
                sprints[1][1] = "Alpha " + sprints[1][1]
                sprints[0][1] = "Master " + sprints[0][1]
        if len(sprints) == 1:
            sprints[0][1] = "Alpha " + sprints[0][1]
        # print(sprints)
        for s in sprints:
            id_, name = s
            res.append((self.handle_current_sprint_info(project_key, id_, name)))
        # print(res)
        return res


if __name__ == "__main__":
    jira = JiraOperation(server=Config.JIRA_SERVER, username=Config.USER_NAME, token=Config.TOKEN)
    # issubs = jira.search_issues_by_project_key("BD")
    # print(issubs,"\n",len(issubs))
    # proj_name=jira.get_project_name('BD')
    # res=jira.get_active_sprints(proj_name)
    # print(res)
    pm = jira.get_project_name("BD")
    sps = jira.get_active_sprints(pm)
    print(sps)
    versions = jira.get_app_version("BD")
    print(f"versions={versions}")
    # sprint, versions = jira.get_active_sprints_versions("BD")
    # print(sprint)
    # print(versions)
    # sps = [[99, 'BP-US-1.47.1'], [93, 'BP-US-1.48.0'], [94, 'BP-US-1.49.0'], [95, 'BP-US-1.50.0']]
    # alpha_version = jira.get_alpha_version(sps)
    # print(alpha_version)
