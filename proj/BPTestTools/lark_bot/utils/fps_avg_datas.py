# -*- coding: utf-8 -*-
"""
@Author: shining
@File: fps_avg_datas.py
@Date: 2022/4/12 4:25 下午
@Version: python 3.10
@Describe:
"""
import datetime
from online_monitor.big_query.big_query import BigQuery


def handle_avg_fps_intraday(fps_info):
    dat = fps_info
    sql = fr"""  #Standard-SQL
                  #UDF for event parameters
                CREATE TEMP FUNCTION
                  paramValueByKey(k STRING,
                    params ARRAY<STRUCT<key STRING,
                    value STRUCT<string_value STRING,
                    int_value INT64,
                    float_value FLOAT64,
                    double_value FLOAT64 >>>) AS ( (
                    SELECT
                      x.value
                    FROM
                      UNNEST(params) x
                    WHERE
                      x.key=k) );
                  #UDF for user properties
                CREATE TEMP FUNCTION
                  propertyValueByKey(k STRING,
                    properties ARRAY<STRUCT<key STRING,
                    value STRUCT<value STRUCT<string_value STRING,
                    int_value INT64,
                    float_value FLOAT64,
                    double_value FLOAT64>,
                    set_timestamp_usec INT64,
                    INDEX INT64 > >>) AS ( (
                    SELECT
                      x.value.value
                    FROM
                      UNNEST(properties) x
                    WHERE
                      x.key=k) );
                  #Query the sample dataset, unnesting the events and turn 'api_version', 'round' and 'type_of_game' into columns
                WITH
                  ta AS (
                  SELECT
                    user_id,
                    event_name,
                    event_timestamp,
                    FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP_MICROS(event_timestamp),'Asia/Shanghai') AS time_hour,
                    platform,
                    paramValueByKey('seq',
                      event_params).string_value AS seq,
                    paramValueByKey('mapId',
                      event_params).string_value AS mapId,
                    paramValueByKey('scene',
                      event_params).int_value AS scene,
                    paramValueByKey('subType',
                      event_params).int_value AS subType,
                    paramValueByKey('fps',
                      event_params).int_value AS fps
                  FROM
                    -- 需要修改结尾的日期，改成想要查询的日期格式参照如下
                    `BP-.events_intraday_{dat}`
                  WHERE
                    event_name = 'unity_avg_fps'
                    AND (app_info.id not like '%.debug' and app_info.id not like '%.master')
                    and paramValueByKey('mapId',event_params).string_value like '%_1'
                    -- AND paramValueByKey('scene',event_params).int_value =1
                    -- AND paramValueByKey('subType',event_params).int_value=2 
                    ),
                  fps_res AS(
                  SELECT
                    seq,
                    mapId,
                    platform,
                    MAX(fps) AS fps
                  FROM
                    ta
                  GROUP BY
                    seq,
                    mapId,
                    platform)
                SELECT
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    fps_res) AS total,
                  (
                  SELECT
                    AVG(fps)
                  FROM
                    fps_res) AS avg_fps,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    fps_res
                  WHERE
                    platform='ANDROID') AS android_total,
                  (
                  SELECT
                    AVG(fps)
                  FROM
                    fps_res
                  WHERE
                    platform='ANDROID') AS android_avg_fps,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    fps_res
                  WHERE
                    platform='IOS') AS ios_total,
                  (
                  SELECT
                    AVG(fps)
                  FROM
                    fps_res
                  WHERE
                    platform='IOS') AS ios_avg_fps"""
    # print(sql)
    return sql

