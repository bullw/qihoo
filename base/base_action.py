class Base_action():
    # 当类初始化的时候这个方法就执行
    def __init__(self, driver):
        self.driver = driver

    # loc代表一个元祖进来, 返回找到的元素
    def find_element(self, loc):
        return self.driver.find_element(loc[0], loc[1])
    # 定位后点击操作进行封装
    def set_click(self, loc):
        return self.find_element(loc).click()
    # 定位输入框后输入文本进行封装
    def set_sendkeys(self, loc, content):
        return self.find_element(loc).send_keys(content)
