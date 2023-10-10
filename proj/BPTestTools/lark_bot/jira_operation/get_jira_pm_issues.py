# -*- coding: utf-8 -*-
"""
@Author: shining
@File: get_jira_pm_issues.py
@Date: 2022/8/12 9:12 下午
@Version: python 3.9
@Describe:
"""
from jira_lark_bot.jira_operation.defect_leakage_rate import DefectLeakageRate


class GetJiraPMIssues(DefectLeakageRate):

    def __init__(self, server, username, token):
        super(DefectLeakageRate, self).__init__(server, username, token)

    def get_active_sprints_pm_issues(self, pm_owner):

        jql = f'project = BD AND sprint in openSprints() AND "PM-Owner" = "{pm_owner}" ORDER BY created DESC'
        return self.search_issues(jql)

    def statistics_pm_issues(self, pm_owners: list):
        """
        issuse.fields.components[0].name区分是哪个模块
        :param pm_owners:
        :return:
        """

        res = dict()
        _, versions = self.get_active_sprints_versions("BD")
        version_nums = self.handle_versions(versions)
        res['version_nums'] = version_nums
        res['pm_owners'] = dict()
        for pm_owner in pm_owners:
            active_issues = self.get_active_sprints_pm_issues(pm_owner)  # 活跃面板BUG
            active_classify_issues = self.classify_issues(active_issues)  # 不同状态bug分布
            # 不同需求的bug状态分布{'无关联需求': {'待办': 30, '处理中': 1, 'In Review': 4, '已完成': 14}}
            demand_issues_status = self.handle_single_pm_demands_issues(active_issues)
            res['pm_owners'][pm_owner] = {
                'total': len(active_issues),
                'status_issues': active_classify_issues,
                'demand_issues_status': demand_issues_status
            }
        return res

    @staticmethod
    def get_pm_demand_issues(issues: list):

        res = dict()
        for i in issues:
            demands = GetJiraPMIssues.get_demands_name(i.fields.components)  # todo 是否兼容多个components情况
            demand = demands[0] if demands else "未关联需求"
            if not res.get(demand, None):
                res[demand] = [i]
            else:
                res[demand].append(i)

        return res

    def classify_pm_demand_issues(self, demand_issues: dict):
        """
        计算每个PM下的需求，待办，处理中，in review 和完成的bug有多少
        :param demand_issues:
        :return:
        """

        res = dict()

        for k in demand_issues.keys():
            res[k] = self.classify_issues(demand_issues[k])

        return res

    @staticmethod
    def filter_bug_all_done_demand(demand_statics_res: dict):

        # 过滤待办，处理中，in review bug数为0的需求
        if not demand_statics_res:
            return demand_statics_res
        done_demand = []
        for demand_k, demand_v in demand_statics_res.items():
            num = 0
            for sub_k, sub_v in demand_v.items():
                if sub_k == "已完成":
                    continue
                num = num + sub_v
            # 待办 + 处理中 + In Review的bug和为0，不同步该需求
            else:
                if num == 0:
                    done_demand.append(demand_k)
        for k in done_demand:
            demand_statics_res.pop(k, None)

        return demand_statics_res

    @staticmethod
    def get_demands_name(components):
        res = []
        if not components:
            return res
        for c in components:
            res.append(c.name)
        return res

    def handle_single_pm_demands_issues(self, issues: list):

        pm_demand_issues = self.get_pm_demand_issues(issues)
        pm_demand_issues_status = self.classify_pm_demand_issues(pm_demand_issues)
        pm_demand_issues_status_filter = self.filter_bug_all_done_demand(pm_demand_issues_status)
        return pm_demand_issues_status_filter

    def handle_versions(self, versions: list):

        temp = [version[-4:] for version in versions]
        res = []
        for item in temp:
            if '.0' in item:
                item = item[:-2]
                res.append(item)
            else:
                res.append(item)
        v = ",".join(res)
        return v


if __name__ == "__main__":
    from lark_bot.lark_bot.leakage_lark_bot import *

    gp = GetJiraPMIssues(server=Config.JIRA_SERVER, username=Config.USER_NAME, token=Config.TOKEN)
    version = ['1.40.0', '1.41.0', '1.40.1']
    v = gp.handle_versions(version)
    print(v)
