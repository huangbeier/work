# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-04-11
from config.VarConfig import Chromepath, test_url, excelpath,auth_code
from mod.homepage_mod import Homepage_mod
from selenium import webdriver
import time
import unittest
from utils.exceltools import Excel_tools
from ddt import ddt,data,unpack
#不利用unittest进行测试 生成报告
from utils.send_mail import SendMail

#
def login():
    h_mod = Homepage_mod()
    ex=Excel_tools()
    ex.read_work_book(excelpath)
    ex.read_work_sheet('Sheet1')
    num=ex.get_max_col()
    value=ex.get_all_dic_data()

    for i in range(2,len(value)+2):#len(value)+2 是总行数
        driver = webdriver.Chrome(Chromepath)
        driver.get(test_url)
        driver.maximize_window()
        if value[i]['is_executed'].lower() == 'y':
            h_mod.login(driver,value[i]['username'],value[i]['password'])
            time.sleep(2)
            try:
                assert value[i]['except_result'] in driver.page_source
                ex.write_specific_data(i,num,'pass')
            except Exception as e:
                ex.write_specific_data(i, num, 'fail')#断言失败写fail
                print(e)
            driver.quit()







if __name__ == '__main__':
    login()
    from config.VarConfig import auth_code
    mail = SendMail('smtp.163.com')
    data = mail.get_content()
    sender = 'beier0917@163.com'
    receivers = ['953564459@qq.com']
    title = '测试报告'
    content = data
    auth_code = auth_code
    mail.send(title, content, sender, auth_code, receivers)