#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests
import json
import os
from Util.operation_json import OperationJson

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
file_path4 = os.path.join(path, "Config", "token.json")
file_path5 = os.path.join(path, "Config", "save.json")


class Operation_Token():
    def __init__(self, file_path=None):
        # self.response = json.loads(response)
        self.op_json = OperationJson()


    # 通过登录获取token
    def get_token_for_login(self):
        url = 'https://www-test.linki.ee/api/webapi/user/account/login'
        data = {"account": "niki", "password": "123456"}
        headers = {
            "content-type": "application/json",
            "link-client": "2",
            "link-device": "0_5624864d-376a-45ce-bc61-69e43331e6fc",
            "link-lang": "en-US",
            "link-token": ""
        }
        try:
            res = requests.post(url=url, data=json.dumps(data), headers=headers).json()
            # res = requests.get(url)
            token = res["data"]["token"]
            return token
        except Exception as err:
            print('获取cookie失败：\n{0}'.format(err))


    # 执行请求时获取token
    def get_token_for_request(self, response):
        token = response["data"]["token"]
        return token

    # 通过配置文件获取token数据-- 取最后一个token
    def read_token_data(self):
        with open(file_path4, 'r') as fp:
            tokens = fp.readlines()
            if len(tokens) == 0:
                return ''
            else:
                token_new = tokens[-1]
                return token_new

    # 根据关键字key获取配置文件里的token数据
    def get_token_value(self, key=None):
        return self.op_json.get_data(key)

    # 从响应数据中提取出token，再将token数据写入token.json里
    def write_token_data(self, data):
        with open(file_path4, 'a') as fp:
            token = json.loads(data)["data"]["token"]
            fp.write(token + '\n')

    # 将登录时获取到的token数据写入配置文件里
    def write_token_data_login(self):
        self.write_token_data(self.get_token_for_login())


if __name__ == "__main__":
    # method = 'post'
    # url = 'https://www-test.linki.ee/api/webapi/user/account/login'
    # data = {"account": "niki", "password": "123456"}
    # header = {
    #     "content-type": "application/json",
    #     "link-client": "2",
    #     "link-device": "0_5624864d-376a-45ce-bc61-69e43331e6fc",
    #     "link-lang": "en-US",
    #     "link-token": ""
    # }
    # res = requests.get(url)
    opjson = Operation_Token()
    data = opjson.read_token_data()
    print(data)
