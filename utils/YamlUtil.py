# -*- coding: utf-8 -*-
import  os
import yaml
class YamlReader:
    def __init__(self,yaml):
        #判断yaml文件是否存在
        if os.path.exists(yaml):
            self.yaml = yaml
        else:
            raise  FileNotFoundError("文件不存在")
        self._data = None
        self._data_all =None
    #读取单个文件
    def data(self):
        #判断文件是不是第一次打开读取yaml文件 不是就返回之前打开的结果
        if  not self._data:
            with open(self.yaml,"rb")as f:
                self._data = yaml.safe_load(f)
        return self._data

    #读取多个文件 返回的是多个文档要用list列表包住并返回
    def data_all(self):
        if not self._data_all:
            with open(self.yaml,"rb")as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all

if __name__ == '__main__':
    yaml = YamlReader("yaml路径").data()
    print(yaml["BASE"]["test"]["url"])