#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import os
import requests
import json
import operator

base_path = os.getcwd()
sys.path.append(base_path)
from deepdiff import DeepDiff
from Base.runmethod import RunMethod
from Util.operation_excel import HandExcel
from Util.operation_init import HandleInit
from Util.get_data import GetData
from Util.dependent_data import DependentData
from Util.operation_token import Operation_Token
from Util.operation_header import Operation_Header
from Util.operation_result import Operation_Result
from Util.operation_json import OperationJson
from Util.send_email import SendEmail
from Util.connect_db import OperationMysql


class RunMain():
    def __init__(self):
        self.run = RunMethod()
        self.excel = HandExcel()
        self.hi = HandleInit()
        self.data = GetData()
        self.token = Operation_Token()
        self.header = Operation_Header()
        self.result = Operation_Result()
        # self.mysql = OperationMysql()
        self.email = SendEmail()

    def run_case(self):
        pass_count = []
        fail_count = []
        leavel = []
        pass_caseid = []
        fail_caseid = []
        rows = self.excel.get_rows()

        for i in range(rows):
            print('当前正在执行第%d次遍历' % (i + 1))
            if i == rows - 1:
                print('遍历结束')
            data = self.excel.get_rows_value(i + 2)
            is_run = data[2]
            if is_run == 'yes':
                case_id = data[0]
                case_name = data[1]
                is_depend = data[3]
                depend_data = data[4]
                depend_key = data[5]
                url = data[6]
                method = data[7]
                request_data_key = data[8]
                request_data = self.excel.get_data_for_json(i + 1)
                token_method = data[9]
                is_header = data[10]
                header = self.header.get_header_data()
                expect_method = data[11]
                expect_result = data[12]
                actual_result = data[13]
                daily_data = data[14]

                if is_depend:
                    # ！！！这里的传的caseid不正确，执行的数据不是拿到依赖的用例数据
                    self.dependt_data = DependentData(is_depend)
                    depend_response_data = self.dependt_data.get_data_for_key(i)
                    depent_key = self.data.get_depend_field(i)
                    request_data[depent_key] = depend_response_data


                elif token_method == 'yes':
                    response = self.run.run_main(method, url, request_data, header)

                elif token_method == 'write':
                    response = self.run.run_main(method, url, request_data, header)
                    # tokens = response.tokens
                    self.token.write_token_data(response)

                elif is_header == 'yes':    # 如果需要传header，先获取再运行
                    response = self.run.run_main(method, url, request_data, header)

                elif is_header == 'write':   # 运行后写入头部
                    response = self.run.run_main(method, url, request_data, header)
                    headers = self.header.get_header_for_request(response)
                    self.header.write_header_data(headers)


                else:
                    response = self.run.run_main(method, url, request_data, header)

                res = json.loads(response)
                if res["code"] == 200:
                    desc = res['msg']
                    code = res['data']
                else:
                    print(res)

                if expect_method == 'message':
                    data = self.excel.split_data_two(expect_result)
                    url_key = data[0]
                    exp_data = data[1]
                    expect_data = self.result.get_result_desc(url_key, exp_data)

                    if expect_data == desc:
                        self.excel.excel_write_data(i + 2, 14, '通过')
                        pass_count.append(i)
                        pass_caseid.append(case_id)
                    else:
                        self.excel.excel_write_data(i + 2, 14, '失败')
                        self.excel.excel_write_data(i + 2, 15, json.dumps(res))
                        fail_count.append(i)
                        fail_caseid.append(case_id)

                if expect_method == 'status_code':
                    if int(expect_result) == code:
                        self.excel.excel_write_data(i + 2, 14, '通过')
                        pass_count.append(i)
                        pass_caseid.append(case_id)
                    else:
                        self.excel.excel_write_data(i + 2, 14, '失败')
                        self.excel.excel_write_data(i + 2, 15, json.dumps(res))
                        fail_count.append(i)
                        fail_caseid.append(case_id)

                if expect_method == 'json':

                    except_result_data = self.result.get_key_result(expect_result)
                    result = self.result.operation_result_json(except_result_data, res)
                    if result:
                        self.excel.excel_write_data(i + 2, 14, '通过')
                        pass_count.append(i)
                        pass_caseid.append(case_id)
                    else:
                        self.excel.excel_write_data(i + 2, 14, '失败')
                        self.excel.excel_write_data(i + 2, 15, json.dumps(res))
                        fail_count.append(i)
                        fail_caseid.append(case_id)

        self.email.send_main(pass_count, fail_count, pass_caseid, fail_caseid)


if __name__ == "__main__":
    run = RunMain()
    run.run_case()
