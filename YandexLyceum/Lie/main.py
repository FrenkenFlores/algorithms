import requests
import json

with open("fraud.json") as f:
    server_param = json.load(fp=f)
items = server_param['from_gold']
suspicious = []
req = requests.request(url=f"http://{server_param['server']}:{server_param['port']}", method="GET")
for i in req.json():
    for item in items:
        if item in i["found"]:
            suspicious.append(i['name'])
            break
print("; ".join(sorted(suspicious)))