def handle_avg_fps(fps_info):

    dat= fps_info
    sql = fr"""  #Standard-SQL
                  #UDF for event parameters
                CREATE TEMP FUNCTION
                  paramValueByKey(k STRING,
                    params ARRAY<STRUCT<key STRING,
                    value STRUCT<string_value STRING,
                    int_value INT64,
                    float_value FLOAT64,
                    double_value FLOAT64 >>>) AS ( (
                    SELECT
                      x.value
                    FROM
                      UNNEST(params) x
                    WHERE
                      x.key=k) );
                  #UDF for user properties
                CREATE TEMP FUNCTION
                  propertyValueByKey(k STRING,
                    properties ARRAY<STRUCT<key STRING,
                    value STRUCT<value STRUCT<string_value STRING,
                    int_value INT64,
                    float_value FLOAT64,
                    double_value FLOAT64>,
                    set_timestamp_usec INT64,
                    INDEX INT64 > >>) AS ( (
                    SELECT
                      x.value.value
                    FROM
                      UNNEST(properties) x
                    WHERE
                      x.key=k) );
                  #Query the sample dataset, unnesting the events and turn 'api_version', 'round' and 'type_of_game' into columns
                WITH
                  ta AS (
                  SELECT
                    user_id,
                    event_name,
                    event_timestamp,
                    FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP_MICROS(event_timestamp),'Asia/Shanghai') AS time_hour,
                    platform,
                    paramValueByKey('seq',
                      event_params).string_value AS seq,
                    paramValueByKey('mapId',
                      event_params).string_value AS mapId,
                    paramValueByKey('scene',
                      event_params).int_value AS scene,
                    paramValueByKey('subType',
                      event_params).int_value AS subType,
                    paramValueByKey('fps',
                      event_params).int_value AS fps
                  FROM
                    -- 需要修改结尾的日期，改成想要查询的日期格式参照如下
                    `BP-.events_{dat}`
                  WHERE
                    event_name = 'unity_avg_fps'
                    AND (app_info.id not like '%.debug' and app_info.id not like '%.master')
                    and paramValueByKey('mapId',event_params).string_value like '%_1'
                    -- AND paramValueByKey('scene',event_params).int_value =1
                    -- AND paramValueByKey('subType',event_params).int_value=2 
                      ),
                  fps_res AS(
                  SELECT
                    seq,
                    mapId,
                    platform,
                    MAX(fps) AS fps
                  FROM
                    ta
                  GROUP BY
                    seq,
                    mapId,
                    platform)
                SELECT
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    fps_res) AS total,
                  (
                  SELECT
                    AVG(fps)
                  FROM
                    fps_res) AS avg_fps,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    fps_res
                  WHERE
                    platform='ANDROID') AS android_total,
                  (
                  SELECT
                    AVG(fps)
                  FROM
                    fps_res
                  WHERE
                    platform='ANDROID') AS android_avg_fps,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    fps_res
                  WHERE
                    platform='IOS') AS ios_total,
                  (
                  SELECT
                    AVG(fps)
                  FROM
                    fps_res
                  WHERE
                    platform='IOS') AS ios_avg_fps"""
    # print(sql)
    return sql

def handle_ctop_params_intraday(ctop_info):
    """
    sql拼装
    :param rate_info:
    :return:
    """
    # TODO 后续改用模板替换实现
    dat= ctop_info
    sql_template = fr"""WITH
                  callUnity AS (
                  SELECT
                    user_id,
                    event_timestamp,
                    event_params.value.string_value AS mapId,
                    event_name,
                    platform,
                    FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP_MICROS(event_timestamp),'Asia/Shanghai') AS time_hour,
                  FROM
                    `BP-.events_intraday_{dat}` AS T
                  CROSS JOIN
                    T.event_params
                  WHERE
                    event_name = 'BP_call_unity'
                    AND event_params.key = 'mapId'
                    AND (event_params.value.string_value LIKE '%_1' OR event_params.value.string_value LIKE '%_7')
                    --AND event_timestamp > 1643068800000000
                    AND (app_info.id not like '%.debug' and app_info.id not like '%.master')),
                  framestep AS (
                  SELECT
                    event_name AS event_name_1,
                    platform,
                    MIN(event_timestamp) AS first_startFrameStep,
                    event_params.value.string_value AS seq
                  FROM
                    `BP-.events_intraday_{dat}` AS T
                  CROSS JOIN
                    T.event_params
                  WHERE
                    event_name = 'unity_startFrameStep_recv'
                    AND event_params.key = 'seq'
                    AND (app_info.id not like '%.debug' and app_info.id not like '%.master')
                  GROUP BY
                    seq,
                    event_name,
                    platform)
                SELECT
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    callUnity
                  WHERE
                    callUnity.event_name = 'BP_call_unity') AS total_call_unity,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    framestep)AS success_enter,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    callUnity
                  WHERE
                    callUnity.event_name = 'BP_call_unity'
                    AND platform='ANDROID') AS android_total_call_unity,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    framestep
                  WHERE
                    platform='ANDROID')AS android_success_enter,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    callUnity
                  WHERE
                    callUnity.event_name = 'BP_call_unity'
                    AND platform='IOS') AS ios_total_call_unity,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    framestep
                  WHERE
                    platform='IOS')AS ios_success_enter"""
    return sql_template

