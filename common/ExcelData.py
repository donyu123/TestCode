# -*- coding: utf-8 -*-
from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import ExcelConfig
class ExcelData:

    def __init__(self,flie_excel,sheet_name):
        self.excel = ExcelReader(flie_excel,sheet_name).data()

    #查找根据 是否运行字段 筛选用例
    def to_run_case(self):
        run_list = list()
        for run_case in self.excel:
            if run_case[ExcelConfig.is_run]  == "y":
                #把得到的用例放到列表内
                run_list.append(run_case)
        return run_list

    #查找全部用例
    def run_case(self):
        run_list = list()
        for run_case in self.excel:
            run_list.append(run_case)
        return run_list

    #获取前置用例条件
    def  get_run_pre(self,pre):
        #调用已经获取全部用例的方法
        run_list = self.run_case()
        #循环全部用例
        for line in run_list:
            #判断当前用例是否包含对应的前置条件
            if  pre in dict(line).values():
                return line
        return None

# if __name__ == '__main__':
#     excel = ExcelData("../data/testdata.xlsx","美多商城接口测试")
#     e =excel.to_run_case()
#
#     print(e)