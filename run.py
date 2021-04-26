# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-04-25
import os
import unittest
import time

from config.VarConfig import reportpath
from utils.ClassicHTMLTestRunner import HTMLTestRunner
from config.VarConfig import auth_code
from utils.send_mail import SendMail
#自动收集测试用例


testcase = unittest.defaultTestLoader.discover('case','test_*.py')

#自动运行case并生成报告 htmltestrunner
filePath = reportpath
title = '测试报告'
tester = 'beier'

with open(filePath,'wb') as f:
    runner =HTMLTestRunner(stream=f,title=title,tester=tester)
    runner.run(testcase)

# mail = SendMail('smtp.163.com')
# send_address = "beier0917@163.com"
# send_password = auth_code
# receive_address = ['953564459@qq.com', '2482821110@qq.com']
# title = "测试报告"
# content = "测试报告在附件中"
# attachfilepath = reportpath
# mail.send_mail(send_address, send_password, receive_address, title, content, file=attachfilepath)