def handle_ctop_params(ctop_info):
    """
    sql拼装
    :param rate_info:
    :return:
    """
    # TODO 后续改用模板替换实现
    dat= ctop_info
    sql_template = fr"""WITH
                  callUnity AS (
                  SELECT
                    user_id,
                    event_timestamp,
                    event_params.value.string_value AS mapId,
                    event_name,
                    platform,
                    FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP_MICROS(event_timestamp),'Asia/Shanghai') AS time_hour,
                  FROM
                    `BP-.events_{dat}` AS T
                  CROSS JOIN
                    T.event_params
                  WHERE
                    event_name = 'BP_call_unity'
                    AND event_params.key = 'mapId'
                    AND (event_params.value.string_value LIKE '%_1' OR event_params.value.string_value LIKE '%_7')
                    --AND event_timestamp > 1643068800000000
                    AND (app_info.id not like '%.debug' and app_info.id not like '%.master')),
                  framestep AS (
                  SELECT
                    event_name AS event_name_1,
                    platform,
                    MIN(event_timestamp) AS first_startFrameStep,
                    event_params.value.string_value AS seq
                  FROM
                    `BP-.events_{dat}` AS T
                  CROSS JOIN
                    T.event_params
                  WHERE
                    event_name = 'unity_startFrameStep_recv'
                    AND event_params.key = 'seq'
                    AND (app_info.id not like '%.debug' and app_info.id not like '%.master')
                  GROUP BY
                    seq,
                    event_name,
                    platform)
                SELECT
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    callUnity
                  WHERE
                    callUnity.event_name = 'BP_call_unity') AS total_call_unity,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    framestep)AS success_enter,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    callUnity
                  WHERE
                    callUnity.event_name = 'BP_call_unity'
                    AND platform='ANDROID') AS android_total_call_unity,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    framestep
                  WHERE
                    platform='ANDROID')AS android_success_enter,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    callUnity
                  WHERE
                    callUnity.event_name = 'BP_call_unity'
                    AND platform='IOS') AS ios_total_call_unity,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    framestep
                  WHERE
                    platform='IOS')AS ios_success_enter"""
    return sql_template

