#coding:utf-8
__author__ = 'Mr. null'

import xlrd

class ReadExcel():
     def readExcel(fileName,SheetName="Sheet1"):
         data = xlrd.open_workbook(fileName)
         table = data.sheet_by_name(SheetName)

         #获取总行数
         nrows = table.nrows
         if nrows > 1:
             #获取第一列的内容，列表格式
             keys = table.row_values(0)

             listData = []
             for col in range(1,nrows):
                 values = table.row_values(col)
                 api_dict = dict(zip(keys, values))
                 listData.append(api_dict)
             return listData
         else:
             print("表格无数据")
             return None

if __name__ == '__main__':
    print('read xls')



