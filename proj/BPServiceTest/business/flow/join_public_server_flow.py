# -*- coding: utf-8 -*-
"""
@Author: shining
@File: join_public_server.py
@Date: 2022/6/20 3:52 下午
@Version: python 3.9
@Describe: 进入房间（公共，私人）房间流程
"""
import time


class JoinPublicServerFlow:

    def __init__(self):
        from proj.BPServiceTest.business.engine.engine_simulation import EngineSimulation
        self.engine = EngineSimulation()

    def join_public_server_single_player(self, info: dict, **kwargs):
        """
        info： player_id， version，room_type
        :param info:
        :return: session info，room detail info
        """
        player_id = info['player_id']
        room_type = info['room_type']
        version = info['version']
        room_code = info.get('room_code', None)
        max_player = info.get('max_player', None)
        is_private = info.get('is_private', None)
        session_info = info.get("session_info", None)
        if session_info:
            room_code = session_info.get("roomId", None)
        # 1. 公共房间获取gameSession
        if not is_private:
            if room_code:
                if not max_player:
                    r1 = self.engine.get_game_session(player_id, room_type, version=version, room_code=room_code,
                                                      **kwargs)
                else:
                    r1 = self.engine.get_game_session(player_id, room_type, version=version, room_code=room_code,
                                                      max_player=max_player, **kwargs)
            else:
                if not max_player:
                    r1 = self.engine.get_game_session(player_id, room_type, version=version, **kwargs)
                else:
                    r1 = self.engine.get_game_session(player_id, room_type, version=version, max_player=max_player,
                                                      **kwargs)
        # 私人房间获取gameSession
        else:
            # 没有传房间码，通过gameSession创建链接
            if not room_code:

                if not max_player:
                    r1 = self.engine.get_game_session(player_id, room_type, version=version, is_private=is_private,
                                                      **kwargs)
                else:
                    r1 = self.engine.get_game_session(player_id, room_type, version=version, max_player=max_player,
                                                      is_private=is_private, **kwargs)
            # 传入了房间码或者sessionInfo，通过房间码或者session_info['roomId']进去房间
            else:
                if not max_player:
                    r1 = self.engine.get_game_session(player_id, room_type, version=version, room_code=room_code,
                                                      is_private=is_private, **kwargs)
                else:
                    r1 = self.engine.get_game_session(player_id, room_type, version=version,
                                                      room_code=room_code, max_player=max_player,
                                                      is_private=is_private, **kwargs)
        # 获取返回参数中session_info
        session_info = dict()
        session_info = r1['msg']
        # 2.user进入房间 入参：player_id, g_session_id, room_type, room_id, version
        # token = info.get("token", None)
        # if not token:
        if not max_player:
            r2 = self.engine.enter_room(player_id, session_info['sessionId'], room_type, session_info['roomId'],
                                        session_info['ipAddress'], session_info['port'], version=version,
                                        frame_port=session_info['framePort'], **kwargs)
        else:
            r2 = self.engine.enter_room(player_id, session_info['sessionId'], room_type, session_info['roomId'],
                                        session_info['ipAddress'], session_info['port'], version=version,
                                        max_player=max_player, frame_port=session_info['framePort'], **kwargs)

        if r2['err_code'] == 5003:
            self.engine.leave_room(player_id, session_info['roomId'], version=version, **kwargs)
            time.sleep(3)
            # if not token:
            if not max_player:
                self.engine.enter_room(player_id, session_info['sessionId'], room_type, session_info['roomId'],
                                       session_info['ipAddress'], session_info['port'], version=version,
                                       frame_port=session_info['framePort'], **kwargs)
            else:
                self.engine.enter_room(player_id, session_info['sessionId'], room_type, session_info['roomId'],
                                       session_info['ipAddress'], session_info['port'], version=version,
                                       max_player=max_player, frame_port=session_info['framePort'], **kwargs)

        # 3. 获取房间详情, 入参： game_session_id, locale="cn", version='1.32.0
        r3 = self.engine.get_room_detail(player_id, session_info['roomId'], version=version, **kwargs)
        assert r3['err_code'] == 0

        # 4. 房间内开始帧同步 入参：player_id, room_id, locale="cn", version='1.32.0'
        r4 = self.engine.start_frame_sync(player_id, session_info['roomId'], version=version, **kwargs)
        assert r4['err_code'] == 0
        print(f"==============>>> 房间码=【{session_info['roomId']}】内玩家{player_id}开启帧同步成功")
        return session_info, r3
