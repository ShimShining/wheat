# -*- coding: utf-8 -*-
"""
@Author: shining
@File: handle_sql.py
@Date: 2022/1/25 6:29 下午
@Version: python 3.10
@Describe:
"""
# import sys
from online_monitor.big_query.big_query import BigQuery


# sys.path.append("../")


class HandleSql:

    def __init__(self, sql_template=None):
        self.sql_template = sql_template

    @staticmethod
    def handle_ctop_params(ctop_info):
        """
        sql拼装
        :param rate_info:
        :return:
        """
        # TODO 后续改用模板替换实现
        _, version, table = ctop_info
        sql_template = fr"""  #Standard-SQL
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
                              callU AS (
                              SELECT
                                platform,
                                paramValueByKey('seq',
                                  event_params).string_value AS seq,
                                paramValueByKey('scene',
                                  event_params).int_value AS scene,
                                paramValueByKey('subType',
                                  event_params).int_value AS subType,
                              FROM
                                `{table}`
                              WHERE
                                event_name = 'BP_call_unity'
                                AND (paramValueByKey('scene',
                                    event_params).int_value = 1
                                  OR paramValueByKey('scene',
                                    event_params).int_value = 6)
                                AND paramValueByKey('subType',
                                  event_params).int_value = 2 
                                AND app_info.version = '{version}'
                                AND (app_info.id NOT LIKE '%.debug%'
                                  AND app_info.id NOT LIKE '%.master%') ),
                              framestep AS (
                              SELECT
                                MIN(event_timestamp) AS event_timestamp,
                                platform,
                                -- propertyValueByKey('api_version', user_dim.user_properties).string_value AS api_version,
                                paramValueByKey('seq',
                                  event_params).string_value AS seq,
                                paramValueByKey('scene',
                                  event_params).int_value AS scene,
                                paramValueByKey('subType',
                                  event_params).int_value AS subType,
                              FROM
                                `{table}`
                              WHERE
                                event_name = 'unity_enterRoom_rsp'
                                AND (app_info.id NOT LIKE '%.debug%'
                                  AND app_info.id NOT LIKE '%.master%')
                                AND app_info.version = '{version}' 
                                --AND event_timestamp > 1654061400000000  and event_timestamp < 1654086600000000
                              GROUP BY
                                seq,
                                platform,
                                scene,
                                subType ),
                            quit as (
                              SELECT
                                platform,
                                paramValueByKey('state',event_params).string_value AS state,
                                paramValueByKey('seq',event_params).string_value AS quit_seq
                              FROM
                                `{table}`
                              WHERE
                                event_name = 'quit_unity'
                                  --AND event_timestamp > 1654061400000000  and event_timestamp < 1654086600000000
                                AND app_info.version = '{version}'
                                AND (app_info.id NOT LIKE '%.debug%'
                                  AND app_info.id NOT LIKE '%.master%')
                            ),
                              callUnity AS (
                              SELECT
                                seq,
                                platform,
                                COUNT(*) AS cnt
                              FROM
                                callU
                              GROUP BY
                                seq,
                                platform
                              ORDER BY
                                COUNT(*) DESC )
                            SELECT
                              (
                              SELECT
                                COUNT(*)
                              FROM
                                callUnity ) AS total_call_unity,
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
                                platform='ANDROID') AS android_total_call_unity,
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
                                platform='IOS') AS ios_total_call_unity,
                              (
                              SELECT
                                COUNT(*)
                              FROM
                                framestep
                              WHERE
                                platform='IOS')AS ios_success_enter,
                               -- (
                              -- SELECT
                                -- COUNT(*)
                              -- FROM
                                -- quit)AS total_quit,
                             (
                              SELECT
                                -- COUNT(*)
                                COUNT(distinct  quit.quit_seq)
                              FROM
                                quit
                              WHERE
                                platform='IOS')AS ios_quit,
                                 (
                              SELECT
                                -- COUNT(*)
                                COUNT(distinct  quit.quit_seq)
                              FROM
                                quit
                              WHERE
                                platform='ANDROID')AS android_quit"""
        return sql_template

    @staticmethod
    def handle_avg_fps(fps_info):
        dat, version, table = fps_info
        avg_fps_app_info = HandleSql.handle_versions_condition(version)

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
                        `{table}`
                      WHERE
                        event_name = 'unity_avg_fps'
                        AND {avg_fps_app_info}
                        AND (app_info.id not like '%.debug%' and app_info.id not like '%.master%')
                        AND (paramValueByKey('scene',event_params).int_value =1 OR paramValueByKey('scene',event_params).int_value =6)
                        AND paramValueByKey('subType',
                          event_params).int_value=2 ),
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
        # raise ValueError("暂停")
        return sql

    @staticmethod
    def handle_30_60_avg_fps(avg_30_60_fps_info, full_fps=30):
        dat, version, table = avg_30_60_fps_info
        avg_30_60_fps_app_info = HandleSql.handle_versions_condition(version)
        max_30_60_sql = fr"""  #Standard-SQL
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
                        `{table}`
                      WHERE
                        event_name = 'unity_avg_fps'
                        AND {avg_30_60_fps_app_info}  
                    AND (app_info.id not like '%.debug%' and app_info.id not like '%.master%')
                        AND (paramValueByKey('scene',
                            event_params).int_value =1
                          OR paramValueByKey('scene',
                            event_params).int_value =6)
                        AND paramValueByKey('subType',
                          event_params).int_value=2 
                        AND paramValueByKey('targetFrameRate',
                          event_params).int_value={full_fps}),
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
                        platform='IOS') AS ios_avg_fps
        """
        return max_30_60_sql

    @staticmethod
    def handle_enter_time(enter_time_info):
        dat, version, table = enter_time_info
        avg_enter_time_app_info = HandleSql.handle_versions_condition(version)
        sql = fr"""#Standard-SQL
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
                    `{table}`
                    -- ,
                    -- UNNEST(event_params) as event
                  WHERE
                    event_name = 'BP_call_unity'
                    -- event_name IN('BP_call_unity',
                      --   'unity_startFrameStep_recv' )
                    AND {avg_enter_time_app_info}
                    AND (app_info.id not like '%.debug%' and app_info.id not like '%.master%')),
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
                    `{table}`
                    -- ,
                    -- UNNEST(event_params) as event
                  WHERE
                    event_name = 'unity_startFrameStep_recv'
                    -- event_name IN('BP_call_unity',
                      --   'unity_startFrameStep_recv' )
                    AND {avg_enter_time_app_info}
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

    @staticmethod
    def handle_ab_cost(ab_cost_info):
        dat, version, table = ab_cost_info
        sql = fr"""WITH
                      testA AS (
                      SELECT
                        event_name,
                        event_timestamp,
                        platform,
                        event_params.value.string_value AS seq
                      FROM
                        `{table}` AS T
                      CROSS JOIN
                        T.event_params
                      WHERE
                        event_name = 'unity_startOffline'
                        AND event_params.key = 'seq'
                        AND app_info.version = '{version}'
                        AND (app_info.id not like '%.debug' and app_info.id not like '%.master')),
                    ab_cost as (SELECT
                      *
                    FROM (
                      SELECT
                        (first_startFrameStep-event_timestamp)AS cost,
                        platform
                      FROM (
                        SELECT
                          event_name AS event_name_1,
                          MIN(event_timestamp) AS first_startFrameStep,
                          platform as p,
                          event_params.value.string_value AS seq
                        FROM
                          `{table}` AS T
                        CROSS JOIN
                          T.event_params
                        WHERE
                          event_name = 'unity_endOffline'
                          AND event_params.key = 'seq'
                          AND app_info.version = '{version}'
                          AND (app_info.id not like '%.debug%' and app_info.id not like '%.master%')
                        GROUP BY
                          seq,
                          event_name,
                          platform ) AS b
                      INNER JOIN
                        testA
                      ON
                        testA.seq = b.seq )
                    WHERE
                        cost > 0 AND cost < 600000000)
                    select(select avg(cost)/1000000 from ab_cost) as ab_time,
                    (select count(*) from ab_cost) as total_ab,
                    (select avg(cost)/1000000 from ab_cost where platform='ANDROID') as android_ab_time,
                    (select count(*) from ab_cost where platform='ANDROID') as android_total_ab,
                    (select avg(cost)/1000000 from ab_cost where platform='IOS') as ios_ab_time,
                    (select count(*) from ab_cost where platform='IOS') as ios_total_ab"""
        return sql

    @staticmethod
    def handle_rc_sql(rc_info):
        dat, version, table = rc_info
        sql = fr"""#Standard-SQL
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
                        platform,
                        paramValueByKey('seq',
                          event_params).string_value AS seq,
                        paramValueByKey('scene',
                          event_params).int_value AS scene,
                        paramValueByKey('subType',
                          event_params).int_value AS subType,
                        paramValueByKey('roomMode',
                          event_params).int_value AS roomMode
                      FROM
                        `{table}`
                      WHERE
                        event_name = 'BP_call_unity'
                        AND app_info.version = '{version}'
                        AND (app_info.id NOT LIKE '%.debug%'
                          AND app_info.id NOT LIKE '%.master%')
                        AND  paramValueByKey('scene',
                          event_params).int_value = 1
                        AND paramValueByKey('subType',
                          event_params).int_value = 2
                        AND paramValueByKey('roomMode',
                          event_params).int_value = 2
                      GROUP BY
                        seq,
                        platform,
                        scene,
                        subType,
                        roomMode ),
                      tb AS (
                      SELECT
                        MIN(event_timestamp) AS event_timestamp,
                        platform,
                        paramValueByKey('seq',
                          event_params).string_value AS seq,
                        paramValueByKey('scene',
                          event_params).int_value AS scene,
                        paramValueByKey('subType',
                          event_params).int_value AS subType,
                        paramValueByKey('roomMode',
                          event_params).int_value AS roomMode
                      FROM
                        `{table}`
                      WHERE
                        event_name = 'unity_enterRoom_rsp'
                        AND app_info.version = '{version}'
                        AND (app_info.id NOT LIKE '%.debug'
                          AND app_info.id NOT LIKE '%.master')
                        AND  paramValueByKey('scene',
                          event_params).int_value = 1
                        AND paramValueByKey('subType',
                          event_params).int_value = 2
                        AND paramValueByKey('roomMode',
                          event_params).int_value = 2
                      GROUP BY
                        seq,
                        platform,
                        scene,
                        subType,
                        roomMode)
                    SELECT
                      (
                      SELECT
                        COUNT(*)
                      FROM
                        ta
                     ) AS total_call_unity,
                      (
                      SELECT
                        COUNT(*)
                      FROM
                        tb) AS success_enter,
                      (
                      SELECT
                        COUNT(*)
                      FROM
                        ta
                      WHERE
                        platform='ANDROID') AS android_total_call_unity,
                      (
                      SELECT
                        COUNT(*)
                      FROM
                        tb
                      WHERE
                        platform='ANDROID') AS android_success_enter,
                      (
                      SELECT
                        COUNT(*)
                      FROM
                        ta
                      WHERE
                        platform='IOS') AS ios_total_call_unity,
                      (
                      SELECT
                        COUNT(*)
                      FROM
                        tb
                      WHERE
                        platform='IOS') AS ios_success_enter"""
        return sql

    @staticmethod
    def handle_ctoe_sql(ctoe_info):
        dat, version, table = ctoe_info

        sql = fr"""WITH
                      framesended AS (
                      SELECT
                        event_name AS event_name,
                        platform,
                        event_params.value.string_value AS seq
                      FROM
                        `{table}` AS T
                      CROSS JOIN
                        T.event_params
                      WHERE
                        event_name = 'unity_frame_sended'
                        AND event_params.key = 'seq'
                        AND app_info.version = '{version}'
                      GROUP BY
                        seq,
                        event_name,
                        platform
                        )
                    SELECT
                      (
                      SELECT
                        COUNT(*)
                      FROM
                        framesended)AS total_success_exit,
                      (
                      SELECT
                        COUNT(*)
                      FROM
                        framesended
                      WHERE
                        platform='ANDROID')AS android_success_exit,
                      (
                      SELECT
                        COUNT(*)
                      FROM
                        framesended
                      WHERE
                        platform='IOS')AS ios_success_exit"""
        return sql

    @staticmethod
    def handle_editor_avg_fps_sql(editor_info):
        dat, version, table = editor_info
        avg_editor_fps_app_info = HandleSql.handle_versions_condition(version)
        sql = fr"""#Standard-SQL
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
                        `{table}`
                      WHERE
                        event_name = 'unity_avg_fps'
                        AND {avg_editor_fps_app_info}
                        AND (app_info.id not like '%.debug%' and app_info.id not like '%.master%')
                        AND ((paramValueByKey('scene',
                              event_params).int_value =1
                            AND (paramValueByKey('subType',
                                event_params).int_value=1
                              OR paramValueByKey('subType',
                                event_params).int_value=3))
                          OR (paramValueByKey('scene',
                              event_params).int_value =2
                            AND (paramValueByKey('subType',
                                event_params).int_value=1
                              OR paramValueByKey('subType',
                                event_params).int_value=2)))
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
        return sql

    @staticmethod
    def handle_avg_ping_sql(ping_info):
        """
        :param info:
        :return:
        """
        dat, version, table = ping_info
        sql = fr"""#Standard-SQL
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
                    platform,
                    paramValueByKey('seq',
                      event_params).string_value AS seq,
                    paramValueByKey('mapId',
                      event_params).string_value AS mapId,
                    paramValueByKey('scene',
                      event_params).int_value AS scene,
                    paramValueByKey('subType',
                      event_params).int_value AS subType,
                    paramValueByKey('region',
                      event_params).string_value AS region,
                    paramValueByKey('maxPing',
                      event_params).string_value AS maxPing,
                    paramValueByKey('averagePing',
                      event_params).string_value AS averagePing
                  FROM
                    -- 需要修改结尾的日期，改成想要查询的日期格式参照如下
                    `{table}`
                  WHERE
                    event_name = 'unity_pingTime_send'
                    AND app_info.version = '{version}'
                    ),
                  ping_res AS(
                  SELECT
                    seq,
                    mapId,
                    platform,
                    min(CAST(averagePing as INT64)) AS averagePing,
                    region
                  FROM
                    ta
                  where 
                  CAST(averagePing as INT64) < 3000
                  GROUP BY
                    seq,
                    mapId,
                    platform,
                    region)
                SELECT
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    ping_res) AS total,
                  (
                  SELECT
                    AVG(averagePing)
                  FROM
                    ping_res) AS avg_ping,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    ping_res
                  WHERE
                    platform='ANDROID') AS android_total,
                  (
                  SELECT
                    AVG(averagePing)
                  FROM
                    ping_res
                  WHERE
                    platform='ANDROID') AS android_avg_ping,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    ping_res
                  WHERE
                    platform='IOS') AS ios_total,
                  (
                  SELECT
                    AVG(averagePing)
                  FROM
                    ping_res
                  WHERE
                    platform='IOS') AS ios_avg_ping,
                   (
                  SELECT
                    COUNT(*)
                  FROM
                    ping_res
                  WHERE
                    averagePing <=100 ) AS le100_ms,
                     (
                  SELECT
                    COUNT(*)
                  FROM
                    ping_res
                  WHERE
                    averagePing > 100 and  averagePing<=200) AS gt100_le200_ms,
                       (
                  SELECT
                    COUNT(*)
                  FROM
                    ping_res
                  WHERE
                    averagePing > 200 and  averagePing<=300) AS gt200_le300_ms,
                       (
                  SELECT
                    COUNT(*)
                  FROM
                    ping_res
                  WHERE
                    averagePing>300) AS gt300_ms,
                    (
                  SELECT
                    AVG(averagePing)
                  FROM
                    ping_res
                  WHERE
                    ping_res.region='PH' or ping_res.region='ph') AS filipino_avg_ping,
                      (
                  SELECT
                    AVG(averagePing)
                  FROM
                    ping_res
                  WHERE
                    ping_res.region='id' or ping_res.region='ID') AS indonesian_avg_ping,
                     (
                  SELECT
                    AVG(averagePing)
                  FROM
                    ping_res
                  WHERE
                    ping_res.region='vn' or ping_res.region='VN') AS vietnam_avg_ping,
                       (
                  SELECT
                    AVG(averagePing)
                  FROM
                    ping_res
                  WHERE
                    ping_res.region='MX' or ping_res.region='mx') AS mexico_avg_ping,
                     (
                  SELECT
                    AVG(averagePing)
                  FROM
                    ping_res
                  WHERE
                    ping_res.region='br' or ping_res.region='BR') AS brazil_avg_ping,
                     (
                  SELECT
                    AVG(averagePing)
                  FROM
                    ping_res
                  WHERE
                    ping_res.region='us' or ping_res.region='US') AS us_avg_ping"""
        return sql

    @staticmethod
    def handle_ios_crash_and_oom_sql(crash_date, version='1.32.0'):
        sql = fr"""#Standard-SQL
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
                WITH
                  ta AS (
                  SELECT
                    user_id,
                    event_name,
                    event_timestamp,
                    app_info.version AS version,
                    FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP_MICROS(event_timestamp),'Asia/Shanghai') AS time_hour,
                    platform,
                    device.mobile_model_name,
                    paramValueByKey('type',
                      event_params).string_value AS type,
                  FROM
                    `BP-_{crash_date}`
                  WHERE
                    event_name = 'reboot_type'
                    AND app_info.version >= '{version}'),
                  normal_crashs AS (
                  SELECT
                    mobile_model_name||':'||COUNT(mobile_model_name) AS mobiel_and_times
                  FROM
                    ta
                  WHERE
                    type = 'normal_crash'
                  GROUP BY
                    mobile_model_name
                  ORDER BY
                    COUNT(mobile_model_name) DESC
                  LIMIT
                    10),
                  foreground_ooms AS (
                  SELECT
                    mobile_model_name||':'||COUNT(mobile_model_name) AS mobiel_and_times
                  FROM
                    ta
                  WHERE
                    type = 'foreground_oom'
                  GROUP BY
                    mobile_model_name
                  ORDER BY
                    COUNT(mobile_model_name) DESC
                  LIMIT
                    10),
                  normal_crsh_high_five AS (
                  SELECT
                    STRING_AGG(mobiel_and_times,'+' ) AS crash_mobile_and_times
                  FROM
                    normal_crashs),
                  foreground_oom_high_five AS (
                  SELECT
                    STRING_AGG(mobiel_and_times,'+' ) AS oom_mobile_and_times
                  FROM
                    foreground_ooms)
                  -- ios 崩溃率及对应崩溃（crash and OOM）前5的机型查询（机型:次数+机型:次数...etc）
                SELECT
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    ta) AS reboot_all,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    ta
                  WHERE
                    type = 'normal_crash') AS normal_crash,
                  (
                  SELECT
                    COUNT(*)
                  FROM
                    ta
                  WHERE
                    type = 'foreground_oom') AS foreground_oom,
                  (
                  SELECT
                    *
                  FROM
                    normal_crsh_high_five) AS normal_crash_mobile_and_times,
                  (
                  SELECT
                    *
                  FROM
                    foreground_oom_high_five) AS oom_mobile_and_times
                  -- select * from normal_crsh_high_five"""
        return sql

    @staticmethod
    def handle_versions_condition(versions):

        if isinstance(versions, (list, tuple)):
            tmp = []
            for v in versions:
                condition = f"app_info.version='{v}'"
                tmp.append(condition)

            app_info_condition = " OR ".join(tmp)
            app_info_condition = "(" + app_info_condition + ")"
        else:
            app_info_condition = f"app_info.version='{versions}'"

        return app_info_condition


if __name__ == "__main__":
    info = ['20220223', '1.16.0', '']
    sql = HandleSql.handle_ctop_params(info)
    print(sql)
