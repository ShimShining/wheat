# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: csv_handler.py
@Date: 2022/12/28 10:52 上午
@Version: python 3.9
@Describe:
"""
import csv
import codecs
import os.path


class CSVHandler:

    @staticmethod
    def read_csv(file_path):
        with codecs.open(file_path, 'r', encoding='utf-8') as f:
            csv_data = list(csv.reader(f))

        return csv_data

    @staticmethod
    def write_to_csv(write_data, file_path, key=None):
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                writer = csv.writer(f)
                if key:
                    writer.writerow(key)
        with codecs.open(file_path, 'a+', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(write_data)
            # if len(write_data) == 1:
            #     writer.writerow(write_data)
            # elif len(write_data) > 1:
            #     writer.writerows(write_data)

