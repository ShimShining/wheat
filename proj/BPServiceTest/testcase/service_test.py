# -*- coding: utf-8 -*-
"""
@Author: shining
@File: service_test.py
@Date: 2021/11/15 7:49 下午
@Version: python 3.10
@Describle: 测试基类
"""
from proj.BPServiceTest.base.base_api_test import BaseApiTest
from proj.BPServiceTest.base.bp_exception import *


class ServiceTest(BaseApiTest):

    def assert_that_api(self, actual, expect):

        pass

    def assert_api_success_code(self, r):

        self.assert_result_is_zero(r)
        self.assert_rsmg_is_empty(r)
        try:
            assert r['data']
            self.log.info("接口返回code正确，无错误信息")
        except AssertionError as e:
            self.log.error(e)
            err = f" api 返回的响应[data]为empty，不符合预期！！！"
            self.log.error(err)
            raise ValueEmptyError(err)

    def assert_result_is_zero(self, r):

        try:
            assert r['result'] == 0
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f" ResultIsNotZeroError: api返回体字段result值不等于0，实际返回值={r['result']}")
            raise ResultIsNotZeroError(f"api返回体字段result值不等于0，实际返回值={r['result']}")

    def assert_rsmg_is_empty(self, r):
        try:
            assert r['rmsg'] == ""
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f" ValueNotEmptyError: api返回体字段rmsg不为空, r['rmsg']={r['rmsg']}")
            raise ValueNotEmptyError(f" ValueNotEmptyError: api返回体字段rmsg不为空, r['rmsg']={r['rmsg']}")

    def assert_length_gt_zero(self, r):
        """
        对象的长度大于0
        :param r:
        :return:
        """
        try:
            assert len(r) > 0
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f" LengthLTZeroError: 长度不大于0，实际长度={len(r)}")
            raise LengthLTZeroError(f" LengthLTZeroError: 长度不大于0，实际长度={len(r)}")

    def assert_engine_room_info(self, player_id, r, data, room_type, owner_id=None):

        self.assert_equal(r['err_code'], 0)
        self.assert_not_empty(r["msg"])
        data2 = r['msg']
        self.assert_equal(data2['room_info']['id'], data['roomId'])
        self.assert_equal(data2['room_info']['type'], room_type)
        if not owner_id:
            owner_id = [player_id]
        self.assert_value_in(data2['room_info']['owner'], owner_id)
        player_list = data2['room_info']["player_list"]
        players = [p['id'] for p in player_list]
        self.assert_value_in(player_id, players)
        for p in player_list:
            self.assert_not_empty(p['id'])
            self.assert_value_in(p['common_network_state'], [0, 1])
            # self.assert_not_empty(p['player_session'])
            self.assert_not_empty(p["timestamp"])
        self.assert_not_empty(data2["room_info"]["frame_rate"])
        self.assert_not_empty(data2["room_info"]['create_time'])
        self.assert_value_in(data2["room_info"]["is_open_blood"], [True, False])

    def assert_session_info_right(self, session_info):

        self.assert_not_empty(session_info['framePort'])
        self.assert_not_empty(session_info['ipAddress'])
        self.assert_not_empty(session_info['port'])
        self.assert_not_empty(session_info['roomId'])

    def assert_frame_data_in(self, send_id, frame_data, res):

        flag = False

        for data in res:
            items = data['Data']['frame'].get('items', None)
            if items:
                for item in items:
                    frame_res_data = item.get("data", None)
                    if frame_res_data and frame_data == frame_res_data:
                        frame_res_player_id = item.get("player_id", None)
                        if frame_res_player_id and frame_res_player_id == send_id:
                            flag = True
        try:
            assert flag
        except AssertionError as e:
            self.log.error(e)
            self.log.error(f"send_id={send_id}发送的帧数据未被接收到，frame_data={frame_data}")
            raise NotContainValueError(f"send_id={send_id}发送的帧数据未被接收到，frame_data={frame_data}")




