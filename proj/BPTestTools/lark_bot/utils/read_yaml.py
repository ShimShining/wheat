# -*- coding: utf-8 -*-
"""
@Author: shining
@File: read_yaml.py
@Date: 2022/11/14 5:26 下午
@Version: python 3.9
@Describe:
"""

# -*- coding: utf-8 -*-
"""
@Author: shining
@File: read_yaml.py
@Date: 2021/11/16 11:19 下午
@Version: python 3.10
@Describle: yaml文件读取
"""
import csv
import yaml


class ReadYAML:

    @staticmethod
    def read(yaml_path):
        """
        读取yaml文件
        :param yaml_path:
        :return: yaml文件内内容
        """
        with open(yaml_path, encoding="utf-8") as yf:

            return yaml.safe_load(yf)

    @staticmethod
    def write_yaml(yaml_path, data: dict):
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)

    def read_csv(self, csv_path):
        """
        读取csv文件
        ：csv_path；csv文件路径
        ：x ：读取文件第一列值:
        """
        with open(csv_path) as c:
            sv = csv.reader(c)
            x = []
            for i, data in enumerate(sv):
                if i == 0:
                    continue
                if len(data[0]) >= 18:
                    x.append(data[0])
            return x


if __name__ == "__main__":

    data = ReadYAML.read('../satic_resource/total_issues.yml')
    print(data)
    # data = {'a': 1, "b": 2}
    # ReadYAML.write_yaml('./test.yml', data)