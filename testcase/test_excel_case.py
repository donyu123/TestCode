# -*- coding: utf-8 -*-
from common.ExcelData import ExcelData
from  config.Config import *
from  config.Config import Config
from common.ExcelConfig import ExcelConfig
from  utils.RequestUtil import Request
from  common.Base import json_data,res_find,res_sub,params_find,allure_report
from utils.LoginUtil import my_log
import pytest
import  allure
log = my_log()
#读取测试用例
excel = ExcelData("D:\\InterfaceTest\\data\\testdata.xlsx","美多商城接口测试")
#获取可执行用例
data_case=excel.to_run_case()
print(data_case)
#获取yaml文件路径
con = Config().yaml_url()
class Test_case:

    def  run_api(self,url,method,params=None,header=None,cookie=None):
       reqest = Request()
       params = json_data(params)
       if str(method).lower() == "get":
           res = reqest.get(url, json=params, headers=header, cookies=cookie)
       elif str(method).lower() == "post":
           res = reqest.post(url, json=params, headers=header, cookies=cookie)
       else:
           log.error("I like you")
           # print(res)
       return res


    # 执行前置用例
    def  run_pre(self,pre_res):
        #获取前置用例
        url = con + pre_res[ExcelConfig.url]
        method = pre_res[ExcelConfig.method]
        params = pre_res[ExcelConfig.params]
        headers = pre_res[ExcelConfig.headers]
        cookies = pre_res[ExcelConfig.cookies]
        # print(params)
        # 判断headers cookise是否存在，json转义，
        header = json_data(headers)
        cookie = json_data(cookies)
        res= self.run_api(url,method,params,header,cookie)
        return res


    @pytest.mark.parametrize("case",data_case)
    def test_run(self,case):
        case_id = case[ExcelConfig.case_id]
        case_model = case[ExcelConfig.case_model]
        case_name = case[ExcelConfig.case_name]
        pre_exec = case[ExcelConfig.pre_exec]
        method = case[ExcelConfig.method]
        params_type = case[ExcelConfig.params_type]
        params = case[ExcelConfig.params]
        expect_result = case[ExcelConfig.expect_result]
        actual_result = case[ExcelConfig.actual_result]
        headers = case[ExcelConfig.headers]
        cookies = case[ExcelConfig.cookies]
        code = case[ExcelConfig.code]
        db_verify = case[ExcelConfig.db_verify]

        #判断当前用例是否有前置用例
        if pre_exec:
           data_pre = excel.get_run_pre(pre_exec)
           #执行前置用例
           pre_res= self.run_pre(data_pre)
           print(pre_res)
           headers, cookies = self.get_correlation(headers, cookies, pre_res)

        url = con + case[ExcelConfig.url]
        print(url)
        header = json_data(headers)
        cookie = json_data(cookies)
        res= self.run_api(url,method,params,header,cookie)
        print(res)

        #allure
        #获取模块story 二级标签
        allure.dynamic.feature(case_model)
        #获取用例id和接口名称
        allure.dynamic.story(case_id+case_name)
        #设置备注 有请求的url 请求类型  期望结果 实际结果
        desc ="<font color = 'red'>请求的url1:{}</font></Br>" \
              "<font color = 'red'>请求类型:{}</font></Br>" \
              "<font color = 'red'>期望结果:{}</font></Br>" \
              "<font color = 'red'>实际结果:{}</font></Br>".format(url,method,expect_result,res)


        allure.dynamic.description(desc)
        return res

    def get_correlation(self,headers, cookies, pre_res):
        if len(headers):
            headers_data = pre_res["body"]["token"]
            # 结果替换
            headers = res_sub(headers, headers_data)
        if len(cookies):
            cookies_data = pre_res["body"][""]
            # 结果替换
            cookies = res_sub(headers, cookies_data)
        return headers,cookies
if __name__ == '__main__':
    #设置存放allure json文件的路径
    report_path =get_report_path()+os.sep+"result"
    #设置生成日志报告的html 路径
    report_html = get_report_path()+os.sep+"html"
    #执行请求并生成allure json 文件
    pytest.main(["-s","test_excel_case.py","--alluredir",report_path])

    #调用生成报告方法 转换成html
    allure_report(report_path,report_html)