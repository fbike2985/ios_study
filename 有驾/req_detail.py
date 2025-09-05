import hashlib
import requests
import time
import json

proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
}


def generate_sign(input_string):
    """生成 MD5 签名"""
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode("utf-8"))
    return md5_hash.hexdigest()


def perform_request():
    headers = {
        "Host": "youjia.baidu.com",
        "accept": "*/*",
        "request-tag": "Others",
        # "x-bd-traceid": "13b0f8bcfb184769b5ce6b03fe6ead24",
        "x-bdboxapp-netengine": "1",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bdapp/1.0 (youjia; youjia) youjia/2.39.0.1 (Baidu; P2 15.8.3)",
        "accept-language": "zh-CN,zh-Hans;q=0.9",
    }

    url = "https://youjia.baidu.com/baijiahao/article"

    params = {
        # "ua": "750_1334_iphone_2.39.0.1_0",
        # "ban_filterid": "3",
        "sign": "",  # 留空，稍后生成
        # "app_version": "2.39.0.1",
        "nid": "9228452690992887075",
        # "from": "appstore",
        # "temp_phone_model": "iPhone9,1",
        # "zid": "NXFhQ4GBgYIAAAADVAP6FG8BawJl8Wgg_AohDy5UBUKzuefjsLXn4OO25eWyteKxsuO34LPi5OS5see3trS3t2V6TVZWAAAAAGi6cYEPdSI",
        # "os": "ios",
        # "mfg": "Apple",
        "token": "2_10af3945b780e8289ebf7ba2110702ae",
        # "sid": "177995_1-103916_3-999993_2-105949_6-999990_2-999992_1-999991_1-999999_71-999989_1-999988_1",
        "city": "深圳",
        # "is_close_individual": "0",
        # "ntsts": "1",
        # "os_version": "15.8.3",
        # "adid": "_a2q8_aq28zqa2iggh268_ugX8_qavIN_a2q8_aq28_qa28qA",
        # "condition_version": "V4_20230412",
        "ts": str(int(time.time())),
    }

    # 构建原始字符串来生成签名
    input_string = "&".join(
        f"{key}={value}" for key, value in params.items() if key != "sign"
    )

    # 生成签名
    sign = generate_sign(input_string)
    params["sign"] = sign  # 添加生成的签名

    # 发送请求
    response = requests.get(url, headers=headers, params=params, proxies=proxies)

    # 解析 JSON 响应
    try:
        json_response = response.json()
        print(
            json.dumps(json_response, ensure_ascii=False, indent=4)
        )  # 打印格式化的 JSON 响应
    except json.JSONDecodeError as e:
        print("JSON 解码错误:", e)
        print("响应文本:", response.text)


# 执行请求
perform_request()
