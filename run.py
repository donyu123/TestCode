# -*- coding: utf-8 -*-
from  config.Config import *
import pytest
if __name__ == '__main__':

    # 设置存放allure json文件的路径
    report_path = get_report_path() + os.sep + "result"
    # 设置生成日志报告的html 路径
    report_html = get_report_path() + os.sep + "html"
    # 执行请求并生成allure json 文件
    pytest.main(["-s","--alluredir", report_path])