# @Author ：黄贝尔
# @Time ：2021/2/7__13:40
# #coding:utf-8
from utils.seleniumtools import new_find_element
from selenium.webdriver import ActionChains
class page(object):
    def __int__(self,driver):
        self.driver=driver
        # self.url=url
        #self.timeout=30

    def input_text(self,loc,text):
        new_find_element(self.driver,loc).send_keys(text)

    def click(self,loc):
        new_find_element(self.driver,loc).click()

    def action(self,loc):
        ActionChains(self.driver).move_to_element(new_find_element(self.driver,loc)).perform()  # 鼠标悬停到XX元素

    def new_page(self):
        self.driver.switch_to_window(self.driver.window_handles[-1]) # 切换到最新的网页

    def roll_to_element(self,num): #向下滚动X像素
        self.driver.execute_script(f'window.scrollBy(0,{num})')

    def clear_loc(self,loc):#清空输入框
        new_find_element(self.driver, loc).clear()

    def to_iframe(self,loc):
         self.driver.switch_to.frame(new_find_element(self.driver,loc))

    # def get_text(self,loc):#获取隐藏文本
    #     new_find_element(self.driver, loc).get_attribute('textContent')

