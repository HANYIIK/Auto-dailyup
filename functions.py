import datetime
import random
import requests
import os
import platform

os_name = platform.system()

def replace_char(s, len_pwd):
    """
    强行对密码所在内存地址进行编辑。用于增强对密码的隐私保护功能。
    输入值： 字符串、修改的位置
    返回值： 0
    """
    import ctypes
    OFFSET = ctypes.sizeof(ctypes.c_size_t) * 6
    a = ctypes.c_char.from_address(id(s) + OFFSET)
    pi = ctypes.pointer(a)
    for idx in range(len_pwd):
        pi[idx] = ord('*')
    return 0

def clearWindow():
    """
    根据操作系统，自动选择清屏方式
    输入值： 无
    返回值： 无
    """
    if os_name == 'Windows':
        os.system("cls")
    elif os_name == 'Linux':
        os.system("clear")
    else:
        print("检测到您是Mac系统，暂时无法实现清屏功能哦~")

def getNowHourMinSec():
    """
    获取现在的时分秒
    输入值： 无
    返回值： 当前是时、分、秒，返回的形式是HOUR、MINIUTE、SECONDS
    """
    d = datetime.datetime.now()
    hour = int(str(d)[11:13])
    miniute = int(str(d)[14:16])
    seconds = int(str(d)[17:19])
    return hour, miniute, seconds

def updateTimeLib(time_lib):
    """
    随机更新下一天上报的时间
    输入值： 原来的上报时间
    返回值： 更新的上报时间
    """
    assert len(time_lib) == 6
    new_time = time_lib
    new_time[1] = random.randint(2,59)
    new_time[3] = random.randint(2,59)
    new_time[5] = random.randint(2,59)
    print("更新晨午晚检上报时间成功！下一天的上报时间为:")
    print("晨检 - %d点%d分，午检 - %d点%d分，晚检 - %d点%d分。" % tuple(new_time))
    return new_time

def checkTime(time_lib):
    """
    判断当前时刻是否需要上报，以及对应模式
    输入值： 上报时间
    返回值： 上报模式(1, 2, 3分别对应晨午晚检)
    """
    Hour, Minus, Secs = getNowHourMinSec()
    if Hour == time_lib[0] and Minus == time_lib[1]:
        # 晨检
        currentState = 1
    elif Hour == time_lib[2] and Minus == time_lib[3]:
        # 午检
        currentState = 2
    elif Hour == time_lib[4] and Minus == time_lib[5]:
        # 晚检
        currentState = 3
    elif Hour == 23 and Minus == 55:
        # 夜间模式
        currentState = 4
    elif not Minus:
        # 整点时刻
        currentState = 5
    else:
        currentState = 0
    if currentState:
        print("当前系统时间  %d:%d:%d" % (Hour, Minus, Secs))
    return currentState

def checkInternetConnection():
    try:
        requests.get("https://xxcapp.xidian.edu.cn/site/ncov/xisudailyup", timeout=5)
    except:
        return False
    return True

def getInfo():
    from utils.LOGIN import COOKIE_FILE_NAME
    # 初始化配置信息
    config = dict()
    for idx_key in ("stuNum", "passWord", "Location", "ServerToken"):
        if not (idx_key in config):
            config[idx_key] = 0
    # 补全缺失的信息
    if not config["stuNum"]:
        # 用户输入学号
        config["stuNum"] = input("请输入学号/工号，按回车键结束：")
        # 确认学号是合法的非0数字
        assert int(config["stuNum"], base=10)

    if not config["Location"]:
        config["Location"] = input("选择想定位的地点：1：北校区，2：南校区，3：广研院，4: 美国加利福尼亚州洛杉矶 按回车键结束：")

    if not(os.path.exists(COOKIE_FILE_NAME)):
        if not config["passWord"]:
            config["passWord"] = input("请输入密码，密码将明文显示，请注意遮挡键盘，按下回车键后将自动清屏(注意: Mac系统无法清屏)：")
            # 清屏
            clearWindow()
    return config
