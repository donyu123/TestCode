# -*- coding: utf-8 -*-
import  logging
import datetime
from config.Config import _logs_path
from config.Config import Config
#设置对应的日志级别映射
log_l  ={
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}
class Loggin:
    #文件名称 日志级别  日志路径
    def  __init__(self,file_name,log_level,log_path):
        self.file_name = file_name
        self.log_level = log_level
        self.log_path = log_path

        #设置控制台名称
        self.loggre = logging.getLogger(self.file_name)
        #设置级别
        self.loggre.setLevel(log_l[self.log_level])
        #判断henders是否存在
        if not self.loggre.handlers:
            #添加handeler
            fh_stream =logging.StreamHandler()
            #设置日志级别
            fh_stream.setLevel(log_l[self.log_level])
            #设置输出格式
            formatter =logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
            #添加输出格式
            fh_stream.setFormatter(formatter)

            #把日志信息写入文件内
            fh_file = logging.FileHandler(self.log_path)
            #设置日志级别
            fh_file.setLevel(log_l[self.log_level])
            #设置输出格式
            fh_file.setFormatter(formatter)
            #添加handers
            self.loggre.addHandler(fh_stream)
            self.loggre.addHandler(fh_file)


#获取logs文件路径
log =_logs_path()

con_log = Config()

#获取log后缀
_log = con_log.log()

#获取当前时间
data_time = datetime.datetime.now().strftime("%Y-%m-%d")

#拼接一个完整的log文件路径
log_path = log + data_time + _log
# print(log_path)
#获取log日志级别
con_log_log_level = con_log.log_level()
# print(con_log_log_level)

#对外提供掉日志方法
def  my_log(file_name=__file__):
    return Loggin(file_name=file_name,log_level=con_log_log_level,log_path=log_path).loggre

if __name__ == "__main__":
    my_log("日志封装").debug("this is a debug")