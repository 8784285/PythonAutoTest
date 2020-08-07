#coding:utf-8
__author__ = 'Mr. null'
import unittest
import time
import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))  #当前文件绝对路径
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")  #项目的根目录
sys.path.append(root_path)  #项目的根目录通过sys.path.append添加为执行时的环境变量

from common.HTMLTestRunner import HTMLTestRunner

def run_case(dir = "testcase"):
    case_dir = os.path.dirname(os.getcwd()) + "\\" + dir
    # test_case = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py")
    return discover

if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #htmlreport = os.path.dirname(os.getcwd()) + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    htmlreport = os.path.dirname(os.getcwd()) + "\\report\\" + r"\report.html"
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner(stream=fp, title="自动化测试报告", description='测试用例执行情况',verbosity=2)
    runner.run(run_case())
    fp.close()
