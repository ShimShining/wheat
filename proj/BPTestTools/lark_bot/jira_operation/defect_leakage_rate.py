# -*- coding: utf-8 -*-
"""
@Author: shining
@File: defect_leakage_rate.py
@Date: 2022/6/26 11:17 下午
@Version: python 3.8
@Describle: 漏测率统计
"""
import math

from utils.read_yaml import *
from jira_lark_bot.jira_operation.jira_operation import JiraOperation
from jira_lark_bot.config import *
from jira_lark_bot.lark_bot.leakage_lark_bot import *


class DefectLeakageRate(JiraOperation):
    def __init__(self, server, username, token):
        super(DefectLeakageRate, self).__init__(server, username, token)
        self._project_key = 'BD'
        self._version = 'prod'

    def set_project_key(self, project_key):
        self._project_key = project_key

    def set_version(self, version):
        self._version = version

    def select_version(self, version_id=None):
        if version_id == None:
            sprints = self.get_app_version(self._project_key)
            board_id = self._version = sprints[0] if self._version == 'prod' else self._version
        else:
            board_id = version_id
        return board_id

    def search_issues(self, jql, max_results=0, fields="summary,customfield_10044,customfield_10048,"
                                                       "customfield_10043,assignee,status,customfield_10044,"
                                                       "created,updated,components,customfield_10087,"
                                                       "customfield_10088,customfield_10089"):
        '''
        添加字段:
        customfield_10087:是否漏测
        customfield_10088:漏测主要负责人
        customfield_10089:漏测次要负责人
        '''
        # TODO Tips==> 新增加的自定义字段，需要在这添加fields，不然可能查询时不返回该字段
        return super().search_issues(jql, max_results, fields)

    def get_board_issues(self, version_id=None):
        board_id = self.select_version(version_id)
        issues = self.get_sprint_issues(project_key=self._project_key, sprint_id=board_id)
        return issues

    def get_active_board_issues(self):  # 获取所有活跃面板BUG
        proj_name = self.get_project_name(self._project_key)
        active_sprints = self.get_active_sprints(proj_name)
        issues = []
        for sprint in active_sprints:
            if "BPX——Web3" not in sprint:
                issues += self.get_board_issues(version_id=sprint[0])
        return issues

    def get_owner_active_issues(self, owner):
        proj_name = self.get_project_name(self._project_key)
        active_sprints = self.get_active_sprints(proj_name)
        issues = []
        for sprint in active_sprints:
            if "BPX——Web3" not in sprint:
                issues += self.get_owner_board_issues(owner=owner, version_id=sprint[0])
        return issues

    def get_owner_board_issues(self, owner, version_id=None):
        board_id = self.select_version(version_id)
        jql = f"project = {self._project_key} AND Sprint = {board_id} AND reporter = '{owner}' ORDER BY created DESC"
        return self.search_issues(jql)

    def is_leakage(self, issue):
        # todo 是否漏测 issue.findes.customfield_10087
        # issue.fields.customfield_10087 这货取值返回的是个对象，不是字符串，要转换才能判值。
        if str(issue.fields.customfield_10087) in ['否', 'None']:
            return False
        return True

    # def get_leakages(self, issues: list):
    #     leakages_issues = []
    #     for issue in issues:
    #         if self.is_leakage(issue):
    #             leakages_issues.append(issue)
    #     return leakages_issues

    def get_leakages(self, version_id=None):
        board_id = self.select_version(version_id)
        jql = f"project = {self._project_key} AND '发现版本[Labels]' = {board_id} AND '是否漏测[Radio Buttons]' = '是' ORDER BY created DESC"
        return self.search_issues(jql)

    def get_history_leakages(self):
        """

        :return:
        """
        jql = f"project = {self._project_key} AND '是否漏测[Radio Buttons]' = '是' ORDER BY created DESC"
        return self.search_issues(jql)

    def get_owner_leakages(self, owner, version_id=None):
        board_id = self.select_version(version_id)
        jql = f"reporter = '{owner}' AND project = {self._project_key} AND '发现版本[Labels]' = {board_id} AND '是否漏测[Radio Buttons]' = '是' ORDER BY created DESC"
        return self.search_issues(jql)

    def get_issue_info(self, issue_key: str = 'BD-3812'):
        issue = self.jira.issue(issue_key)
        return '\n'.join(['{0}: {1}'.format(item[0], item[1]) for item in issue.fields.__dict__.items()])

    def get_team_defects(self):
        issues = self.get_board_issues()
        return len(issues)

    def get_owner_defects(self, owner):
        issues = self.get_owner_board_issues(owner=owner)
        return len(issues)

    def classify_issues(self, issues: list):
        cla_issues = {'待办': 0,
                      '处理中': 0,
                      'In Review': 0,
                      '已完成': 0
                      }
        if not issues:
            return cla_issues
        for issue in issues:
            cla_issues[issue.fields.status.name] += 1
        return cla_issues

    def count_leakage_rate(self, defects: int, leakages: int):
        if defects == 0 or (defects - leakages) <= 0:
            return round(float(leakages), 2)
        rate = leakages / defects
        return round(rate, 4)

    def count_team_leakage_rate(self, history_file=None):
        ds = self.get_board_issues()
        ls = self.get_leakages()
        cla_issues = self.classify_issues(ds)
        active_issues = self.get_active_board_issues()  # 活跃面板BUG
        act_cla_issues = self.classify_issues(active_issues)
        rate = self.count_leakage_rate(defects=len(ds), leakages=len(ls))
        history_leakages = len(self.get_history_leakages())
        history_total_issues = self.get_all_issues(history_file=history_file)
        history_leakages_rate = self.count_leakage_rate(history_total_issues, history_leakages)
        res = {
            'version': self._version,
            'defects': len(ds),
            'leakages': len(ls),
            'rate': rate,
            'status_issues': cla_issues,
            'active_issues': act_cla_issues,
            'leakages_issues': ls,
            "history_leakages": history_leakages,
            "history_total_issues": history_total_issues,
            "history_leakages_rate": history_leakages_rate
        }
        return res

    def count_owner_leakage_rate(self, owners: list):
        res = {}
        for owner in owners:
            # ds 是上一个版本的bug list [<JIRA Issue: key='BD-12484', id='26837'>, <JIRA Issue: key='BD-12469', id='26822'>]
            ds = self.get_owner_board_issues(owner=owner)
            recent_prod_demands_issues_distribute = self.handle_qa_demand_issues_dstribute(ds)
            ls = self.get_owner_leakages(owner=owner)
            active_issues = self.get_owner_active_issues(owner)  # 活跃面板BUG
            act_cla_issues = self.classify_issues(active_issues)
            cla_issues = self.classify_issues(ds)
            owner_rate = self.count_leakage_rate(defects=len(ds), leakages=len(ls))
            res[owner] = {
                'defects': len(ds),
                'leakages': len(ls),
                'owner_rate': owner_rate,
                'status_issues': cla_issues,
                'active_issues': act_cla_issues,
                'leakages_issues': ls,
                'recent_v_demand_issues_distribute': recent_prod_demands_issues_distribute
            }
        return res

    @staticmethod
    def get_qa_recent_prod_demands_issues(issues: list):
        from lark_bot.jira_operation.get_jira_pm_issues import GetJiraPMIssues
        demands_issues = GetJiraPMIssues.get_pm_demand_issues(issues)
        return demands_issues

    def handle_qa_demand_issues_dstribute(self, issues):
        res = dict()
        demand_issues = self.get_qa_recent_prod_demands_issues(issues)
        for k, v in demand_issues.items():
            res[k] = len(v)

        return res

    def get_defect_leakage_rate(self, owners, history_file=None):
        team_rate = self.count_team_leakage_rate(history_file=history_file)
        owner_rate = self.count_owner_leakage_rate(owners)
        leakage_rate = {
            'project_name': self.get_project_name(self._project_key),
            'version': self._version,
            'team_rate': team_rate,
            'owner_rate': owner_rate,
        }
        return leakage_rate

    def get_all_issues(self, project_key=None, history_file=None):
        """
        :param project_key:
        :return:
        """
        if history_file:
            d = ReadYAML.read(history_file)
            if not d:
                if not project_key:
                    jql = f"project = {self._project_key} ORDER BY created DESC"
                else:
                    jql = f"project = {project_key} ORDER BY created DESC"
                total_issues = len(self.search_issues(jql))
                time_now = str(int(time.time()))
                tmp = {time_now: total_issues}
                # print(f"无文件tmp={tmp}")
                ReadYAML.write_yaml(history_file, tmp)
            else:
                for k, v in d.items():
                    k = k
                    v = v
                diff_minute = math.ceil((int(time.time()) - int(k)) / 60)
                if not project_key:
                    # created >= -100m AND project = BD ORDER BY created DESC
                    jql = f"created >= -{diff_minute}m AND project = {self._project_key} ORDER BY created DESC"
                else:
                    jql = f"created >= -{diff_minute}m AND project = {project_key} ORDER BY created DESC"
                interval_issues = len(self.search_issues(jql))
                total_issues = v + interval_issues
                time_now = str(int(time.time()))
                tmp = {time_now: total_issues}
                # print(f"已有文件tmp={tmp}")
                ReadYAML.write_yaml(history_file, tmp)
            # print(f"total_issues === {total_issues}")
            return total_issues

    def get_qa_roles(self):
        resource = self.jira.project_role("BD", "10022")
        roles = resource.raw['actors']
        owner_name = []
        for role in roles:
            if role["displayName"] not in ["Risa Feng", "赵威豪 Stanley"]:
                owner_name.append(role["displayName"])
        return owner_name


if __name__ == "__main__":
    from pprint import pprint
    import time

    start_time = time.time()
    from lark_bot.lark_bot.leakage_lark_bot import *

    jira = DefectLeakageRate(server=Config.JIRA_SERVER, username=Config.USER_NAME, token=Config.TOKEN)

    rate = jira.count_leakage_rate(61, 1)
    # rate = leakage / total
    # pprint(leakage)
    print(rate)
    # print(r.text)

    jira.set_version('1.35.0')
    role = jira.get_qa_roles()
    print(role)

