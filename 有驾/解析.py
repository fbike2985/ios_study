import json
with open("response_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

ddata=data["data"]
print(ddata)
data_14001=ddata["14001"]
print(data_14001)
itemlist=data_14001["itemlist"]
items=itemlist["items"]
for item in items:
    print(item["id"])
