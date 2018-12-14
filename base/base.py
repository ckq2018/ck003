"""
base 目录放公共部分
1. 找元素封装
2. 输入方法封装
3. 点击方法封装
"""
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 初始化driver
    def __init__(self, driver):
        self.driver = driver

    # 封装定位元素
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 封装输入方法
    def base_input(self, loc, value):
        # 先获取元素
        values = self.base_find(loc)
        # 清空输入框的内容,不管有没有,输入内容前都要清空
        values.clear()
        # 输入内容
        values.send_keys(value)

    # 封装点击方法
    def base_click(self, loc):
        self.base_find(loc).click()
