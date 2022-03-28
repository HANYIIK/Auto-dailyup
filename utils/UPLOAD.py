# -*- coding: utf-8 -*-
"""
@Time        : 2021/3/12 12:28
@Author      : YIIK HAN
@File        : UPLOAD.py
@Description : Add a Guangzhou version

@Time        : 2020/9/2 17:32
@Author      : Jiang Du
@Email       : 39544089+jiang-du@users.noreply.github.com
@File        : Utils.py
@Description :
@Version     : 0.3

@Time        : 2020/7/19 12:25
@Author      : NingWang
@Email       : yogehaoren@gmail.com
@File        : Utils.py
@Description :
@Version     : 0.1-dev
"""
import requests
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
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/84.0.4147.89",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://xxcapp.xidian.edu.cn/site/ncov/xisudailyup",
    "Origin": "https://xxcapp.xidian.edu.cn"
}

# 填报网址
UPLOAD_URL = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save"

# 北校区 上传信息
NORTH_UPLOAD_MSG = {
    "sfzx": "1",  # 是否在校(0->否, 1->是)
    "tw": "1",  # 体温 (36℃->0, 36℃到36.5℃->1, 36.5℃到36.9℃->2, 36.9℃到37℃.3->3, 37.3℃到38℃->4, 38℃到38.5℃->5,
    # 38.5℃到39℃->6, 39℃到40℃->7, 40℃以上->8)
    "sfcyglq": "0",  # 是否处于隔离期? (0->否, 1->是)
    "sfyzz": "0",  # 是否出现乏力、干咳、呼吸困难等症状？ (0->否, 1->是)
    "qtqk": "",  # 其他情况 (文本)
    "askforleave": "0",  # 是否请假外出? (0->否, 1->是)
    "geo_api_info": "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"VDa\":\"jsonp_324977_\","
                    "\"position\":{\"Q\":34.23254,\"R\":108.91516000000001,\"lng\":108.91802,\"lat\":34.23231},"
                    "\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\","
                    "\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"61010\","
                    "\"adcode\":\"610113\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\","
                    "\"building\":\"\",\"buildingType\":\"\",\"street\":\"白沙路\",\"streetNumber\":\"238号\","
                    "\"country\":\"中国\",\"province\":\"陕西省\",\"city\":\"西安市\",\"district\":\"雁塔区\","
                    "\"township\":\"电子城街道\"},\"formattedAddress\":\"陕西省西安市雁塔区电子城街道西安电子科技大学北校区\",\"roads\":[],"
                    "\"crosses\":[],\"pois\":[]}",
    "area": "陕西省 西安市 雁塔区",  # 地区
    "city": "西安市",  # 城市
    "province": "陕西省",  # 省份
    "address": "陕西省西安市雁塔区电子城街道西安电子科技大学北校区"  # 实际地址
}

# 南校区 上传信息
SOUTH_UPLOAD_MSG = {
    "sfzx": "1",  # 是否在校(0->否, 1->是)
    "tw": "1",
    # 体温 (36℃->0, 36℃到36.5℃->1, 36.5℃到36.9℃->2, 36.9℃到37℃.3->3, 37.3℃到38℃->4, 38℃到38.5℃->5, 38.5℃到39℃->6, 39℃到40℃->7,
    # 40℃以上->8)
    "sfcyglq": "0",  # 是否处于隔离期? (0->否, 1->是)
    "sfyzz": "0",  # 是否出现乏力、干咳、呼吸困难等症状？ (0->否, 1->是)
    "qtqk": "",  # 其他情况 (文本)
    "askforleave": "0",  # 是否请假外出? (0->否, 1->是)
    "geo_api_info": "{\"type\":\"complete\",\"position\":{\"Q\":34.121994628907,\"R\":108.83715983073,"
                    "\"lng\":108.83716,\"lat\":34.121995},\"location_type\":\"html5\",\"message\":\"Get ipLocation "
                    "failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":65,"
                    "\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"61010\","
                    "\"adcode\":\"610116\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\","
                    "\"building\":\"\",\"buildingType\":\"\",\"street\":\"雷甘路\",\"streetNumber\":\"264号\","
                    "\"country\":\"中国\",\"province\":\"陕西省\",\"city\":\"西安市\",\"district\":\"长安区\","
                    "\"township\":\"兴隆街道\"},\"formattedAddress\":\"陕西省西安市长安区兴隆街道西安电子科技大学长安校区办公辅楼\",\"roads\":[],"
                    "\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}",
    "area": "陕西省 西安市 长安区",  # 地区
    "city": "西安市",  # 城市
    "province": "陕西省",  # 省份
    "address": "陕西省西安市长安区兴隆街道西安电子科技大学长安校区行政辅楼",  # 实际地址
}

