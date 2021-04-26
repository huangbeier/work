from selenium.webdriver.support.ui import WebDriverWait

def new_find_element(driver, locator):
    """
        方法名：动态查找元素:显式等待
        参数：
            driver: 浏览器的句柄/把柄
            locator: 元素定位方式
                格式： 
                    - ("id", "username")
                    - ("name", "username")
                    - ("class name", "username")
                    - ("xpath", "username")
                    - ("css selector", "username")
                    - ("link text", "username")
                    - ("partial link text", "username")
            timeout: 超时间时间，默认10
        返回值：
            - 找到元素：返回元素
            - 没找到元素：直接报错
    """
    try:
        return WebDriverWait(driver, 30).until(lambda s: s.find_element(*locator))
    except Exception as e:
        raise e