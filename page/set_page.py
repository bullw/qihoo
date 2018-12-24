import os,sys
sys.path.append(os.getcwd())
import pytest
from base.base_action import Base_action
import base
import yaml
def data_yaml():
    with open("./data/data_setting.yaml", "r") as f:
        data = yaml.load(f)
        return data.get('data')

class Seting(Base_action):

    def __init__(self, driver):
        Base_action.__init__(self, driver)
    # 点击搜索
    def set_serch(self):
        self.set_click(base.set_search)
    # 搜索框输入搜索

    def set_send(self, content):
        self.set_sendkeys(base.set_text, content)
    def set_back(self):
        self.set_click(base.set_back)