def handle_enter_time_intraday(info):

    dat= info

    sql = fr"""  #Standard-SQL
              #UDF for event parameters
            CREATE TEMP FUNCTION
              paramValueByKey(k STRING,
                params ARRAY<STRUCT<key STRING,
                value STRUCT<string_value STRING,
                int_value INT64,
                float_value FLOAT64,
                double_value FLOAT64 >>>) AS ( (
                SELECT
                  x.value
                FROM
                  UNNEST(params) x
                WHERE
                  x.key=k) );
              #UDF for user properties
            CREATE TEMP FUNCTION
              propertyValueByKey(k STRING,
                properties ARRAY<STRUCT<key STRING,
                value STRUCT<value STRUCT<string_value STRING,
                int_value INT64,
                float_value FLOAT64,
                double_value FLOAT64>,
                set_timestamp_usec INT64,
                INDEX INT64 > >>) AS ( (
                SELECT
                  x.value.value
                FROM
                  UNNEST(properties) x
                WHERE
                  x.key=k) );
              #Query the sample dataset, unnesting the events and turn 'api_version', 'round' and 'type_of_game' into columns
            WITH
              ta AS (
              SELECT
                user_id,
                event_name,
                event_timestamp,
                platform,
                -- propertyValueByKey('api_version', user_dim.user_properties).string_value AS api_version,
                paramValueByKey('seq',
                  event_params).string_value AS seq,
                paramValueByKey('mapId',
                  event_params).string_value AS mapId,
                paramValueByKey('scene',
                  event_params).int_value AS scene,
                paramValueByKey('subType',
                  event_params).int_value AS subType,
                paramValueByKey('roomMode',
                  event_params).int_value AS roomMode
              FROM
                `BP-.events_intraday_{dat}`
                -- ,
                -- UNNEST(event_params) as event
              WHERE
                event_name = 'BP_call_unity'
                -- event_name IN('BP_call_unity',
                  --   'unity_startFrameStep_recv' )
                AND (app_info.id not like '%.debug' and app_info.id not like '%.master')),
              tb AS (
              SELECT
                user_id,
                event_name,
                MIN(event_timestamp) AS event_timestamp,
                platform,
                -- propertyValueByKey('api_version', user_dim.user_properties).string_value AS api_version,
                paramValueByKey('seq',
                  event_params).string_value AS seq,
                paramValueByKey('mapId',
                  event_params).string_value AS mapId,
                paramValueByKey('scene',
                  event_params).int_value AS scene,
                paramValueByKey('subType',
                  event_params).int_value AS subType,
                paramValueByKey('roomMode',
                  event_params).int_value AS roomMode
              FROM
                `BP-.events_intraday_{dat}`
                -- ,
                -- UNNEST(event_params) as event
              WHERE
                event_name = 'unity_startFrameStep_recv'
                -- event_name IN('BP_call_unity',
                  --   'unity_startFrameStep_recv' )
                AND (app_info.id not like '%.debug' and app_info.id not like '%.master')
              GROUP BY
                seq,
                user_id,
                event_name,
                platform,
                mapId,
                scene,
                subType,
                roomMode),
              cost AS (
              SELECT
                ta.user_id,
                ta.event_name,
                tb.event_name,
                (tb.event_timestamp - ta.event_timestamp) AS enter_cost,
                ta.mapId,
                ta.scene,
                ta.subType,
                ta.roomMode,
                ta.event_timestamp,
                tb.event_timestamp,
                ta.platform
              FROM
                ta
              INNER JOIN
                tb
              ON
                ta.seq = tb.seq
              WHERE
                ta.scene=1
                AND ta.subType=2
                AND tb.scene=1
                AND tb.subType=2)
            SELECT
              (
              SELECT
                AVG(enter_cost)/1000000
              FROM
                cost
              WHERE
                enter_cost >= 0
                AND enter_cost < 300000000)AS enter_time,
              (
              SELECT
                COUNT(*)
              FROM
                cost
              WHERE
                enter_cost >= 0
                AND enter_cost < 300000000)AS total_enter,
              (
              SELECT
                AVG(enter_cost)/1000000
              FROM
                cost
              WHERE
                platform = 'ANDROID'
                AND enter_cost >= 0
                AND enter_cost < 300000000)AS android_enter_time,
              (
              SELECT
                COUNT(*)
              FROM
                cost
              WHERE
                platform = 'ANDROID'
                AND enter_cost >= 0
                AND enter_cost < 300000000)AS android_total_enter,
              (
              SELECT
                AVG(enter_cost)/1000000
              FROM
                cost
              WHERE
                platform = 'IOS'
                AND enter_cost >= 0
                AND enter_cost < 300000000)AS ios_enter_time,
              (
              SELECT
                COUNT(*)
              FROM
                cost
              WHERE
                platform = 'IOS'
                AND enter_cost >= 0
                AND enter_cost < 300000000)AS ios_total_enter"""
    return sql

