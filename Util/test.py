# -*- coding:utf-8 -*-
# @Time : 2022/7/24 下午3:52
# @Author : niki
# @File : test.py
# @Software: PyCharm
import os,json,requests
from jsonpath_rw import jsonpath, parse

url = 'https://www-test.linki.ee/api/webapi/user/account/login'
data = {"account": "niki", "password": "123456"}
headers = {
    "content-type": "application/json",
    "link-client": "2",
    "link-device": "0_5624864d-376a-45ce-bc61-69e43331e6fc",
    "link-lang": "en-US",
    "link-token": ""
}

# res = requests.post(url=url, data=json.dumps(data), headers=headers).json()
# print(res)
#
# depend = 'data.token'  # 按响应数据结构编写需要查找的CartId
# json_exe = parse(depend)  # parse用于从一个字符串中解析出json对象
# model = json_exe.find(res)  # 返回的是list,但是不是我们想要的值
# print(model)
# print([match.value for match in model][0])
# # 返回响应参数中CartId的a47141fddd8848e1be5a281b25e613b8



depend_data = "data.linkId"
res_data =  {
  "code": 200,
  "data": {
    "linkId": 4794375685793793,
    "priority": 1659255491818,
    "status": 1,
    "title": "",
    "type": 1,
    "uid": 2147483717,
    "url": "https://www.baidu.com"
  },
  "msg": "Success"
}
json_exe = parse(depend_data)
model = json_exe.find(res_data)
print([match.value for match in model][0])





