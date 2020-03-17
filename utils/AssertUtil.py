# -*- coding: utf-8 -*-
from  utils.LoginUtil import my_log
import json
class AssertUtil:

    def __init__(self):
       self.log = my_log("断言验证")

    #判断状态码是否相对
    def assert_code(self,code,expected_code):
        try:
            assert  int(code) == int(expected_code)
            return True
        except:
            self.log.error("{}{}状态码错误".format(code,expected_code))
            raise

    #判断body是否相等
    def assert_body(self,body,expected_body):
        try:
            assert  body == expected_body
            return True
        except:
            self.log.error("{}{}内容不相等".format(body,expected_body))
            raise

    #判断返回结果是否包含期望结果
    def assert_in_body(self,body,expected_body):
        try:
            body=json.dumps(body)
            assert expected_body in body
            return  True
        except:
            self.log.error("不包含错误{}{}".format(body,expected_body))
            raise

