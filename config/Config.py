# -*- coding: utf-8 -*-
import  os
from utils.YamlUtil import YamlReader
#获取项目路径
BASE_PATH =os.path.abspath(__file__)
#获取项目根目录
_dirname = os.path.dirname(os.path.dirname(BASE_PATH))
#获取config路径
yaml_path = _dirname +os.sep+"config"+os.sep+"conf.yml"

#获取report路径
report_path = _dirname +os.sep+"report"
#定义report文件路径
def get_report_path():
    return  report_path

#获取logs路径
logs_path = _dirname + os.sep+"logs\\"

#把获取conf.yaml的路径写入方法内
def  file_yaml_path():
    return yaml_path

#lgos路径方法
def  _logs_path():
    return logs_path

#创建类读取Yaml文件
class Config:
    def __init__(self):
        #读取yam文件把获取的路径写入
        self.con = YamlReader(file_yaml_path()).data()

    #创建读取url的方法
    def yaml_url(self):
        return self.con["BASE"]["test"]["url"]
        # 创建读取url的方法

    #创建读取log后缀的方法
    def log(self):
        return self.con["BASE"]["test"]["log"]
        # 创建读取log后缀方法的方法

    #创建读取log级别的方法
    def log_level(self):
        return self.con["BASE"]["test"]["log_level"]

if __name__ == '__main__':
    c = Config().log_level()
    print(c)