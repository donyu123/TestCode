# -*- coding: utf-8 -*-
import json
from utils.LoginUtil import my_log
import  re
import subprocess
p_data = '\\${(.*)}\\$'
#日志
log = my_log()
def  json_data(data):
    return  json.loads(data) if data else data


#进行字段替换
def res_find(headers,cookies,data, pattern_data=p_data):
    if "${" in headers:
        pattern = re.compile(pattern_data)
        pattern.findall(data)
    if "${" in cookies:
        pattern = re.compile(pattern_data)
        pattern.findall(data)
    log.info("替换过后的值是{}".format(headers))
    return headers,cookies

# def res_find(data, pattern_data=p_data):
#     pattern = re.compile(pattern_data)
#     re_res = pattern.findall(data)
#
#     log.info("替换过后的值是{}".format(re_res))
#     return re_res


#替换
def res_sub(data,replace,pattern_data=p_data):

    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    # print("data的是值是", data)
    # print("replace的值是",replace)
    if re_res:
        return re.sub(pattern_data,replace,data)
    return re_res

#验证是heander是否包含
def params_find(headers,cookies):
    log.info("heanders的值是：{} cookies的值是：{}".format(headers,cookies))
    if "${" in headers:
        headers = res_find(headers)
    if "${" in cookies:
        cookies = res_find(cookies)
    return headers,cookies


#执行allure命令
def allure_report(report_path,report_html):
    allure_cmd = "allure generate {} -o {} --clean".format(report_path,report_html)
    try:
        subprocess.call(allure_cmd,shell=True)
    except:
        log.error("生成失败")
        raise
