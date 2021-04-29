# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-04-25
import time
import unittest
from ddt import ddt, data, unpack

from config.VarConfig import excelpath, Chromepath, test_url, elementLocationPath
from mod.homepage_mod import Homepage_mod
from obj.homepage_obj import Homepage_obj
from utils.exceltools import Excel_tools
from selenium import webdriver
from utils.logg import Loggings
from utils.seleniumtools import new_find_element
import configparser
from loguru import logger


loggings = Loggings()
ex = Excel_tools()
ex.read_work_book(excelpath)
ex.read_work_sheet('Sheet1')
num = ex.get_max_col()
value = ex.get_all_dic_data()
lst = []
for i in value.values():
    lst.append(i)





@ddt
class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod=Homepage_mod()
        cls.driver=webdriver.Chrome(Chromepath)
        cls.obj=Homepage_obj(cls.driver)
        cls.conf=configparser.ConfigParser()
        cls.conf.read(elementLocationPath)

    def setUp(self):
        self.driver.get(test_url)
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @logger.catch
    @data(*lst)
    @unpack
    def test_login(self,Id,scene,username,password,is_executed,except_result,test_result):
        if is_executed == 'y':
            self.mod.login(self.driver,username,password)
            try:
                time.sleep(1)
                assert self.driver.title == except_result
                print(self.driver.title)
                ex.write_specific_data(Id+1,num,'pass')
            except Exception as e:
                ex.write_specific_data(Id + 1, num, 'fail')
                print(self.driver.title)
                raise e




if __name__ == '__main__':
    unittest.main()
    t=Test_login()
    loggings.info(t.test_login)

