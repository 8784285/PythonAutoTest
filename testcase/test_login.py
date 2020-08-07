#coding:utf-8
__author__ = 'Mr. null'

import unittest
from ddt import ddt,data
from common.req_api import SendRequests
from common.read_Xls import ReadExcel
import os

path = os.path.dirname(os.getcwd())+"\\data\\data_login.xlsx"
testData = ReadExcel.readExcel(path,"Sheet1")

@ddt
class Test_Login(unittest.TestCase):

    def setUp(self):
        print('start test...')

    @data(*testData)
    def test_login(self,data):
        print(data)
        resp = SendRequests().sendRequests(data)
        #切割字符串取后面的部分
        expect_result1 = data["expect_result"].split(":")[1]
        print('expect_result1',expect_result1)
        #转换为字符串
        expect_result = eval(expect_result1)
        #print(expect_result)

        self.assertEqual(resp.json()["code"], expect_result, "返回错误,实际结果是%s"%resp.json()["code"])
        #self.assertEqual(re.json()["msg"], expect_result, "返回错误,实际结果是%s"%re.json()["msg"])

    def tearDown(self):
        print('end testing....')

if __name__ == '__main__':
    unittest.main(verbosity=2)
