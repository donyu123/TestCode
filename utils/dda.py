# -*- coding: utf-8 -*-
list1 = ['用例ID', '模块', '接口名称', '请求URL', '前置条件']
list2 = ['请求类型', '请求参数类型', '请求参数', '预期结果']
list3 = list()
list3.append(dict(zip(list1,list2)))
print(list3)