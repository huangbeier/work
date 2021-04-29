# @Author ：黄贝尔
# @Time ：2021/4/29__10:21
# #coding:utf-8
from config.VarConfig import excelpath2, Chromepath, test_url
from utils.exceltools import Excel_tools
from selenium import webdriver


def gjz(h_find,ele,vaules):
    driver=webdriver.Chrome(Chromepath)
    driver.get(test_url)
    driver.switch_to.frame(driver.find_element(h_find,ele))
    driver.find_element(h_find,ele).send_keys(vaules)
    driver.find_element(h_find,ele).send_keys(vaules)
    driver.find_element(h_find,ele)

if __name__ == '__main__':
    ex=Excel_tools()
    ex.read_work_book(excelpath2)
    ex.read_work_sheet('Sheet1')
    cols=ex.get_max_col()


    for i in range(2,cols+1):
        val = ex.get_row_data(i)
        gjz(value['h_find'],value['ele'],value['vaules'])


