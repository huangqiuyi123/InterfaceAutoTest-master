#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import os

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
file_path2 = os.path.join(path, "Config", "request.json")
file_path3 = os.path.join(path, "Config", "save.json")
file_path4 = os.path.join(path, "Config", "result.json")
file_path5 = os.path.join(path, "Config", "token.json")


class OperationJson():
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = file_path2
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path, 'r', encoding='utf-8-sig', errors='ignore') as fp:
            # json_data = fp.read()    # 一次性读取文件的内容
            json_data = json.load(fp, strict=False)  # json.load()：从json文件中读取数据
            # json_data = fp.readlines()   # 每次读取一行的内容，fp.readlines()读取全部的内容
            return json_data


    # 根据关键字获取数据
    def get_data(self, key=None):
        if key:
            return self.data[key]
        else:
            return self.data

    # 写json数据
    def write_data(self, data):
        with open(file_path3, 'a') as fp:  # 写操作，在文件末尾追加内容
            # fp.write(json.dumps(data) + '\n')   #json.dumps()：将dict类型的数据转换成str，并写入json文件
            fp.write(data + '\n')


if __name__ == "__main__":
    opjson = OperationJson()
    data = opjson.read_data()

    # write_data = opjson.write_data('{"name":"huangqiuyi"}')
    # print(data["api3/getcourseinfo"])
    print(data,type(data))
