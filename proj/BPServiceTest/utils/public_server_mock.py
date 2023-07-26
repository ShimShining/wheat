# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: public_server_mock.py
@Date: 2022/11/10 11:27 上午
@Version: python 3.9
@Describe: mock public server 参数拼接
"""
import json
import random
import string

from us_api_test.business.search.search import Search
from us_api_test.config import Config


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
            "uid": "1527534371115646976",
            "userName": "kin",
            "userNick": "",
            "portraitUrl": "https://image-cdn.joinbudapp.com/UgcImage/1527534371115646976/Profile1527534371115646976_1653316800.png"
                }
        :return:
        """
        if need_user:
            players = self.get_players(count=need_user)
        else:
            players = None
        rsp = {
            "result": 0,
            "rmsg": "",
            "data": {
                "downtownInfo": {
                    "downtownId": "teambud_downtown1_1",
                    "downtownName": "Great Snowfield（Beta）",
                    "downtownCover": "https://buddy-app-bucket.s3.us-west-1.amazonaws.com/downtown_new/pr/teambud_downtown1_1/detailpage.png",
                    "downtownPngPrefix": "https://image-cdn.joinbudapp.com/downtown11071519/pr/teambud_downtown1_1/",
                    "downtownJson": "https://cdn.joinbudapp.com/great_field/1668578712.json",
                    "downtownDesc": "The Great Snowfield is the marvelous spectacles of the Forgotten Wonders.  Dangers and opportunities scatter in the alpine region.  Greatest treasures belong to the brave and the wise. Let the adventure begin!",
                    "downtownDescLanguage": "en",
                    "downtownNameLanguage": "en",
                    "editorVersion": "1.50.0",
                    "hasPublicServer": 1,
                    "downtownStatus": {
                        "clickMsg": ""
                    }
                },
                "downtownCard": {
                    "cardCover": "https://image-cdn.joinbudapp.com/downtown_new/master/teambud_downtown1_1/50downtownCard.png",
                    "cardTitle": "Great Snowfield",
                    "cardDesc": "The Great Snowfield opens new challenges for adventurers. Collecting BUD coins can unlock plenty of limited rewards! It's time to form your adventure team and hunt for BUD coins!",
                    "buttonTextColor": "#0088FF"
                },
                "downtownPlayerCount": 0,
                "downtownPlayers": [{
                    "uid": "1585532114517704704",
                    "userName": "id_8xq_pa_owvvcwwwwwwwww",
                    "portraitUrl": "https://buddy-app-bucket.s3-accelerate.amazonaws.com/peopleHeadImg/15855321145177047041667194411930coverImg.png"
                }, {
                    "uid": "1592716446843670528",
                    "userName": "ID_8z8a24aljvqm",
                    "portraitUrl": "https://buddy-app-bucket.s3-accelerate.amazonaws.com/peopleHeadImg/1592716446843670528coverImg.png"
                }],
                "storyCard": {
                    "cardCover": "https://image-cdn.joinbudapp.com/downtown_new/master/teambud_downtown1_1/50storyCard.png",
                    "cardTitle": "Above the Clouds",
                    "cardDesc": "Decorate your space to unlock outfits!",
                    "buttonTextColor": "#FF4D88"
                },
                "storyInfo": {
                    "mapId": "1592148384070971392_1668516581_6",
                    "mapCover": "https://image-cdn.joinbudapp.com/fit-in/570x330/spaceTemplate/MySpace_Cover.jpg",
                    "mapCoverFull": "https://cdn.joinbudapp.com/spaceTemplate/MySpace_Cover.jpg",
                    "mapName": "Above the Clouds",
                    "mapNameLanguage": "en",
                    "mapJson": "https://cdn.joinbudapp.com/spaceTemplate/MySpace_Json.json",
                    "mapDesc": "",
                    "mapDescLanguage": "en",
                    "mapCreator": {
                        "uid": "1592148384070971392",
                        "userName": "ID_8z3xc80r73n5",
                        "userNick": "ID_8z3xc80r73n5",
                        "portraitUrl": "https://image-cdn.joinbudapp.com/fit-in/128x128/peopleHeadImg/1592148384070971392_1668432730.png"
                    },
                    "dataType": 3,
                    "dataSubType": 1,
                    "hasPropList": 0,
                    "hasDcList": 0,
                    "hasComments": 0,
                    "hasPhotos": 0,
                    "hasLeaderboard": 0,
                    "hasPublicServer": 0,
                    "lastModifiedTime": 0,
                    "propsBuyLevel": {
                        "propsType": 0,
                        "userList": None
                    },
                    "isLimit": 0,
                    "audioList": None,
                    "highestResIds": None,
                    "draftId": 0,
                    "templateId": 0,
                    "maxPlayer": 0,
                    "editTime": 0,
                    "buyNumLimit": 0,
                    "isIncludeCollection": 0,
                    "isDC": 0,
                    "dcInfo": None,
                    "isPurchase": 0,
                    "isPGC": 0,
                    "groupServers": None,
                    "renderJson": "",
                    "jsonUrl": "",
                    "dataUrl": "",
                    "hasMaterial": False,
                    "storySpaceStatus": 1
                },
                "appstoreUpdate": False
            },
            "requestId": "pr-cdq8d7pm59d0gb6c35kg"
        }
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
        rsp = {
            "result": 0,
            "rmsg": "",
            "data": {
                "cookie": "{\"paging_key\":null,\"offset\":2}",
                "isEnd": 1,
                "active": 49,
                "serverList": [{
                    "roomCode": "BFXrUFdJu",
                    "maxPlayer": 50,
                    "roomPlayerNum": 42,
                    "players": None,
                    "PlayerUid": None
                }, {
                    "roomCode": "MHim8rr0a",
                    "maxPlayer": 8,
                    "roomPlayerNum": 7,
                    "players": None,
                    "PlayerUid": None
                }]
            },
            "requestId": "master-e6a71297-6ee1-44fc-a874-fee398139345"
        }
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

        rsp = {
            "result": 0,
            "rmsg": "",
            "data": {
                "cookie": "{\"paging_key\":null,\"offset\":1}",
                "isEnd": 1,
                "downtownServer": {
                    "maxPlayer": 16,
                    "mapName": "Great Snowfield（Beta）",
                    "mapCover": "https://image-cdn.joinbudapp.com/downtown11071519/pr/teambud_downtown1_1/hangout.png",
                    "roomCode": "TNVekeAK2",
                    "mapId": "teambud_downtown1_1",
                    "players": [{
                        "uid": "1592716446843670528",
                        "userName": "ID_8z8a24aljvqm",
                        "userNick": "",
                        "portraitUrl": "https://image-cdn.joinbudapp.com/peopleHeadImg/1592716446843670528coverImg.png"
                    }],
                    "roomPlayerNum": 1,
                    "PlayerUid": ["1592716446843670528"]
                },
                "isView": f"{is_view}",
                "playerCount": f"{player_count}",  # 全部在房人数
                "iconPlayers": [{
                    "uid": "1592716446843670528",
                    "userName": "ID_8z8a24aljvqm",
                    "userNick": "",
                    "portraitUrl": "https://buddy-app-bucket.s3-accelerate.amazonaws.com/peopleHeadImg/1592716446843670528coverImg.png"
                }]
            },
            "requestId": "pr-cdq9d5pm59d4ed4tqkkg"
        }
        icon_players = self.get_players(count=icon_player_num)
        rsp['data']['iconPlayers'] = icon_players
        return rsp

    def mock_hangout_list(self, cards=1, card_heads=None):
        """

        :param cards:
        :param card_heads: (0, friends, player_count, max_player)
        :return:
        """

        rsp = {
            "result": 0,
            "rmsg": "",
            "data": {
                "cookie": "{\"paging_key\":null,\"offset\":2}",
                "isEnd": 1,
                "downtownPngPrefix": "https://image-cdn.joinbudapp.com/downtown11071519/pr/teambud_downtown1_1/",
                "serverList": [{
                    "maxPlayer": 16,
                    "mapName": "Great Snowfield（Beta）",
                    "mapCover": "https://image-cdn.joinbudapp.com/downtown11071519/pr/teambud_downtown1_1/hangout.png",
                    "roomCode": "Dxel3MXlz",
                    "mapId": "teambud_downtown1_1",
                    "players": [{
                        "uid": "1592716446843670528",
                        "userName": "ID_8z8a24aljvqm",
                        "portraitUrl": "https://image-cdn.joinbudapp.com/peopleHeadImg/1592716446843670528coverImg.png"
                    }],
                    "roomPlayerNum": 1,
                    "PlayerUid": ["1592716446843670528"]
                }, {
                    "maxPlayer": 16,
                    "mapName": "Great Snowfield（Beta）",
                    "mapCover": "https://image-cdn.joinbudapp.com/downtown11071519/pr/teambud_downtown1_1/hangout.png",
                    "roomCode": "vLqeCdswI",
                    "mapId": "teambud_downtown1_1",
                    "players": [{
                        "uid": "1547085303167340544",
                        "userName": "engine001",
                        "portraitUrl": "https://image-cdn.joinbudapp.com/UgcImage/1547085303167340544/Profile1547085303167340544_1658499307.png"
                    }],
                    "roomPlayerNum": 1,
                    "PlayerUid": ["1547085303167340544"]
                }]
            },
            "requestId": "pr-cdqbuepm59d9odjjahi0"
        }
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
        down_town_room['mapCover'] = "https://image-cdn.joinbudapp.com/downtown11071519/pr/teambud_downtown1_1/hangout.png"
        down_town_room['mapId'] = "teambud_downtown1_1"
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
