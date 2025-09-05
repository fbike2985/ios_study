import hashlib
import requests
import json
import time

def generate_sign(input_string):
    """生成 MD5 签名"""
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode("utf-8"))
    return md5_hash.hexdigest()
headers = {
    "Host": "youjia.baidu.com",
    "accept": "*/*",
    "request-tag": "Others",
    # "x-bd-traceid": "9e3e478b652a4f6bba9740fef4523bf6",
    "x-bdboxapp-netengine": "1",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bdapp/1.0 (youjia; youjia) youjia/2.39.0.1 (Baidu; P2 15.8.3)",
    "accept-language": "zh-CN,zh-Hans;q=0.9"
}

url = "https://youjia.baidu.com/bff-app-api/video/crawlerdetail"
params = {
    "ts": str(int(time.time())),
    "meta_type": "bjh_video",
    "app_version": "2.39.0.1",
    "ua": "750_1334_iphone_2.39.0.1_0",
    "city": "深圳",
    "zid": "RSgpG3x8fH8AAAAEVAP6fm8BawJl8S8g_CNNIShdZCBORBoeTUgaHR5LGBhPSB9MTx5KHU4fGRlETBpKS0lKSi8lCjgeAAAAAGi6i3xAblY",
    "os": "ios",
    "sid": "999999_71-177995_1-103916_3-999993_2-105949_6-999990_2-999992_1-999991_1-7310_15016-999989_1-999988_1",
    "is_close_individual": "0",
    "sign": "691888168c96845abe472eee883565ba",
    "mfg": "Apple",
    "token": "2_530073fe69e584cbb9347704e228fe59",
    "temp_phone_model": "iPhone9,1",
    "ntsts": "1",
    "os_version": "15.8.3",
    "from": "appstore",
    "condition_version": "V4_20230412",
    "adid": "_a2q8_aq28zqa2iggh268_ugX8_qavIN_a2q8_aq28_qa28qA",
    "meta_id": "8317636278008304583",
    "ban_filterid": "3"
}
# 构建原始字符串来生成签名
input_string = "&".join(
    f"{key}={value}" for key, value in params.items() if key != "sign"
)

# 生成签名
sign = generate_sign(input_string)
params["sign"] = sign  # 添加生成的签名
response = requests.get(url, headers=headers,params=params,proxies={
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
})

try:
    json_response = response.json()
    print(
        json.dumps(json_response, ensure_ascii=False, indent=4)
    )  # 打印格式化的 JSON 响应
except json.JSONDecodeError as e:
    print("JSON 解码错误:", e)
    print("响应文本:", response.text)