import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class Testapp:
    def setup(self):
            capabilities = {}
            # Android平台测试
            capabilities['platformName'] = 'Android'
            # 测试手机版本为5.0
            capabilities['platformVersion'] = '5.1.1'
            capabilities['deviceName'] = '127.0.0.1:62001'
            # 系统手机中的联系人app的包名
            capabilities['appPackage'] = 'com.android.systemui'
            # 系统手机中的联系人app的主入口activity
            # capabilities['appActivity'] = '.Launcher'
            capabilities['noReset'] = 'True'
            # 连接测试机所在服务器服务器
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
            self.driver.implicitly_wait(8)
    def teardown(self):
        # 断开连接
        self.driver.quit()
    def test_touchactions(self):
        actions = TouchAction(self.driver)
        actions.press(x=243,y=395).move_to("ele1").move_to().move_to().release().perform()
