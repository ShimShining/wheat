# -*- coding: utf-8 -*-
"""
@Author: shining
@File: draw.py
@Date: 2022/12/28 5:59 下午
@Version: python 3.9
@Describe:
"""
import pyecharts.options as opts
from pyecharts import types
from pyecharts.charts import Line


class Draw:

    @staticmethod
    def generate_rate_trend(rate_data) -> Line:

        times = [int(d[0]) for d in rate_data]
        reward_type_no_rate = [round(float(d[1]) * 100, 2) for d in rate_data]
        reward_type_prop_rate = [round(float(d[2]) * 100, 2) for d in rate_data]
        reward_type_clothes_purple_rate = [round(float(d[3]) * 100, 2) for d in rate_data]
        reward_type_clothes_blue_rate = [round(float(d[4]) * 100, 2) for d in rate_data]
        reward_type_gold_rate = [round(float(d[5]) * 100, 2) for d in rate_data]
        reward_type_souvenir_rate = [round(float(d[6]) * 100, 2) for d in rate_data]
        reward_type_potion_rate = [round(float(d[7]) * 100, 2) for d in rate_data]
        c = (
            Line()
                .add_xaxis(times)
                .add_yaxis(series_name="无奖品", y_axis=reward_type_no_rate, label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(
                               data=[
                                   # opts.MarkPointItem(name='min', type_='min'),
                                   # opts.MarkPointItem(name='max', type_='max'),
                                   opts.MarkPointItem(name='average', type_='average')],
                               label_opts=opts.LabelOpts(position="top", distance=-60))
                           )
                .add_yaxis(series_name="素材", y_axis=reward_type_prop_rate,
                           label_opts=opts.LabelOpts(is_show=False, position="top", distance=-15),
                           markpoint_opts=opts.MarkPointOpts(
                               data=[
                                   # opts.MarkPointItem(name='min', type_='min'),
                                   # opts.MarkPointItem(name='max', type_='max'),
                                   opts.MarkPointItem(name='average', type_='average')],
                               label_opts=opts.LabelOpts(position="top", distance=-70))
                           )
                .add_yaxis(series_name="紫色衣服", y_axis=reward_type_clothes_purple_rate, label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(
                               data=[
                                   # opts.MarkPointItem(name='min', type_='min'),
                                   # opts.MarkPointItem(name='max', type_='max'),
                                   opts.MarkPointItem(name='average', type_='average')],
                               label_opts=opts.LabelOpts(position="top", distance=3))
                           )
                .add_yaxis(series_name="蓝色衣服", y_axis=reward_type_clothes_blue_rate,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(
                               data=[
                                   # opts.MarkPointItem(name='min', type_='min'),
                                   # opts.MarkPointItem(name='max', type_='max'),
                                   opts.MarkPointItem(name='average', type_='average')],
                               label_opts=opts.LabelOpts(position="top", distance=3))
                           )
                .add_yaxis(series_name="金币", y_axis=reward_type_gold_rate,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(
                               data=[
                                   # opts.MarkPointItem(name='min', type_='min'),
                                   # opts.MarkPointItem(name='max', type_='max'),
                                   opts.MarkPointItem(name='average', type_='average')],
                               label_opts=opts.LabelOpts(position="top", distance=3))
                           )
                .add_yaxis(series_name="纪念品", y_axis=reward_type_souvenir_rate,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(
                               data=[
                                   # opts.MarkPointItem(name='min', type_='min'),
                                   # opts.MarkPointItem(name='max', type_='max'),
                                   opts.MarkPointItem(name='average', type_='average')],
                               label_opts=opts.LabelOpts(position="top", distance=3))
                           )
                .add_yaxis(series_name="药水", y_axis=reward_type_potion_rate,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(
                               data=[
                                   # opts.MarkPointItem(name='min', type_='min'),
                                   # opts.MarkPointItem(name='max', type_='max'),
                                   opts.MarkPointItem(name='average', type_='average')],
                               label_opts=opts.LabelOpts(position="top", distance=3))
                           )
                .set_global_opts(title_opts=opts.TitleOpts(title="扭蛋机奖品概率"),
                                 yaxis_opts=opts.AxisOpts(name='概率（%）'),
                                 xaxis_opts=opts.AxisOpts(name='抽奖次数')

                                 )
        )
        return c

    @staticmethod
    def generate_color_rate_trend(colors_data):
        times = [int(d[0]) for d in colors_data]
        orange_rate = [round(float(d[1]) * 100, 2) for d in colors_data]
        purple_rate = [round(float(d[2]) * 100, 2) for d in colors_data]
        blue_rate = [round(float(d[3]) * 100, 2) for d in colors_data]
        c = (
            Line()
                .add_xaxis(times)
                .add_yaxis(series_name="橙色球", y_axis=orange_rate, label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(
                               data=[
                                   # opts.MarkPointItem(name='min', type_='min'),
                                   # opts.MarkPointItem(name='max', type_='max'),
                                   opts.MarkPointItem(name='average', type_='average')],
                               label_opts=opts.LabelOpts(position="top", distance=-60))
                           )
                .add_yaxis(series_name="紫色球", y_axis=purple_rate,
                           label_opts=opts.LabelOpts(is_show=False, position="top", distance=-15),
                           markpoint_opts=opts.MarkPointOpts(
                               data=[
                                   # opts.MarkPointItem(name='min', type_='min'),
                                   # opts.MarkPointItem(name='max', type_='max'),
                                   opts.MarkPointItem(name='average', type_='average')],
                               label_opts=opts.LabelOpts(position="top", distance=-70))
                           )
                .add_yaxis(series_name="蓝色球", y_axis=blue_rate, label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(
                               data=[
                                   # opts.MarkPointItem(name='min', type_='min'),
                                   # opts.MarkPointItem(name='max', type_='max'),
                                   opts.MarkPointItem(name='average', type_='average')],
                               label_opts=opts.LabelOpts(position="top", distance=3))
                           )
                .set_global_opts(title_opts=opts.TitleOpts(title="扭蛋机球概率"),
                                 yaxis_opts=opts.AxisOpts(name='概率（%）'),
                                 xaxis_opts=opts.AxisOpts(name='抽奖次数')

                                 )
        )
        return c
