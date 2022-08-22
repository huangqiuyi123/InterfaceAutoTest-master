#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import operator
from Util.operation_json import OperationJson
from deepdiff import DeepDiff
import os

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# file_path6 = os.path.join(path, "Config", "code_message.json")
file_path = os.path.join(path, "Config", "result.json")

class Operation_Result():

    def __init__(self):
        self.op_result = OperationJson(file_path)
        self.data = self.read_result()

    # 读取result文件
    def read_result(self):
        data = self.op_result.read_data()
        return data

    # 根据关键字获取预期结果json数据
    def get_key_result(self, key=None):
        data = self.op_result.get_data(key)
        new_data = {k: v for (k, v) in data.items()}  # 列表生成式，最后输出格式是key：value
        return new_data

    # 获取预期结果--文本信息
    def get_result_desc(self, url_key, desc):
        res_data = self.op_result.get_data(url_key)
        if res_data != None:
            message = res_data.get(desc)
            if message:
                return message
        return None

        # if data != None:
        #     for i in data:
        #         message = i.get(desc)
        #         if message:
        #             return message
        # return None

    # 获取预期结果--json数据
    def get_result_json(self, url_key, status):
        data = self.op_result.get_data(url_key)
        if data != None:
            for i in data:
                message = i.get(status)
                if message:
                    return message
        return None

    # 判断两个字典是否相等
    def operation_result_json(self, dict1, dict2):
        if isinstance(dict1, dict) and isinstance(dict2, dict):
            cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()  # 对比两个对象内容，ignore_order=True：忽略参数
            if cmp_dict.get("dictionary_item_added"):
                return False
            else:
                return True
        return False

    # 判断一个字符串是否包含在另外一个字符串
    def is_contain(self, str_one, str_two):
        flag = None
        if operator.contains(str_one, str_two):
            flag = True
        else:
            flag = False
        return flag


if __name__ == "__main__":
    dict1 = {"aaa": "AAA", "ccc": "BBBB", "bbb": "A1A", "CC": [{"11": "22"}, {"11": "44"}]}
    dict2 = {"aaa": "AAA", "ccc": "BBBB", "bbb": "A1A", "CC": [{"11": "22"}, {"11": "44"}]}
    dict = {'timestamp': '1507790990179', 'uid': '5249191', 'uuid': '5ae7d1a22c82fb89c78f603420870ad7', 'secrect': 'd9656c6c08b815b8ce069edf36f3df30', 'token': '0c45fea910fc3ff0cc5ed856e5289d25', 'cid': '885'}

    op_result = Operation_Result()
    result = op_result.read_result()
    data = op_result.get_result_desc(dict,"uuid")
    print(result)
    print(type(result))