def handle_enter_time(info):

    dat = info

    sql = fr"""  #Standard-SQL
              #UDF for event parameters
            CREATE TEMP FUNCTION
              paramValueByKey(k STRING,
                params ARRAY<STRUCT<key STRING,
                value STRUCT<string_value STRING,
                int_value INT64,
                float_value FLOAT64,
                double_value FLOAT64 >>>) AS ( (
                SELECT
                  x.value
                FROM
                  UNNEST(params) x
                WHERE
                  x.key=k) );
              #UDF for user properties
            CREATE TEMP FUNCTION
              propertyValueByKey(k STRING,
                properties ARRAY<STRUCT<key STRING,
                value STRUCT<value STRUCT<string_value STRING,
                int_value INT64,
                float_value FLOAT64,
                double_value FLOAT64>,
                set_timestamp_usec INT64,
                INDEX INT64 > >>) AS ( (
                SELECT
                  x.value.value
                FROM
                  UNNEST(properties) x
                WHERE
                  x.key=k) );
              #Query the sample dataset, unnesting the events and turn 'api_version', 'round' and 'type_of_game' into columns
            WITH
              ta AS (
              SELECT
                user_id,
                event_name,
                event_timestamp,
                platform,
                -- propertyValueByKey('api_version', user_dim.user_properties).string_value AS api_version,
                paramValueByKey('seq',
                  event_params).string_value AS seq,
                paramValueByKey('mapId',
                  event_params).string_value AS mapId,
                paramValueByKey('scene',
                  event_params).int_value AS scene,
                paramValueByKey('subType',
                  event_params).int_value AS subType,
                paramValueByKey('roomMode',
                  event_params).int_value AS roomMode
              FROM
                `BP-.events_{dat}`
                -- ,
                -- UNNEST(event_params) as event
              WHERE
                event_name = 'BP_call_unity'
                -- event_name IN('BP_call_unity',
                  --   'unity_startFrameStep_recv' 
                AND (app_info.id not like '%.debug' and app_info.id not like '%.master')),
              tb AS (
              SELECT
                user_id,
                event_name,
                MIN(event_timestamp) AS event_timestamp,
                platform,
                -- propertyValueByKey('api_version', user_dim.user_properties).string_value AS api_version,
                paramValueByKey('seq',
                  event_params).string_value AS seq,
                paramValueByKey('mapId',
                  event_params).string_value AS mapId,
                paramValueByKey('scene',
                  event_params).int_value AS scene,
                paramValueByKey('subType',
                  event_params).int_value AS subType,
                paramValueByKey('roomMode',
                  event_params).int_value AS roomMode
              FROM
                `BP-.events_{dat}`
                -- ,
                -- UNNEST(event_params) as event
              WHERE
                event_name = 'unity_startFrameStep_recv'
                -- event_name IN('BP_call_unity',
                  --   'unity_startFrameStep_recv' )
                AND (app_info.id not like '%.debug' and app_info.id not like '%.master')
              GROUP BY
                seq,
                user_id,
                event_name,
                platform,
                mapId,
                scene,
                subType,
                roomMode),
              cost AS (
              SELECT
                ta.user_id,
                ta.event_name,
                tb.event_name,
                (tb.event_timestamp - ta.event_timestamp) AS enter_cost,
                ta.mapId,
                ta.scene,
                ta.subType,
                ta.roomMode,
                ta.event_timestamp,
                tb.event_timestamp,
                ta.platform
              FROM
                ta
              INNER JOIN
                tb
              ON
                ta.seq = tb.seq
              WHERE
                ta.scene=1
                AND ta.subType=2
                AND tb.scene=1
                AND tb.subType=2)
            SELECT
              (
              SELECT
                AVG(enter_cost)/1000000
              FROM
                cost
              WHERE
                enter_cost >= 0
                AND enter_cost < 300000000)AS enter_time,
              (
              SELECT
                COUNT(*)
              FROM
                cost
              WHERE
                enter_cost >= 0
                AND enter_cost < 300000000)AS total_enter,
              (
              SELECT
                AVG(enter_cost)/1000000
              FROM
                cost
              WHERE
                platform = 'ANDROID'
                AND enter_cost >= 0
                AND enter_cost < 300000000)AS android_enter_time,
              (
              SELECT
                COUNT(*)
              FROM
                cost
              WHERE
                platform = 'ANDROID'
                AND enter_cost >= 0
                AND enter_cost < 300000000)AS android_total_enter,
              (
              SELECT
                AVG(enter_cost)/1000000
              FROM
                cost
              WHERE
                platform = 'IOS'
                AND enter_cost >= 0
                AND enter_cost < 300000000)AS ios_enter_time,
              (
              SELECT
                COUNT(*)
              FROM
                cost
              WHERE
                platform = 'IOS'
                AND enter_cost >= 0
                AND enter_cost < 300000000)AS ios_total_enter"""
    return sql

