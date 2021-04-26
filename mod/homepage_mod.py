# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-04-11

from obj.homepage_obj import Homepage_obj
from selenium import webdriver
class Homepage_mod:


    def login(self,driver,username1,password1):
        h_obj=Homepage_obj(driver)
        h_obj.to_iframe()
        h_obj.input_username(username1)
        h_obj.input_password(password1)
        h_obj.click_login_btn()
        driver.switch_to.default_content()

    def exit_login(self,driver):
        h_obj = Homepage_obj(driver)
        h_obj.to_iframe()
        h_obj.clear_username()
        driver.switch_to.default_content()



if __name__ == '__main__':
    path = r'F:\0411\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get('https://mail.163.com')
    driver.maximize_window()
    h_mod=Homepage_mod()
    h_mod.login(driver)
