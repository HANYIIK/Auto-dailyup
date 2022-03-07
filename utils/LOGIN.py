import pickle
import requests
import os
import json
import urllib.request

#获取代理
def get_proxy_():
    proxy=urllib.request.getproxies() #获取代理
    if len(proxy) != 0:
        proxies = {
            "http": proxy['http'],
            "https": proxy['https'].replace('https','http')
        }
        return proxies

    else:
        proxies = {
            "http": None,
            "https": None
        }
        return proxies

DEFAULT_HEADER = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/84.0.4147.89",
    "X-Requested-With": "XMLHttpRequest"
}

# 登录网址
LOGIN_URL = "https://xxcapp.xidian.edu.cn/uc/wap/login/check"

COOKIE_FILE_NAME = "data/cookie.inf"

# master
def login(config):
    """
    登录的高阶API，将登录操作的细节进行隐藏
    有 cookie 文件则返回 cookie 字节流, 没有则登录生成 cookie 文件并返回字节流。
    :return: cookie 文件字节流
    """
    _cookies = ""
    if os.path.exists(COOKIE_FILE_NAME):
        _cookies = load_cookie_from_file(COOKIE_FILE_NAME)
    else:
        stu_num = config["stuNum"]
        password = config["passWord"]
        _cookies = get_cookie_from_login(stu_num, password)
    return _cookies

# branch
def get_cookie_from_login(student_id: str, password: str, cookie_file_path=COOKIE_FILE_NAME):
    """
    登录成功时保存 cookie.inf 文件
    :param student_id: 学号
    :param password: 密码
    :param cookie_file_path: cookies文件路径
    :return: cookie文件
    """
    r = requests.post(LOGIN_URL, data={"username": student_id, "password": password}, headers=DEFAULT_HEADER, proxies=get_proxy_())
    if r.status_code == 200:
        # 登录成功
        if r.json()['e'] == 0:
            print("登录成功！已为您自动开通免密登录，下次运行无需输入密码(^_^)")
            # 写入cookie文件，下次免密登录
            with open(cookie_file_path, 'wb') as f:
                pickle.dump(r.cookies, f)
            return r.cookies
        else:
            print(r.json()['m'])
            raise RuntimeError("登录失败, 请检查用户名或密码是否正确(T_T)")

# branch
def load_cookie_from_file(cookie_file_path=COOKIE_FILE_NAME):
    """
    从文件中加载cookie
    :param cookie_file_path: 文件路径
    :return:
    """
    with open(cookie_file_path, 'rb') as f:
        return pickle.load(f)

