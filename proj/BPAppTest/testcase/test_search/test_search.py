# -*- coding: utf-8 -*-
"""
@Author: shining
@File: test_search.py
@Date: 2022/12/1 3:15 下午
@Version: python 3.9
@Describe: 搜索测试类
"""
import allure
import pytest

from testcase.BP_app_test import BPAppTest
from utils.yaml_handler import YAMLHandler as yh


@pytest.mark.smoking
@pytest.mark.search
@allure.feature("搜索服务")
class TestSearch(BPAppTest):

    @allure.story("首页搜索")
    def test_search_target_user_success(self, login: "HomePage"):
        """
        测试首页搜索对应用户成功
        :return:
        """
        allure.dynamic.title("首页搜索指定用户成功")
        home = login
        # 读入data下对应yaml文件的测试数据
        search_word = yh.case_data('search', case_name="search_target_user_success").search_word
        self.log.info(f"test_search_target_user_success.search_word={search_word}")
        home.goto_search_input_page().goto_search_landing_page(search_word=search_word).\
            assert_search_user_in_result(search_word=search_word).goto_home_page().assert_is_home_page()

