# coding=utf-8
import allure
import pytest


class Test01():
    @allure.step("测试步骤001")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test01(self):
        allure.attach("描述", "中国是一个美丽的国家")
        print("中国")

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step("测试步骤002")
    def test02(self):
        print("深圳")

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step("测试步骤003")
    def test03(self):
        print("广州")

    @allure.step("测试步骤004")
    def test04(self):
        print("贺州")

    @allure.step("测试步骤005")
    def test05(self):
        allure.attach("描述", "黄宝是一个美丽的乡村")
        print("黄宝")
