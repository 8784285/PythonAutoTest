# -*- coding:utf-8 -*-

import requests
import json

class SendRequests():

    def sendRequests(self,Data,header=''):
        '''
        从表格中获取测试数据作为参数值发送
        '''
        method = Data["method"]
        url = Data["url"]
        if Data["params"] == "":
            param = None
        else:
            param = eval(Data["params"])

        if Data["body"] == "":
            body_data = None
        else:
            body_data = eval(Data["body"])

        #发送请求
        if method == 'get':
            resp = requests.get(url=url,headers=header,params=param)
        elif method == 'post':
            resp = requests.post(url=url,headers=header,data=json.dumps(body_data))
        return resp

if __name__ == '__main__':
    print('start testing...')