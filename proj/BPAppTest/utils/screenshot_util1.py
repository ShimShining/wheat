# 截图存储
import traceback
from conf.module import *

# 截图函数
from utils.datetim_util1e import get_chinese_date, get_chinese_time


def take_screenshot(driver, SCREENSHOT_PATH=None):
    # 创建当前日期目录
    dir = os.path.join(SCREENSHOT_PATH, get_chinese_date())
    if not os.path.exists(dir):
        os.makedirs(dir)
    # 以当前时间为文件名

    file_name = get_chinese_time()
    map = os.path.join(dir, file_name + ".png")
    try:
        driver.get_screenshot_as_file(map)
        # 返回截图文件的绝对路径
        return map
    except:
        print("截图发生异常【{}】".format(map))
        traceback.print_exc()
        return map

