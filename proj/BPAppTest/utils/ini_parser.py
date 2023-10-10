#ini配置文件读取操作
import configparser
class IniParser:

    # 初始化打开指定ini文件并指定编码
    def __init__(self, file_path, section):
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path, encoding="utf-8")
        self.section = section
