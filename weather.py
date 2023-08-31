"""
ProgramName:WEATHER-PYTHON
"""
import json
import os
import pickle
import requests
import time
import logging
import sys
import time
# 导入所需要的库

if not os.path.exists("first_time.bin"):
    key = input("请输入和风天气key：")
    with open("first_time.bin", "wb") as f:
        pickle.dump(key, f)
else:
    with open("first_time.bin", "rb") as f:
        key = pickle.load(f)
# 首次使用检查

city = input("请输入你想查询的城市名称：")
# 用户输入地名

URL = "https://geoapi.qweather.com/v2/city/lookup?"
# 和风天气查询接口

querystring = {"location": city, "key": key}
# 访问前信息收集

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
# 用户请求头

response = requests.request("GET", URL, headers=headers, params=querystring,timeout=10)

if "location" in response.json():
    city_id = response.json()["location"][0]["id"]
else:
    print("获取城市ID失败，请检查你的请求参数和API Key是否正确。")
    logging.ERROR('APIKEYERROR')
    pickle.dump("", f)
    exit()
# 获取id，获取到了就保存，没有就报错

URL = "https://devapi.qweather.com/v7/weather/now"

querystring = {"location": city_id, "key": key}

response = requests.request("GET", URL, headers=headers, params=querystring,timeout=10)

response = requests.request("GET", URL, headers=headers, params=querystring,timeout=10)

data = json.loads(response.text)
code = data["code"]
update_time = data["updateTime"]
fx_link = data["fxLink"]
now_data = data["now"]
obs_time = now_data["obsTime"]
temp = now_data["temp"]
feels_like = now_data["feelsLike"]
icon = now_data["icon"]
text = now_data["text"]
wind360 = now_data["wind360"]
wind_dir = now_data["windDir"]
wind_scale = now_data["windScale"]
wind_speed = now_data["windSpeed"]
humidity = now_data["humidity"]
precip = now_data["precip"]
pressure = now_data["pressure"]
vis = now_data["vis"]
cloud = now_data["cloud"]
dew = now_data["dew"]

#print结果输出

# 以下为包装好的 Logger 类的定义
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding="utf-8")  # 防止编码错误

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

t = time.strftime("-%Y%m%d-%H%M%S", time.localtime())  # 时间戳
filename = 'log' + t + '.txt'

log = Logger(filename)  
sys.stdout = log

print("网页视图链接", fx_link)
print("天气更新时间", obs_time)
print("当前温度为", temp, "℃")
print("体感温度", feels_like, "℃")
print("天气状况", text)
print("风向360角度", wind360, "°")
print("风向", wind_dir)
print("风力等级", wind_scale)
print("风速", wind_speed, "公里/小时")
print("相对湿度", humidity, "%")
print("当前小时累计降水量", precip, "毫米")
print("大气压强", pressure, "百帕")
print("能见度", vis, "公里")
print("云量", cloud, "%")
print("露点湿度", dew)
