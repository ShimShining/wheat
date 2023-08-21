# -*- coding: utf-8 -*-
"""
@Author: shining
@File: public_server_mock.py
@Date: 2022/11/10 11:27 上午
@Version: python 3.9
@Describe: mock public server 参数拼接
"""
import json
import random
import string

from business.search.search import Search
from config import Config


class PublicServerMock:
    __search_users = Search()
    __uid = Config.case_data('global_user_info').uid

    def handle_players_data(self, user_infos, count):
        res = []
        if user_infos:
            for i, val in enumerate(user_infos):
                if i < count:
                    item = {
                        "uid": val['userInfo']['uid'],
                        'userName': val['userInfo']['userName'],
                        'userNick': val['userInfo']['userNick'],
                        'portraitUrl': val['userInfo']['portraitUrl']
                    }
                    res.append(item)
        return res

    def get_players(self, count=20, kw="ID_q"):

        if count <= 20:
            r = self.__search_users.get_search_user(self.__uid, kw)
            user_infos = r['data'].get('searchInfo', None)
            res = self.handle_players_data(user_infos, count)
            return res
        page_count = count // 20
        last_page_size = count % 20
        cookie = None
        res = []
        for i in range(page_count):
            if i == 0:
                r = self.__search_users.get_search_user(self.__uid, kw)
                user_infos = r['data'].get('searchInfo', None)
                result = self.handle_players_data(user_infos, 20)
                cookie = r['data']['cookie']
            else:
                r = self.__search_users.get_search_user(self.__uid, kw, cookie=cookie)
                user_infos = r['data'].get('searchInfo', None)
                result = self.handle_players_data(user_infos, 20)
                cookie = r['data']['cookie']
            res += result
        if last_page_size:
            r = self.__search_users.get_search_user(self.__uid, kw, cookie=cookie)
            user_infos = r['data'].get('searchInfo', None)
            result = self.handle_players_data(user_infos, last_page_size)
            res += result

        return res

    def mock_public_server_count_rsp(self, count=20, need_user=None):
        """
        :param players: 字典类型的players
        {
            "uid": "",
            "userName": "kin",
            "userNick": "",
            "portraitUrl": ""
                }
        :return:
        """
        if need_user:
            players = self.get_players(count=need_user)
        else:
            players = None
        rsp = {}
        if players:
            temp = []
            for i, p in enumerate(players):
                if i >= 5:
                    break
                p.pop('userNick', None)
                temp.append(p)
            rsp['data']['downtownPlayers'] = temp
            rsp['data']['downtownPlayerCount'] = count
        else:
            rsp['data']['downtownPlayers'] = players
            rsp['data']['downtownPlayerCount'] = count

        return rsp

    def random_search_kw(self):
        letters = list(string.ascii_letters)

        return "".join(random.choices(letters, k=2))

    def random_generate_room_code(self):

        letters = list(string.ascii_letters)
        nums = list(string.digits)
        code_pools = letters + nums
        return "".join(random.choices(code_pools, k=9))

    def generate_room_card(self, player_count=None):

        room = dict()
        room['roomCode'] = self.random_generate_room_code()
        room['maxPlayer'] = 50
        room['roomPlayerNum'] = player_count if player_count else random.randint(1, 50)
        room['players'] = None
        room['PlayerUid'] = None
        return room

    def mock_public_server_list(self, cards=2, card_heads=None):
        """

        :param cards:
        :param card_heads: [(i, count)]
        :return:
        """
        rsp = {}
        server_list = []
        for i in range(cards):
            room = self.generate_room_card(player_count=card_heads[i][2])
            server_list.append(room)
        if card_heads:
            for i, v, _ in card_heads:
                if v:
                    players = self.get_players(count=v, kw=self.random_search_kw())
                    player_uids = [p['uid'] for p in players]
                    server_list[i]['players'] = players
                    server_list[i]['PlayerUid'] = player_uids

        rsp['data']['serverList'] = server_list
        if cards > 12:
            rsp['data']['isEnd'] = 0

        return rsp

    def mock_hangout(self, player_count=1, is_view=False, icon_player_num=None):

        rsp = {}
        icon_players = self.get_players(count=icon_player_num)
        rsp['data']['iconPlayers'] = icon_players
        return rsp

    def mock_hangout_list(self, cards=1, card_heads=None):
        """

        :param cards:
        :param card_heads: (0, friends, player_count, max_player)
        :return:
        """

        rsp = {}
        server_list = []
        for i in range(cards):
            room = self.generate_downtown_room(player_count=card_heads[i][2], max_player=card_heads[i][3])
            server_list.append(room)
        if card_heads:
            for i, v, _, _ in card_heads:
                if v:
                    players = self.get_players(count=v)
                    player_uids = [p['uid'] for p in players]
                    server_list[i]['players'] = players
                    server_list[i]['PlayerUid'] = player_uids

        rsp['data']['serverList'] = server_list
        if cards > 12:
            rsp['data']['isEnd'] = 0
        return rsp

    def generate_downtown_room(self, max_player=16, player_count=16):

        down_town_room = dict()
        down_town_room['maxPlayer'] = max_player
        down_town_room['mapName'] = "Great Snowfield（Beta）"
        down_town_room['mapCover'] = ""
        down_town_room['mapId'] = ""
        down_town_room['roomCode'] = self.random_generate_room_code()
        down_town_room['roomPlayerNum'] = player_count
        return down_town_room

    def write_rsp_to_file(self, file_name, rsp):

        with open(file_name, "w") as f:
            json.dump(rsp, f)


if __name__ == '__main__':
    psm = PublicServerMock()

    # 首页Public Servers
    # rsp = psm.mock_public_server_count_rsp(count=6, need_user=6)
    # psm.write_rsp_to_file('./result/public_server_count.json', rsp)
    # print(json.dumps(rsp, indent=4, ensure_ascii=False))


    # Public Server list
    rsp = psm.mock_public_server_list(cards=12, card_heads=[
        (0, 0, 16), [1, 15, 16], [2, 1, 18], [3, 10, 18], [4, 11, 52], [5, 9, 9], [6, 16, 16], [7, 20, 21],
        [8, 15, 19], [9, 50, 50], [10, 14, 14], [11, 11, 20]
    ])
    psm.write_rsp_to_file('./result/public_server_list.json', rsp)
    # # print(rsp)

    # hangout
    # rsp = psm.mock_hangout(player_count=5, is_view=True, icon_player_num=5)
    # # print(json.dumps(rsp, indent=4, ensure_ascii=False))
    # psm.write_rsp_to_file('./result/hangout.json', rsp)

    # hangout list
    # (0, friends, player_count, max_player)
    # rsp = psm.mock_hangout_list(cards=8, card_heads=[
    #     (0, 1, 5, 50), (1, 5, 5, 50), (2, 6, 19, 50), (3, 10, 10, 50), (4, 11, 20, 50), (5, 19, 19, 50),
    #     (6, 33, 40, 50), (7, 50, 50, 50)
    # ])
    # print(json.dumps(rsp, indent=4, ensure_ascii=False))
    # psm.write_rsp_to_file('./result/hangout_list.json', rsp)
