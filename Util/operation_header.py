#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
from Util.operation_json import OperationJson
import os
from  Util.operation_token import Operation_Token

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
file_path8 = os.path.join(path, "Config", "header.json")
file_path7 = os.path.join(path, "Config", "save.json")


class Operation_Header():
    def __init__(self):
        self.header = OperationJson(file_path8)
        self.token = Operation_Token()

    # 通过配置文件获取header数据--token不变
    def get_header_token(self):
        data = self.header.read_data()
        return data

    # 通过配置文件获取header数据--可以获取最新的token
    def get_header_data(self):
        with open(file_path8,'r') as fp:
            token = self.token.read_token_data()
            token_new = token.replace('\n','')
            data = json.loads(fp.read())
            data["link-token"] = token_new
        return data

    # 写header数据到配置文件json里
    def write_header_data(self, data):
        with open(file_path7, 'a') as fp:
            fp.write(json.dumps(data) + '\n')

    # 执行请求时获取header
    def get_header_for_request(self, response):
        headers = response.headers
        return headers

    # 生成header，由str格式组合成dict格式
    def gen_headers(self, s):
        ls = s.split('\n')
        lsl = []
        ls = ls[1:-1]
        headers = {}
        for l in ls:
            l = l.split(': ')
            lsl.append(l)
        for x in lsl:
            headers[str(x[0]).strip('    ')] = x[1]
        return headers


if __name__ == "__main__":
    op_header = Operation_Header()
    data = op_header.get_header_data()
    print(data)
    print(type(data))
