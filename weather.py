"""
ProgramName:WEATHER-PYTHON
"""
import json
import os
import pickle
import requests
import time
import logging
# 导入所需要的库

if not os.path.exists("first_time.pickle"):
    key = input("请输入和风天气key：")
    with open("first_time.pickle", "wb") as f:
        pickle.dump(key, f)
else:
    with open("first_time.pickle", "rb") as f:
        key = pickle.load(f)
# 首次使用检查

city = input("请输入你想查询的城市名称：")
# 用户输入地名

URL = "https://geoapi.qweather.com/v2/city/lookup"
# 和风天气查询接口

querystring = {"location": city, "key": key}
# 访问前信息收集

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
# 用户请求头

response = requests.request("GET", URL, headers=headers, params=querystring,timeout=10)

if "location" in response.json():
    city_id = response.json()["location"][0]["id"]
    logging.INFO('request ok')
else:
    print("获取城市ID失败，请检查你的请求参数和API Key是否正确。")
    logging.ERROR('APIKEYERROR')
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

<<<<<<< HEAD
# 懒得写了，应该都能看懂吧？
=======
#日志记录
log_json = open('output_json.log', mode='a')
log_json.write( time.time()+response.text+'\n' )
log_output = open('weather.log', mode='a')
log_json.write( time.time()+'\n'+'link'+fx_link+'\n'+'returncode'+code+'\n' )
>>>>>>> 4323ff794a82804860aedb9ea33e429e131a7fd1
