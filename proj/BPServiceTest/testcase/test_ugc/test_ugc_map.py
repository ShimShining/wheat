# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: test_ugc_map.py
@Date: 2022/4/14 4:47 下午
@Version: python 3.10
@Describe:
ugc模版列表
设置地图/素材/衣服/space
地图/素材/衣服/space草稿列表
地图/素材/衣服/space发布列表
地图/素材/衣服/space详情
测试case
"""
import random

import allure
import pytest

from us_api_test.business.ugc.ugc_map import UGCMap
from us_api_test.config import Config
from proj.BPServiceTest.testcase.service_test import ServiceTest
from utils.time_tools import TimeTools


@allure.feature("草稿箱模块")
class TestUGCMap(ServiceTest):
    uid = Config.case_data('global_user_info.yml').uid
    to_uid = Config.case_data('global_user_info.yml').to_uid

    def setup(self):

        self.um = UGCMap()

    @allure.story('ugc草稿模板获取')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("data_type,title", [
        [0, "获取地图草稿模板成功"], [2, '获取衣服草稿模板成功']
    ])
    def test_get_ugc_templates(self, data_type, title):
        allure.dynamic.title(title)
        version = Config.get_run_env_version()
        r = self.um.get_ugc_templates(self.uid, data_type=data_type, version=version)

        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        self.assert_value_in(r['data']['isEnd'], [0, 1])
        self.assert_length_gt_zero(r['data']['templates'])
        mt = r['data']['templates'][0]
        _id = str(mt.get('id', None)) if mt.get('id', None) else ""
        template_id = str(mt.get("templateId", None)) if mt.get("templateId", None) else ""
        # self.assert_not_empty(str(mt['templateId']))
        self.assert_any_not_empty([_id, template_id])
        self.assert_not_empty(mt['mapCover'])
        self.assert_not_empty(mt['mapCoverFull'])
        self.assert_not_empty(mt['mapName'])
        self.assert_not_empty(mt['mapJson'])
        self.assert_equal(mt['dataType'], data_type)

    @allure.story('新建ugc草稿')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("data_type, operation_type, map_info, template_id, title",
                             Config.case_data_dict("ugc_map_draft.yml", "create_ugc_draft_first"))
    def test_create_ugc_draft_first(self, data_type, operation_type, map_info, template_id, title):
        allure.dynamic.title(title)
        # todo space数据准备 done
        map_name = map_info['mapName']
        if data_type != 3:
            map_name = map_info['mapName'] + TimeTools.get_now_sec_timestamp()
        r = self.um.publish_ugc_draft(self.uid, data_type, operation_type, map_info, map_name=map_name)

        self.assert_api_success_code(r)
        self.assert_not_empty(r['data']['mapId'])
        draft_list = self.um.get_draft_create_list(self.uid, data_type=data_type)
        map_ids = [d['mapId'] for d in draft_list['data']['mapInfos']]
        map_names = [d['mapName'] for d in draft_list['data']['mapInfos']]
        self.assert_value_in(r['data']['mapId'], map_ids)
        self.assert_value_in(map_name, map_names)
        if data_type not in (3, 4):  # ToDo 一个月后 4也走删除逻辑
            del_draft_map_id = r['data']['mapId']
            map_info['mapId'] = del_draft_map_id
            map_info.pop('mapName', None)
            r = self.um.delete_ugc_draft(self.uid, map_info)
            self.assert_api_success_code(r)
            self.assert_equal(r['data']['mapId'], del_draft_map_id)
            draft_list = self.um.get_draft_create_list(self.uid, data_type=data_type)
            map_ids = [d['mapId'] for d in draft_list['data']['mapInfos']]
            self.assert_value_not_in_seq(del_draft_map_id, map_ids)

    @allure.story('新建ugc草稿')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("data_type,operation_type,map_info,template_id,title",
                             Config.case_data_dict("ugc_map_draft.yml", "continue_edit_ugc_draft"))
    def test_continue_edit_ugc_draft(self, data_type, operation_type, map_info, template_id, title):

        allure.dynamic.title(title)
        map_info['draftId'] += 1
        r = self.um.publish_ugc_draft(self.uid, data_type, operation_type, map_info)

        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        self.assert_not_empty(r['data']['mapId'])
        self.assert_value_in(r['data']['mapId'], map_info['mapId'])
        draft_list = self.um.get_draft_create_list(self.uid, data_type=data_type)
        map_ids = [d['mapId'] for d in draft_list['data']['mapInfos']]
        map_names = [d['mapName'] for d in draft_list['data']['mapInfos']]
        self.assert_value_in(map_info['mapName'], map_names)
        self.assert_value_in(map_info['mapId'], map_ids)

    @allure.story('ugc草稿发布')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("data_type,operation_type,map_info,template_id,title",
                             Config.case_data_dict("ugc_map.yml", 'publish_ugc_draft'))
    def test_publish_ugc_draft(self, data_type, operation_type, map_info, template_id, title):
        allure.dynamic.title(title)
        map_name = map_info['mapName']
        map_info['draftId'] += 1
        if data_type != 3:
            map_name = map_name + '-' + TimeTools.get_now_sec_timestamp()
        map_info['mapDesc'] = map_info['mapDesc'] + '-' + TimeTools.get_now_sec_timestamp()
        r = self.um.publish_ugc_draft(self.uid, data_type, operation_type, map_info, map_name=map_name)
        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        map_id = r['data']['mapId']
        self.assert_not_empty(map_id)
        r1 = self.um.get_ugc_detail_info(self.uid, map_id)
        self.assert_api_success_code(r1)
        self.assert_data_not_empty(r1)
        map_info = r1['data']['mapInfo']
        self.assert_equal(map_info['mapId'], map_id)
        self.assert_not_empty(map_info['mapCover'])
        self.assert_not_empty(map_info['mapCoverFull'])
        self.assert_not_empty(map_info['mapName'])
        # self.assert_any_not_empty(
        #     [map_info['mapJson'], map_info['propsJson'], map_info['clothesJson'], map_info['clothesUrl']])
        self.assert_rsp_json(map_info)
        self.assert_not_empty(map_info['mapDesc'])
        self.assert_not_empty(map_info['mapCreator'])
        self.assert_not_empty(str(map_info['dataType']))
        if data_type != 3:   # 3是space，不走删除逻辑
            r = self.um.delete_ugc_draft(self.uid, map_info)
            self.assert_api_success_code(r)
            self.assert_equal(r['data']['mapId'], map_id)

    @allure.story('ugc地图草稿覆盖发布cover原地图')
    @pytest.mark.smoking
    @pytest.mark.ugc
    def test_cover_publish_ugc_draft_same_map(self):
        d = Config.case_data('ugc_map.yml', 'cover_publish_ugc_draft_same_map')
        d.map_info['mapDesc'] = d.map_info['mapDesc'] + '-' + TimeTools.get_now_sec_timestamp()
        r = self.um.publish_ugc_draft(self.uid, d.data_type, d.operation_type, d.map_info,
                                      overwrite_map_id=d.overwrite_map_id)
        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        map_id = r['data']['mapId']
        self.assert_equal(map_id, d.overwrite_map_id)
        r1 = self.um.get_ugc_detail_info(self.uid, map_id)
        self.assert_api_success_code(r1)
        self.assert_data_not_empty(r1)
        map_info = r1['data']['mapInfo']
        self.assert_equal(map_info['mapId'], map_id)
        self.assert_not_empty(map_info['mapCover'])
        self.assert_not_empty(map_info['mapCoverFull'])
        self.assert_not_empty(map_info['mapName'])
        # self.assert_any_not_empty(
        #     [map_info['mapJson'], map_info['propsJson'], map_info['clothesJson'], map_info['clothesUrl']])
        self.assert_rsp_json(map_info)
        self.assert_not_empty(map_info['mapDesc'])
        self.assert_not_empty(map_info['mapCreator'])
        self.assert_not_empty(str(map_info['dataType']))

    @allure.story('ugc地图草稿覆盖发布cover不同地图')
    @pytest.mark.smoking
    @pytest.mark.ugc
    def test_cover_publish_ugc_draft_different_map(self):

        d1 = Config.case_data('ugc_map.yml', 'cover_publish_ugc_draft_same_map')
        case_map_id = d1.overwrite_map_id
        r0 = self.um.get_ugc_publish_list(self.uid, self.uid, data_type=0)
        map_ids = [data['mapId'] for data in r0['data']['mapInfos'] if data['mapId'] != case_map_id]
        overwrite_map_id = random.choice(map_ids)
        d = Config.case_data('ugc_map.yml', 'publish_ugc_draft_different_map')
        d.map_info['mapName'] = d.map_info['mapName'] + TimeTools.get_now_sec_timestamp()
        d.map_info['mapDesc'] = d.map_info['mapDesc'] + '-' + TimeTools.get_now_sec_timestamp()
        r = self.um.publish_ugc_draft(self.uid, d.data_type, d.operation_type, d.map_info,
                                      overwrite_map_id=overwrite_map_id)
        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        map_id = r['data']['mapId']
        self.assert_equal(map_id, overwrite_map_id)
        r1 = self.um.get_ugc_detail_info(self.uid, map_id)
        self.assert_api_success_code(r1)
        self.assert_data_not_empty(r1)
        map_info = r1['data']['mapInfo']
        self.assert_equal(map_info['mapId'], map_id)
        self.assert_not_empty(map_info['mapCover'])
        self.assert_not_empty(map_info['mapCoverFull'])
        self.assert_not_empty(map_info['mapName'])

        # self.assert_any_not_empty(
        #     [map_info['mapJson'], map_info['propsJson'], map_info['clothesJson'], map_info['clothesUrl']])
        self.assert_rsp_json(map_info)
        self.assert_not_empty(map_info['mapDesc'])
        self.assert_not_empty(map_info['mapCreator'])
        self.assert_not_empty(str(map_info['dataType']))

    @allure.story('ugc草稿列表获取')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("title,data_type", [
        ["地图草稿列表获取", 0], ["素材草稿列表获取", 1],
        ["衣服草稿列表获取", 2], ["space草稿列表获取", 3],
        ["材质草稿列表获取", 4]
    ])
    def test_get_draft_create_list(self, title, data_type):
        allure.dynamic.title(title)

        r = self.um.get_draft_create_list(self.uid, data_type)

        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        self.assert_not_empty(r['data']['cookie'])
        self.assert_value_in(r['data']['isEnd'], [0, 1])
        self.assert_length_gt_zero(r['data']['mapInfos'])

    @allure.story('ugc草稿列表翻页刷新获取')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("title,data_type", [
        ["地图草稿列表获取", 0], ["素材草稿列表获取", 1], ["衣服草稿列表获取", 2], ["材质草稿列表获取", 4]
    ])
    def test_get_draft_create_list_with_cookie(self, title, data_type):
        allure.dynamic.title(title)

        r = self.um.get_draft_create_list(self.uid, data_type)

        self.assert_api_success_code(r)
        if r['data'].get('isEnd', None) != 1:
            r = self.um.get_draft_create_list(self.uid, data_type, cookie=r['data']['cookie'])
            self.assert_api_success_code(r)
            map_infos = r['data'].get('mapInfos', None)
            if map_infos:
                self.assert_not_empty(r['data']['cookie'], msg="r['data']['cookie']")
                self.assert_value_in(r['data']['isEnd'], [0, 1])
                self.assert_length_gt_zero(map_infos)

    @allure.story('ugc发布列表获取')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("to_uid,", [[uid], [to_uid]])
    @pytest.mark.parametrize("title,data_type", [
        ["获取map发布列表", 0], ["获取prop发布列表", 1], ["获取clothes发布列表", 2], ["获取材质发布列表", 4]
    ])
    def test_get_ugc_publish_list(self, title, to_uid, data_type):
        allure.dynamic.title(title)

        r = self.um.get_ugc_publish_list(self.uid, to_uid, data_type)
        self.assert_api_success_code(r)
        self.assert_value_in(r['data']['isEnd'], [0, 1])
        map_infos = r['data'].get('mapInfos', None)
        if map_infos:
            self.assert_not_empty(r['data']['cookie'])
            self.assert_length_gt_zero(map_infos)

    @allure.story('ugc发布列表获取')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("to_uid,", [uid, to_uid])
    @pytest.mark.parametrize("title,data_type", [
        ["加入cookie再次获取map发布列表", 0], ["加入cookie获取prop发布列表", 1], ["加入cookie获取clothes发布列表", 2],
        ["加入cookie获取材质发布列表", 4]
    ])
    def test_get_ugc_publish_list_with_cookie(self, title, to_uid, data_type):

        allure.dynamic.title(title)
        # if Config.get_run_env_name() in ("ALPHA", "PROD") and self.uid != to_uid:
        #     return

        r1 = self.um.get_ugc_publish_list(self.uid, to_uid, data_type)
        self.assert_api_success_code(r1)
        self.assert_value_in(r1['data']['isEnd'], [0, 1])
        map_infos = r1['data'].get('mapInfos', None)
        if map_infos:
            self.assert_not_empty(r1['data']['cookie'])
            self.assert_length_gt_zero(map_infos)
        is_end = r1['data']['isEnd']
        cookie = r1['data']['cookie']
        if cookie and is_end != 1:
            r2 = self.um.get_ugc_publish_list(self.uid, to_uid, data_type=data_type, cookie=cookie)
            self.assert_api_success_code(r2)
            self.assert_data_not_empty(r2)
            self.assert_value_in(r2['data']['isEnd'], [0, 1])
            map_infos = r2['data'].get("mapInfos", None)
            if map_infos:
                self.assert_not_empty(r2['data']['cookie'])
                self.assert_length_gt_zero(r2['data']['mapInfos'])

    @allure.story('ugc详情页获取')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("map_id,title", Config.case_data_dict("ugc_map.yml", "get_ugc_detail_info"))
    def test_get_ugc_detail_info(self, map_id, title):
        allure.dynamic.title(title)

        r = self.um.get_ugc_detail_info(self.uid, map_id)
        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        map_info = r['data']['mapInfo']
        self.assert_equal(map_info['mapId'], map_id)
        self.assert_not_empty(map_info['mapCover'])
        self.assert_not_empty(map_info['mapCoverFull'])
        self.assert_not_empty(map_info['mapName'])
        # self.assert_any_not_empty(
        #     [map_info['mapJson'], map_info['propsJson'], map_info['clothesJson'], map_info['clothesUrl']])
        self.assert_rsp_json(map_info)
        self.assert_not_empty(map_info['mapDesc'])
        self.assert_not_empty(map_info['mapCreator'])
        self.assert_not_empty(str(map_info['dataType']))

    @allure.story("Tab-Studio")  # todo 51版本后去掉studio相关的
    @pytest.mark.smoking
    @pytest.mark.ugc
    def test_get_studio_list(self):
        allure.dynamic.title("Studio tab拉取第一页配置的模板")

        r = self.um.get_studio_list(self.uid)
        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)

        studio_infos = r['data'].get("studioInfos", None)
        if studio_infos:
            studio = studio_infos[0]
            self.assert_not_empty(studio['ugcTemplate'])
            ut = studio['ugcTemplate']
            self.assert_not_empty(str(ut['id']))
            self.assert_not_empty(ut['mapCover'])
            self.assert_not_empty(ut['mapCoverFull'])
            self.assert_not_empty(ut['mapName'])
            self.assert_not_empty(str(ut['dataType']))
            self.assert_not_empty(studio["mapInfo"])
            mi = studio["mapInfo"]
            self.assert_not_empty(mi['mapId'])
            self.assert_not_empty(mi['mapCover'])
            self.assert_not_empty(mi['mapCoverFull'])
            self.assert_not_empty(studio['studioDesc'])
            # self.assert_not_empty(studio['studioName'])
            self.assert_not_empty(studio['studioCover'])
            self.assert_not_empty(str(studio['dataType']))
            self.assert_not_empty(studio['studioUserInfo'])

    @allure.story("Tab-Studio")
    @pytest.mark.smoking
    @pytest.mark.ugc
    def test_get_studio_list_with_cookie(self):
        allure.dynamic.title("Studio tab 翻页拉取配置的模板")

        r = self.um.get_studio_list(self.uid)
        self.assert_api_success_code(r)
        self.assert_data_not_empty(r)
        is_end = r['data']['isEnd']
        if is_end == 0:
            cookie = r['data']['cookie']
            r = self.um.get_studio_list(self.uid, cookie=cookie)
            self.assert_api_success_code(r)
            self.assert_data_not_empty(r)

            studio_infos = r['data'].get("studioInfos", None)
            if studio_infos:
                studio = studio_infos[0]
                self.assert_not_empty(studio['ugcTemplate'])
                ut = studio['ugcTemplate']
                self.assert_not_empty(str(ut['id']))
                self.assert_not_empty(ut['mapCover'])
                self.assert_not_empty(ut['mapCoverFull'])
                self.assert_not_empty(ut['mapName'])
                self.assert_not_empty(str(ut['dataType']))
                self.assert_not_empty(studio["mapInfo"])
                mi = studio["mapInfo"]
                self.assert_not_empty(mi['mapId'])
                self.assert_not_empty(mi['mapCover'])
                self.assert_not_empty(mi['mapCoverFull'])
                self.assert_not_empty(studio['studioDesc'])
                # self.assert_not_empty(studio['studioName'])
                self.assert_not_empty(studio['studioCover'])
                self.assert_not_empty(str(studio['dataType']))
                self.assert_not_empty(studio['studioUserInfo'])

    @allure.story('ugc点赞列表获取')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("to_uid", [uid])
    @pytest.mark.parametrize("title,data_type,listType", [
        ["获取map点赞列表", 0, 1], ["获取prop点赞列表", 1, 1], ["获取clothes点赞列表", 2, 1]])
    def test_get_ugc_like_list(self, title, to_uid, data_type, listType):
        allure.dynamic.title(title)

        r = self.um.get_ugc_favorite_list(self.uid, to_uid, data_type, listType)
        self.assert_api_success_code(r)
        self.assert_not_empty(r['data']['cookie'])
        self.assert_value_in(r['data']['isEnd'], [0, 1])
        self.assert_length_gt_zero(r['data']['mapInfos'])

    @allure.story('ugc点赞列表分页获取')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("to_uid", [uid])
    @pytest.mark.parametrize("title,data_type,listType", [
        ["加入cookie获取map点赞列表", 0, 1], ["加入cookie获取prop点赞列表", 1, 1], ["加入cookie获取clothes点赞列表", 2, 1]])
    def test_get_ugc_like_list_with_cookie(self, title, to_uid, data_type, listType):
        allure.dynamic.title(title)

        r1 = self.um.get_ugc_favorite_list(self.uid, to_uid, data_type, listType)
        self.assert_api_success_code(r1)
        self.assert_not_empty(r1['data']['cookie'])
        self.assert_value_in(r1['data']['isEnd'], [0, 1])
        self.assert_length_gt_zero(r1['data']['mapInfos'])

        is_end = r1['data']['isEnd']
        cookie = r1['data']['cookie']
        if cookie and is_end != 1:
            r2 = self.um.get_ugc_favorite_list(self.uid, to_uid, data_type, listType, cookie=cookie)
            self.assert_api_success_code(r2)
            self.assert_data_not_empty(r2)
            self.assert_value_in(r2['data']['isEnd'], [0, 1])
            map_infos = r2['data'].get("mapInfos", None)
            if map_infos:
                self.assert_not_empty(r2['data']['cookie'])
                self.assert_length_gt_zero(r2['data']['mapInfos'])

    @allure.story('ugc收藏列表获取')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("to_uid,", [uid])
    @pytest.mark.parametrize("title,data_type,listType", [["获取map收藏列表", 0, 0]])
    def test_get_ugc_favorite_list(self, title, to_uid, data_type, listType):
        allure.dynamic.title(title)

        r = self.um.get_ugc_favorite_list(self.uid, to_uid, data_type, listType)
        self.assert_api_success_code(r)
        self.assert_not_empty(r['data']['cookie'])
        self.assert_value_in(r['data']['isEnd'], [0, 1])
        self.assert_length_gt_zero(r['data']['mapInfos'])

    @allure.story('ugc收藏列表分页获取')
    @pytest.mark.smoking
    @pytest.mark.ugc
    @pytest.mark.parametrize("to_uid,", [uid])
    @pytest.mark.parametrize("title,data_type,listType", [["加入cookie获取map收藏列表", 0, 0]])
    def test_get_ugc_favorite_list_with_cookie(self, title, to_uid, data_type, listType):
        allure.dynamic.title(title)

        r1 = self.um.get_ugc_favorite_list(self.uid, to_uid, data_type, listType)
        self.assert_api_success_code(r1)
        self.assert_not_empty(r1['data']['cookie'])
        self.assert_value_in(r1['data']['isEnd'], [0, 1])
        self.assert_length_gt_zero(r1['data']['mapInfos'])

        is_end = r1['data']['isEnd']
        cookie = r1['data']['cookie']
        if cookie and is_end != 1:
            r2 = self.um.get_ugc_favorite_list(self.uid, to_uid, data_type, listType, cookie=cookie)
            self.assert_api_success_code(r2)
            self.assert_data_not_empty(r2)
            self.assert_value_in(r2['data']['isEnd'], [0, 1])
            map_infos = r2['data'].get("mapInfos", None)
            if map_infos:
                self.assert_not_empty(r2['data']['cookie'])
                self.assert_length_gt_zero(r2['data']['mapInfos'])
