# -*- coding: utf-8 -*-
import requests
class Request:
    #封装请求
    def request_api(self,url,data=None,json=None,headers=None,cookies=None,method="get"):
        #判断请求是get还是post
        if method =="get":
            r = requests.get(url,data=data,json=json,headers=headers,cookies=cookies)

        elif method =="post":
            r = requests.post(url, data=data, json=json, headers=headers, cookies=cookies)

        #获取返回数据的状态
        code = r.status_code

        #获取返回的数据body如果报错就抛出异常返回文本
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        #把返回的状态码 和数据放到新的字典内
        res = dict()
        res["code"] = code
        res["body"] = body
        return res


    #调用请求对外提供的方法
    def get(self,url,**kwargs):
        return self.request_api(url,method="get",**kwargs)
    def post(self,url,**kwargs):
        return self.request_api(url,method="post",**kwargs)

