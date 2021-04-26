# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-04-11

import configparser
from utils.seleniumtools import new_find_element
from config.VarConfig import elementLocationPath

class Homepage_obj:
    def __init__(self,driver):
        self.driver=driver
        self.conf=configparser.ConfigParser()
        self.conf.read(elementLocationPath)



    def to_iframe(self):
        i_frame = self.conf.get('homepage','homepage.frame')
        self.driver.switch_to.frame(new_find_element(self.driver, i_frame.split(':')))

    def input_username(self,username1):
        username=self.conf.get('homepage','homepage.username')
        new_find_element(self.driver,username.split(':')).send_keys(username1)

    def input_password(self,password1):
        password=self.conf.get('homepage','homepage.password')
        new_find_element(self.driver,password.split(':')).send_keys(password1)

    def click_login_btn(self):
        login_btn = self.conf.get('homepage', 'homepage.login_btn')
        new_find_element(self.driver, login_btn.split(':')).click()

    def clear_username(self):
        username = self.conf.get('homepage', 'homepage.username')
        new_find_element(self.driver,username.split(':')).clear()

    def is_validation(self):
        validation=self.conf.get('homepage','homepage.validation')
        new_find_element(self.driver,validation.split(':'))




if __name__ == '__main__':
    # path = r'F:\0411\chromedriver.exe'
    # driver = webdriver.Chrome(path)
    # driver.get('https://mail.163.com')
    # driver.maximize_window()
    conf = configparser.ConfigParser()
    conf.read(r'F:\0411\config\config.ini')
    i_frame = conf.get('homepage', 'homepage.frame')
    #new_find_element(self.driver, tuple(i_frame))
    print(i_frame.split(','))