#coding:utf-8
__author__ = 'Mr. null'

import unittest
from ddt import ddt,data
from common.req_api import SendRequests
from common.read_Xls import ReadExcel
import os
import json

path = os.path.dirname(os.getcwd())+"\\data\\data_door.xlsx"
testData = ReadExcel.readExcel(path,"Sheet1")

@ddt
class Test_Door(unittest.TestCase):

    def setUp(self):
        path = os.path.dirname(os.getcwd())+"\\data\\data_init.xlsx"
        testData = ReadExcel.readExcel(path,"Sheet1")
        login_resp = SendRequests().sendRequests(testData[0])
        print(login_resp)
        resp_json = json.loads(login_resp.text)
        self.header = {"Authorization": "Bearer "+resp_json['token']}

    @data(*testData)
    def test_door(self,data):
        resp = SendRequests().sendRequests(data,header=self.header)
        expect_result1 = data["expect_result"].split(":")[1]
        print('expect_result1',expect_result1)
        #转换为字符串
        expect_result = eval(expect_result1)
        self.assertEqual(resp.json()["code"], expect_result, "返回错误,实际结果是%s"%resp.json()["code"])

    def tearDown(self):
        print('end testing....')

if __name__ == '__main__':
    unittest.main(verbosity=2)
