import hashlib
import time
import requests
import json
proxies = {"http": "127.0.0.1:7890", "https": "127.0.0.1:7890"}

def generate_sign(input_string):
    """生成 MD5 签名"""
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode("utf-8"))
    return md5_hash.hexdigest()

def list():
    # 请求头设置
    headers = {
        "Host": "youjia.baidu.com",
        "content-type": "application/x-www-form-urlencoded",
        "x-bd-traceid": "fc9e1e176b4f4e9f8f74d27c1a6ae80d",
        "accept": "*/*",
        "x-bdboxapp-netengine": "1",
        "accept-language": "zh-CN,zh-Hans;q=0.9",
        "request-tag": "Others",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bdapp/1.0 (youjia; youjia) youjia/2.39.0.1 (Baidu; P2 15.8.3)",
    }

    # 请求 URL
    url = (
        "https://youjia.baidu.com/feed/2_530073fe69e584cbb9347704e228fe59/getlistbychannel"
    )

    # 请求参数
    params = {
        "action": "feed",
        "cmd": "14001",
        "maid": "_a2S8_aq28_qa28q8a2q8_a628ggh28q_uXN8_aqvI_6a28qza2qi_a628_qa28q_0268_aq28_quX86_avgI_aq28zqa2iggh268_aq28_qa28qALqqC",
        "refresh": "7",
        "imgtype": "webp",
        "appname": "youjia",
        "branchname": "youjia",
        "cfrom": "1024323j",
        "from": "1024323j",
        "is_close_individual": "0",
        "osbranch": "i0",
        "osname": "baiduboxapp",
        "service": "bdbox",
        "sid": "177995_1-103916_3-999993_2-105949_6-999990_2-999992_1-999991_1-999999_71-999989_1-999988_1",
        "ua": "750_1334_iphone_2.39.0.1_0",
        "uid": "3273A56E0143AE21B24602A793934ED89D755C054OLHLERBNOL",
        "ut": "iPhone9,1_15.8.3",
        "zid": "UH9yJICAgIMAAAADVAP6S28BawJl8RAg_Bp3RQEhXx-yuObisbTm4eK35OSztOOws-K24bLj5eW4sOa2t7W2tgApcjF7AAAAAGi6cYAmKAE",
        "sign": "",
    }

    # 构建原始字符串来生成签名
    input_string = "&".join(
        f"{key}={value}" for key, value in params.items() if key != "sign"
    )

    # 生成签名
    sign = generate_sign(input_string)
    params["sign"] = sign  # 添加生成的签名

    # 请求数据
    data = {
        "data": '{\n  "from" : "youjia",\n  "city" : "深圳",\n  "youjia_pn" : "6",\n  "data" : {\n    "tab_id" : "14001",\n    "refresh_index" : "5",\n    "refresh_count" : "1",\n    "tab_name" : "推荐",\n    "idfa" : "00000000-0000-0000-0000-000000000000",\n    "BSSID" : "",\n    "mod" : "iPhone9,1",\n    "client_query_time" : "1757049216661",\n    "refresh_state" : "7",\n    "network_state" : "1",\n    "is_close_individual" : "0",\n    "click_id" : "f62e1fd12195c75799c6ac3f2488f615",\n    "session_id" : "1757048541575",\n    "nt" : "1",\n    "pull_to_refresh_count" : "5"\n  },\n  "dislike_mthid_list" : "[]",\n  "dislike_yjcard_list" : "[]",\n    "upload_ids" : [\n    {\n      "clk_ts" : 0,\n      "id" : "news_9194983260603746823",\n      "show" : 1,\n      "focus_dur" : 0.05000000074505806,\n      "ht" : 171.80322265625,\n      "clk" : 0,\n      "show_ts" : 1757049104,\n      "show_dur" : 4.0999999046325684,\n      "focus_ts" : 1757049216,\n      "show_ht" : 137.2364501953125\n    },\n    {\n      "clk_ts" : 1757049106,\n      "id" : "news_9113297853153288637",\n      "show" : 1,\n      "focus_dur" : 0.05000000074505806,\n      "ht" : 171.80322265625,\n      "clk" : 1,\n      "show_ts" : 1757049104,\n      "show_dur" : 0.05000000074505806,\n      "focus_ts" : 1757049104,\n      "show_ht" : 108.05217742919922\n    },\n    {\n      "id" : "sv_9592463175121930562",\n      "clk" : 0,\n      "show" : 1,\n      "clk_ts" : 0,\n      "show_ts" : 1757049216\n    }\n  ],\n  "dislike_seriesid_list" : "[]",\n  "info" : {\n\n  }\n}'
    }

    # 发送 POST 请求
    response = requests.post(
        url,
        headers=headers,
        params=params,
        data=data,
        proxies=proxies,
    )

    # 解析 JSON 响应并保存到本地
    try:
        json_response = response.json()
        # 保存JSON到文件
        with open("response_data.json", "w", encoding="utf-8") as f:
            json.dump(json_response, f, ensure_ascii=False, indent=4)
        print("JSON 数据已保存到 response_data.json")

        # 获取 data 字段
        ddata = json_response["data"]

        # 如果 ddata 是字符串，解析为字典
        if isinstance(ddata, str):
            ddata_dict = json.loads(ddata)  # 解析字符串为字典
        else:
            ddata_dict = ddata  # 已经是字典

        # 访问数据中的部分
        data_14001 = ddata_dict["14001"]
        itemlist = data_14001["itemlist"]
        items = itemlist["items"]
        for item in items:
            nid = item["id"].split("_")[1]
            print("nid==>", nid)
            detail(nid)
            break
    except json.JSONDecodeError as e:
        print("JSON 解码错误:", e)
        print("响应文本:", response.text)


def detail(nid):
    headers = {
        "Host": "youjia.baidu.com",
        "accept": "*/*",
        "request-tag": "Others",
        "x-bd-traceid": "13b0f8bcfb184769b5ce6b03fe6ead24",
        "x-bdboxapp-netengine": "1",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bdapp/1.0 (youjia; youjia) youjia/2.39.0.1 (Baidu; P2 15.8.3)",
        "accept-language": "zh-CN,zh-Hans;q=0.9",
    }

    url = "https://youjia.baidu.com/baijiahao/article"

    params = {
        "ua": "750_1334_iphone_2.39.0.1_0",
        "ban_filterid": "3",
        "sign": "",  # 留空，稍后生成
        "app_version": "2.39.0.1",
        "nid": nid,
        "from": "appstore",
        "temp_phone_model": "iPhone9,1",
        "zid": "NXFhQ4GBgYIAAAADVAP6FG8BawJl8Wgg_AohDy5UBUKzuefjsLXn4OO25eWyteKxsuO34LPi5OS5see3trS3t2V6TVZWAAAAAGi6cYEPdSI",
        "os": "ios",
        "mfg": "Apple",
        "token": "2_10af3945b780e8289ebf7ba2110702ae",
        "sid": "177995_1-103916_3-999993_2-105949_6-999990_2-999992_1-999991_1-999999_71-999989_1-999988_1",
        "city": "深圳",
        "is_close_individual": "0",
        "ntsts": "1",
        "os_version": "15.8.3",
        "adid": "_a2q8_aq28zqa2iggh268_ugX8_qavIN_a2q8_aq28_qa28qA",
        "condition_version": "V4_20230412",
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


if __name__ == "__main__":
    list()