import hashlib


def generate_md5(input_string):
    # 创建 MD5 哈希对象
    md5_hash = hashlib.md5()

    # 更新哈希对象，使用 UTF-8 编码的字符串
    md5_hash.update(input_string.encode("utf-8"))

    # 返回十六进制格式的哈希值
    return md5_hash.hexdigest()


# 输入字符串
input_data = "adid=_a2q8_aq28zqa2iggh268_ugX8_qavIN_a2q8_aq28_qa28qAapp_version=2.39.0.1ban_filterid=3city=深圳condition_version=V4_20230412from=appstoreis_close_individual=0mfg=Applenid=9194983260603746823ntsts=1os=iosos_version=15.8.3sid=177995_1-103916_3-999993_2-105949_6-999990_2-999992_1-999991_1-999999_71-999989_1-999988_1temp_phone_model=iPhone9,1token=2_10af3945b780e8289ebf7ba2110702aets=1757049217ua=750_1334_iphone_2.39.0.1_0zid=NXFhQ4GBgYIAAAADVAP6FG8BawJl8Wgg_AohDy5UBUKzuefjsLXn4OO25eWyteKxsuO34LPi5OS5see3trS3t2V6TVZWAAAAAGi6cYEPdSIQHQi84"

# 生成并打印 MD5 哈希值
md5_result = generate_md5(input_data)
print(f"MD5 Hash: {md5_result}")