def get_date_list(start_date, end_date):

    date_list = []
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    date_list.append(start_date.strftime('%Y-%m-%d'))
    while start_date < end_date:
        start_date += datetime.timedelta(days=1)
        date_list.append(start_date.strftime('%Y-%m-%d'))
    return date_list


def get_res_data():

    intraday_list = get_date_list('2022-02-18', '2022-03-22')
    date_list = get_date_list('2022-03-23', '2022-04-17')
    big_query = BigQuery(r"./cred/google_application_credentials.json")
    res_a =[]
    res_b = []
    res = []
    for dat in intraday_list:
        day = {}
        day['date'] = dat
        dat = dat.replace('-', '')
        sql = handle_ctop_params_intraday(dat)

        # r = big_query.get_avg_fps_info(sql)
        r = big_query.get_click_to_play_pv(sql)
        day['total_rate'] = r[0]
        day['total_enter'] = r[1]
        day['total_success'] = r[2]
        day['android_rate'] = r[3]
        day['android_enter'] = r[4]
        day['android_success'] = r[5]
        day['ios_rate'] = r[6]
        day['ios_enter'] = r[7]
        day['ios_success'] = r[8]
        res.append(day)

    for dat in date_list:
        day = {}
        day['date'] = dat
        dat = dat.replace('-', '')
        sql = handle_ctop_params(dat)

        # r = big_query.get_avg_fps_info(sql)
        r = big_query.get_click_to_play_pv(sql)
        day['total_rate'] = r[0]
        day['total_enter'] = r[1]
        day['total_success'] = r[2]
        day['android_rate'] = r[3]
        day['android_enter'] = r[4]
        day['android_success'] = r[5]
        day['ios_rate'] = r[6]
        day['ios_enter'] = r[7]
        day['ios_success'] = r[8]
        res.append(day)
    print(res)
    return res


def get_enter_time():
    intraday_list = get_date_list('2022-04-23', '2022-04-24')
    date_list = get_date_list('2022-04-19', '2022-04-22')
    big_query = BigQuery(r"./cred/google_application_credentials.json")

    res = []
    for dat in intraday_list:
        day = {}
        day['date'] = dat
        dat = dat.replace('-', '')
        sql = handle_enter_time_intraday(dat)

        # r = big_query.get_avg_fps_info(sql)
        r = big_query.get_avg_enter_room_time(sql)
        day['total_time'] = r[0]
        day['android_enter'] = r[2]
        day['ios_success'] = r[4]
        res.append(day)

    for dat in date_list:
        day = {}
        day['date'] = dat
        dat = dat.replace('-', '')
        sql = handle_enter_time(dat)

        # r = big_query.get_avg_fps_info(sql)
        r = big_query.get_avg_enter_room_time(sql)
        day['total_time'] = r[0]
        day['android_enter'] = r[2]
        day['ios_success'] = r[4]
        res.append(day)
    print(res)
    return res


if __name__ == '__main__':

    res = get_enter_time()
    print(res)


