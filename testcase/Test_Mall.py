# -*- coding: utf-8 -*-
from  utils.RequestUtil import Request
from  config.Config import Config
from  utils.LoginUtil import my_log
from  utils.MysqlUtil import Mysql
from  utils.AssertUtil import AssertUtil
log = my_log("日志")
def login():
    log.info("登录请求")
    con = Config().yaml_url()
    url = con+"/authorizations/"
    data = {"username":"python","password":"12345678"}
    req = Request()
    r=req.post(url,json=data)
    #数据验证
    # mysql = Mysql()
    # my = mysql.execute("select id,username from tb_users where username='python'")
    # body =r["body"]["user_id"]
    # assert  my["id"] ==body
    # print(my)
    print(r)
    #断言验证状态码是否相等
    ass = AssertUtil()
    # ass.assert_code(r["code"],200)
    # ass.assert_body(r["body"],"")
    #验证是否包含
    body=r["body"]
    ass.assert_in_body(body,"'username': 'python', 'user_id': 1")


# login()

st = "hello word"
ass = AssertUtil()
ass.assert_in_body(st, "word")