# 广州研究院 上传信息
GZ_UPLOAD_MSG = {
    "sfzx": "1",  # 是否在校(0->否, 1->是)
    "tw": "1",
    # 体温 (36℃->0, 36℃到36.5℃->1, 36.5℃到36.9℃->2, 36.9℃到37℃.3->3, 37.3℃到38℃->4, 38℃到38.5℃->5, 38.5℃到39℃->6, 39℃到40℃->7,
    # 40℃以上->8)
    "sfcyglq": "0",  # 是否处于隔离期? (0->否, 1->是)
    "sfyzz": "0",  # 是否出现乏力、干咳、呼吸困难等症状？ (0->否, 1->是)
    "qtqk": "",  # 其他情况 (文本)
    "askforleave": "0",  # 是否请假外出? (0->否, 1->是)
    "geo_api_info": "{\"type\":\"complete\",\"position\":{\"Q\":23.393325923617535,\"R\":113.49440818443395,"
                    "\"lng\":113.49441,\"lat\":23.39333},\"location_type\":\"html5\",\"message\":\"Get ipLocation "
                    "failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":65,"
                    "\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"4401\","
                    "\"adcode\":\"440112\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\","
                    "\"building\":\"\",\"buildingType\":\"\",\"street\":\"凤凰一横路\",\"streetNumber\":\"313号\","
                    "\"country\":\"中国\",\"province\":\"广东省\",\"city\":\"广州市\",\"district\":\"黄埔区\","
                    "\"township\":\"九佛街道\"},\"formattedAddress\":\"广东省广州市黄埔区凤凰一横路313号九佛街道中新广州知识城\",\"roads\":[],"
                    "\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}",
    "area": "广东省 广州市 黄埔区",  # 地区
    "city": "广州市",  # 城市
    "province": "广东省",  # 省份
    "address": "广东省广州市黄埔区九佛街道中新广州知识城",  # 实际地址
}

# 杭州研究院 上传信息
HZ_UPLOAD_MSG = {
    "sfzx": "1",  # 是否在校(0->否, 1->是)
    "tw": "1",
    # 体温 (36℃->0, 36℃到36.5℃->1, 36.5℃到36.9℃->2, 36.9℃到37℃.3->3, 37.3℃到38℃->4, 38℃到38.5℃->5, 38.5℃到39℃->6, 39℃到40℃->7,
    # 40℃以上->8)
    "sfcyglq": "0",  # 是否处于隔离期? (0->否, 1->是)
    "sfyzz": "0",  # 是否出现乏力、干咳、呼吸困难等症状？ (0->否, 1->是)
    "qtqk": "",  # 其他情况 (文本)
    "askforleave": "0",  # 是否请假外出? (0->否, 1->是)
    "geo_api_info": "{\"type\":\"complete\",\"position\":{\"Q\":30.241904123617535,\"R\":120.3283711443395,"
                    "\"lng\":120.328371,\"lat\":30.241904},\"location_type\":\"html5\",\"message\":\"Get ipLocation "
                    "failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":65,"
                    "\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"3301\","
                    "\"adcode\":\"330109\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\","
                    "\"building\":\"\",\"buildingType\":\"\",\"street\":\"钱农东路\",\"streetNumber\":\"8号\","
                    "\"country\":\"中国\",\"province\":\"浙江省\",\"city\":\"杭州市\",\"district\":\"萧山区\","
                    "\"township\":\"经济技术开发区\"},\"formattedAddress\":\"浙江省杭州市萧山区经济技术开发区钱农东路8号西安电子科技大学杭州研究院\",\"roads\":[],"
                    "\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}",
    "area": "浙江省 杭州市 萧山区",  # 地区
    "city": "杭州市",  # 城市
    "province": "浙江省",  # 省份
    "address": "浙江省杭州市萧山区经济技术开发区西安电子科技大学杭州研究院",  # 实际地址
}


# master
def upload_ncov_message(cookie, config):
    """
    提交内容的高阶API
    外部使用提交功能就是调用这个API，传入cookies即可提交
    :param cookie: cookies
    :param config: 配置信息
    :return: 无
    """
    header = DEFAULT_HEADER
    upload_message = get_upload_msg(config)
    print("您当前的地点：" + upload_message["address"])
    r = requests.post(UPLOAD_URL, cookies=cookie, headers=header, data=upload_message, proxies=get_proxy_())
    # 上报成功
    if r.json()['e'] == 0:
        print("上报成功(^_^)")
        return 0

    # 上报失败
    else:
        print("上报出现错误(T_T)")
        print("错误信息: {}".format(r.json()['m']))
        return 1

# branch
def get_upload_msg(config):
    """
    位置四选一
    :param config: 得到位置信息
    :return: 提交的内容
    """
    location = config["Location"]
    if location == "1":
        upload_msg = NORTH_UPLOAD_MSG   # 北校区

    elif location == "2":
        upload_msg = SOUTH_UPLOAD_MSG   # 南校区

    elif location == "3":
        upload_msg = GZ_UPLOAD_MSG      # 广州研究院

    elif location == "4":
        upload_msg = HZ_UPLOAD_MSG      # 杭州研究院

    elif location == "5":
        raise RuntimeError("？请认真选择位置")

    else:
        raise RuntimeError("未选择位置信息")

    return upload_msg
