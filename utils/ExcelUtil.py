# -*- coding: utf-8 -*-
import xlrd
import os
from  utils.LoginUtil import my_log
class  ExcelReader:

    #初始化方法用例文件路径 和sheet名称
    def __init__(self,flie_excel,sheet_name):
        self.log = my_log("读取excel sheet名称")
        #判断文件是否存在
        if os.path.exists(flie_excel):
            self.flie_excel = flie_excel
            self.sheet_name = sheet_name
            self._data = list()
        else:
            raise  FileNotFoundError("文件不存在")

    #读取excel 表格
    def data(self):
        #创建workbook对象
        work = xlrd.open_workbook(self.flie_excel)
        #判断读取sheet_name的方式
        if type(self.sheet_name) not in [str,int]:
            self.log.error("读取sheet错误")

        elif type(self.sheet_name) == str:
            sheet = work.sheet_by_name(self.sheet_name)

        elif type(self.sheet_name) == int:
            sheet = work.sheet_by_index(self.sheet_name)
        #获取首行
        title = sheet.row_values(0)
        #循环其他行数数据 和第0行拼接字典 key value

        for line in range(1,sheet.nrows):
            col_value =sheet.row_values(line)
            #拼接
            self._data.append(dict(zip(title,col_value)))
        return self._data

if __name__ == '__main__':
    excel = ExcelReader("../data/testdata.xlsx","美多商城接口测试")
    e = excel.data()
    print(e)