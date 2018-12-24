from appium import webdriver

# def base_in():
#     desired_caps = {}
#     # 设备信息
#     desired_caps['platformName'] = 'Android'  # 平台名称
#     desired_caps['platformVersion'] = '5.1'  # 平台版本
#     desired_caps['deviceName'] = '192.168.56.101:5555'  # 设备号
#     # app信息
#     desired_caps['appPackage'] = 'com.android.settings'  # 应用的包名
#     desired_caps['appActivity'] = '.Settings'  # 代表启动的activity
#
#     return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 声明driver对象
def init_driver():
    # 前置代码
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)