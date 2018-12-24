import os, sys
# 通过sys获取系统的环境
import allure

sys.path.append(os.getcwd())
import pytest
import yaml
import time
from base.base_driver import init_driver
from page.set_page import Seting
def data_yaml():
    with open("./data/data_setting.yaml", "r") as f:
        data = yaml.load(f)
        return data.get('data')


class Test_Android:

    def setup_class(self):
        self.driver = init_driver()
        self.set_page = Seting(self.driver)

    def teardown_class(self):
        time.sleep(5)
        # 关闭app driver对象不会关闭
        self.driver.close_app()
        # 关闭驱动对象
        self.driver.quit()

    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("content", data_yaml())
    def test_one(self, content):
        self.set_page.set_serch()
        self.set_page.set_send(content)
        self.set_page.set_back()
        print("\n阁下何不乘风起,扶摇之上九万里")





