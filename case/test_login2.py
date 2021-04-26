# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-04-25
import time
import unittest
from ddt import ddt, data, unpack

from config.VarConfig import excelpath, Chromepath, test_url
from mod.homepage_mod import Homepage_mod
from obj.homepage_obj import Homepage_obj
from utils.exceltools import Excel_tools
from selenium import webdriver
from utils.logg import Loggings


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
    def setUp(self):
        self.driver.get(test_url)
        self.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    @data(*lst)
    @unpack
    def test_login(self,Id,scene,username,password,is_executed,except_result,test_result):

        if is_executed == 'y':
            #self.mod.exit_login(self.driver)
            self.mod.login(self.driver,username,password)
            time.sleep(2)
            try:
                self.assertIn(except_result,self.driver.page_source)
                ex.write_specific_data(Id+1,num,'pass')
                #self.driver.delete_all_cookies()
                #time.sleep(2)
            except Exception as e:
                ex.write_specific_data(Id + 1, num, 'fail')
                raise e
        # self.mod.exit_login(self.driver)



if __name__ == '__main__':
    unittest.main()
    loggings.info(Test_login)
