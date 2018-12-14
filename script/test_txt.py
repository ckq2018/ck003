"""
操作：
1. 新建测试模块(test_页面对象.py)
2. 类名(使用大驼峰去掉下划线)
3. 不用过脑(def setup_class teardown_class test_login)编写三个方法
    setup_class
        1. 实例化 page页面对象
    teardown_class
        1. 关闭 driver对象
    test_login()
        1.根据操作步骤调用page对象内方法

"""
# 解决路径问题
import sys
import os

from base.read_txt import ReadTxt

sys.path.append(os.getcwd())

from base.base_yaml import BaseYaml


def get_data():
    # 新建空列表
    list = []
    # 遍历字典中的值,然后添加到空列表中
    for datas in ReadTxt("data.txt").read_txt():
        list.append(tuple(datas))
        list.append(tuple(datas))
    # 将列表返回
    return list


import pytest

from base.get_driver import get_driver
from page.page_login import PageLogin


class TestLogin():

    # 实力化page对象
    def setup_class(self):
        self.login = PageLogin(get_driver())

    # 关闭driver对象
    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("usernames, password", get_data())
    def test_login(self, usernames, password):
        self.login.page_username(usernames)
        self.login.page_pwd(password)
        self.login.page_click()
