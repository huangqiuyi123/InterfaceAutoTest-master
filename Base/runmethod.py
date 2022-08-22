#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import json
import datetime

class RunMethod():
    def post_main(self,url,data,header=None):
        res=None
        if header != None:
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print("当前时间：", time)
            res = requests.post(url=url,data=json.dumps(data),headers=header,verify=True).json()
        else:
            res = requests.post(url=url,data=data,verify=False).json()
        return res


    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header,verify=True).json()
        else:
            res = requests.get(url=url, data=data, verify=False).json()
        return res


    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__ == "__main__":
    method='post'
    # url='https://www-test.linki.ee/api/webapi/user/account/login'
    # data= {"account":"niki","password":"123456"}
    # header = {
    #             "content-type": "application/json",
    #             "link-client": "2",
    #             "link-device": "0_5624864d-376a-45ce-bc61-69e43331e6fc",
    #             "link-lang": "en-US",
    #             "link-token": ""
    #         }
    url = 'https://www-test.linki.ee/api/webapi/link/save'
    data = {'linkId': '0', 'title': '', 'url': '', 'type': 1}
    header = {'content-type': 'application/json', 'link-client': '2', 'link-device': '0_5624864d-376a-45ce-bc61-69e43331e6fc',
     'link-lang': 'en-US',
     'link_token': '7b226964223a302c22636970686572223a22636563666666306438656634623961373761373433633365353434346464663837393230666432316231373132623835663232316138333332336564636636373836336136663136393161333638643163343438613931313930613739316663376636643937323538653366373163393563313030623738386566343466303361316338633231633635353939623864383635613263643631633964313361633262626438316232353633663263656638626161666333613739666533306635227d'}

    rm = RunMethod()
    data= rm.run_main(method=method,url=url,data=data,header = header)
    print(data)

