import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
# from hamcrest import assert_that, close_to
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testapp:
    def setup(self):
            capabilities = {}
            # Android平台测试
            capabilities['platformName'] = 'Android'
            # 测试手机版本为5.0
           # capabilities['platformVersion'] = '5.1.1'
            capabilities['platformVersion'] = '6.0.1'

            capabilities['deviceName'] = '127.0.0.1:7555'
            # 系统手机中的联系人app的包名
            capabilities['appPackage'] = 'com.xueqiu.android'
            # 系统手机中的联系人app的主入口activity
            capabilities['appActivity'] = '.view.WelcomeActivityAlias'
            capabilities['noReset'] = 'true'
            # capabilities["dontStopAppOnReset"] = 'true'
            # 连接测试机所在服务器服务器
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
            self.driver.implicitly_wait(20)

    def teardown(self):
        # 断开连接
       self.driver.quit()

    def test_api(self):
        self.driver.set_network_connection(1)  #设置飞行模式
        time.sleep(3)
        self.driver.set_network_connection(2)	#设置数据连接
        time.sleep(3)
        self.driver.get_screenshot_as_file("./photos/img2.png")


