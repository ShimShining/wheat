# -*- coding: utf-8 -*-
"""
@Author: shining
@File: ugc_map.py
@Date: 2022/4/14 4:40 下午
@Version: python 3.10
@Describe:
ugc模版列表
设置地图/素材/衣服/space
地图/素材/衣服/space草稿列表
地图/素材/衣服/space发布列表
地图/素材/衣服/space详情
"""
from proj.BPServiceTest.business.bp_service import BPService


class UGCMap(BPService):

    def get_ugc_templates(self, uid, **kwargs):

        """
        获取ugc模版列表
        :return:
        """
        path = ""

        h = {
            "uid": uid
        }
        params = {
        }
        req = {
            "name": "获取ugc模板列表",
            "path": path,
            "headers": h,
            "params": params
        }
        r = self.bp_get(req, **kwargs)
        return r.json()

    def publish_ugc_draft(self, uid, **kwargs):

        path = ""
        h = {
            "uid": uid,
        }

        j = {
        }
        req = {
            "name": "设置地图/素材/衣服/space草稿，发布",
            "path": path,
            "headers": h,
            "json": j
        }
        r = self.bp_post(req, **kwargs)
        return r.json()

    def set_like_ugc_map(self, uid, data_type, operation_type, map_info, **kwargs):

        path = ""
        h = {
            "uid": uid,
        }
        map_info['dataType'] = int(data_type)
        j = {
            "mapInfo": map_info,
            "operationType": operation_type,
        }
        req = {
            "name": "设置ugc地图/素材/衣服/space 点赞/收藏/置顶",
            "path": path,
            "headers": h,
            "json": j
        }
        r = self.bp_post(req, **kwargs)
        return r.json()

    def delete_ugc_draft(self, uid, map_info, **kwargs):

        path = ""
        h = {
            "uid": uid
        }
        j = {
            "mapInfo": map_info,
            "operationType": 1
        }
        req = {
            "name": "map-set接口删除草稿",
            "path": path,
            "headers": h,
            "json": j
        }
        r = self.bp_post(req, **kwargs)
        return r.json()

    def get_draft_create_list(self, uid, **kwargs):

        path = ""
        h = {
            "uid": uid
        }
        params = {
        }
        req = {
            "name": "获取草稿列表",
            "path": path,
            "headers": h,
            "params": params
        }
        r = self.bp_get(req, **kwargs)
        return r.json()

    def get_ugc_publish_list(self, uid, to_uid, **kwargs):

        path = ""
        h = {
            "uid": uid
        }
        # name = "获取草稿列表"
        params = {
            "toUid": to_uid,
        }

        req = {
            "name": "获取草稿列表",
            "path": path,
            "headers": h,
            "params": params
        }
        # req = self.handle_req_params(locals())
        r = self.bp_get(req, **kwargs)
        return r.json()

    def get_ugc_detail_info(self, uid, map_id, **kwargs):

        path = ""
        h = {
            "uid": uid
        }
        params = {
        }
        req = {
            "name": "获取地图/素材/衣服/space详情数据",
            "path": path,
            "headers": h,
            "params": params
        }
        r = self.bp_get(req, **kwargs)
        return r.json()

    def get_studio_list(self, uid, **kwargs):

        path = ""
        name = 'Tab-Studio列表'
        h = {"uid": uid}

        req = self.handle_req_params(locals())
        r = self.bp_get(req, **kwargs)
        return r.json()

    def get_ugc_favorite_list(self, uid, **kwargs):

        path = ""
        h = {
            "uid": uid
        }
        params = {
        }

        req = {
            "name": "获取点赞收藏列表",
            "path": path,
            "headers": h,
            "params": params
        }
        r = self.bp_get(req, **kwargs)
        return r.json()

    def get_hashtag_list(self, uid, **kwargs):
        path = ""
        h = {
            "uid": uid
        }
        params = {
        }

        req = {
            "name": "获取话题列表",
            "path": path,
            "headers": h,
            "params": params
        }
        r = self.bp_get(req, **kwargs)
        return r.json()

    def get_hashtag_info(self, uid, **kwargs):
        path = ""
        h = {
            "uid": uid
        }
        params = {
        }

        req = {
            "name": "获取话题详情",
            "path": path,
            "headers": h,
            "params": params
        }
        r = self.bp_get(req, **kwargs)
        return r.json()

    def get_quote_list(self, uid, **kwargs):
        path = ""
        h = {
            "uid": uid
        }
        params = {}

        req = {
            "name": "引用素材、dc衣服列表",
            "path": path,
            "headers": h,
            "params": params
        }
        r = self.bp_get(req, **kwargs)
        return r.json()

    def get_photo_list(self, uid, **kwargs):
        path = ""
        h = {
            "uid": uid
        }
        params = {
        }
        req = {
            "name": "地图相册列表",
            "path": path,
            "headers": h,
            "params": params
        }
        r = self.bp_get(req, **kwargs)
        return r.json()


if __name__ == '__main__':
    u = UGCMap()
    u.get_ugc_publish_list("uid", "to_uid")
