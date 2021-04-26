# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-04-25
import unittest

from ddt import ddt, data, unpack

from config.VarConfig import excelpath
from utils.exceltools import Excel_tools

ex = Excel_tools()
ex.read_work_book(excelpath)
ex.read_work_sheet('Sheet1')
num = ex.get_max_col()
value = ex.get_all_dic_data()
lst = []
for i in value.values():
    lst.append(i)
@ddt
class TestExample0428(unittest.TestCase):
    def setUp(self):
        print('开始')
    def tearDown(self):
        print('结束')

    @data(*lst)
    @unpack
    def test_dict(self,Id,scene,username,password,is_executed,except_result,test_result):
        print(Id,scene,username,password,is_executed,except_result,test_result)

# @ddt #装饰测试类 unittest.TestCase的子类
# class TestAdd(unittest.TestCase):
#     @data(*[{'a':0,'b':0,'expected':0},{'a':1,'b':1,'expected':2}])
#     #@unpack#字典进行拆分（针对每一条用例的数据进行拆分）
#     def test_add_dict(self,a):
#         print(a)