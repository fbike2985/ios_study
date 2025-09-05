import requests
import hashlib
import json
proxies={
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
}
def generate_sign(input_string):
    """生成 MD5 签名"""
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode("utf-8"))
    return md5_hash.hexdigest()
headers = {
    "Host": "youjia.baidu.com",
    "content-type": "application/x-www-form-urlencoded",
    "x-bd-traceid": "787647989aaa43aa84d6b0ab6f2859b5",
    "accept": "*/*",
    "x-bdboxapp-netengine": "1",
    "accept-language": "zh-CN,zh-Hans;q=0.9",
    "request-tag": "Others",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bdapp/1.0 (youjia; youjia) youjia/2.39.0.1 (Baidu; P2 15.8.3)"
}

url = "https://youjia.baidu.com/wenda/getquestiondetail"
params = {
    "adid": "_a2q8_aq28zqa2iggh268_ugX8_qavIN_a2q8_aq28_qa28qA",
    "ban_filterid": "3",
    "app_version": "2.39.0.1",
    "from": "appstore",
    "temp_phone_model": "iPhone9,1",
    "zid": "I1AuQtzc3N8AAAAEVAP6fm8BawJl8WUg_H1NFGR0dVzu5Lq-7ei6vb7ruLjv6L_s777qve6_ubnk7Lrq6-nq6i0eUy9gAAAAAGi6lNwuCVo",
    "os": "ios",
    "mfg": "Apple",
    "token": "2_530073fe69e584cbb9347704e228fe59",
    "sid": "999999_71-177995_1-103916_3-999993_2-105949_6-999990_2-999992_1-999991_1-7310_15016-999989_1-999988_1",
    "city": "深圳",
    "is_close_individual": "0",
    "ntsts": "1",
    "os_version": "15.8.3",
    "condition_version": "V4_20230412",
    "ts": "1757058268",
    "ua": "750_1334_iphone_2.39.0.1_0",
    "sign": "dcaa1e5feea8c7e3656773375646d67e"
}
cookies = {
    "SP_FW_VER": "3.430.14",
    "BAIDUCUID": "_uvsiladvug6av8Pl8vPi0aC28_wuS8ljuBQig8fHtYfivicg8v3igtJWP5f81axt0EmA",
    "BAIDUZID": "NDtMHkUCDTcAAAADVAP6PW8BawJl8Wsg_Cd5RREkK1tLQR8bSE0fGBtOHR1KTRpJShtPGEsaHBxBSR9PTkxPT0xgSDlfAAAAAGi6lHlPHTk",
    "CITY": "%7B%22name%22%3A%22%E6%B7%B1%E5%9C%B3%22%2C%22code%22%3A%22340%22%7D",
    "YOUJIAID": "9F6902AC786FA752358617B6753DF9AA:FG=1",
    "BAIDUID": "669FD4D738A83B26D0F9341665766B68:FG=1"
}
# 构建原始字符串来生成签名
input_string = "&".join(
    f"{key}={value}" for key, value in params.items() if key != "sign"
)
# sign = generate_sign(input_string)
# params["sign"] = sign  # 添加生成的签名
data = {
    "question_id": "378996"
}
response = requests.post(url, headers=headers,params=params, data=data,cookies=cookies,proxies=proxies)

try:
    json_response = response.json()
    print(
        json.dumps(json_response, ensure_ascii=False, indent=4)
    )  # 打印格式化的 JSON 响应
except json.JSONDecodeError as e:
    print("JSON 解码错误:", e)
    print("响应文本:", response.text)