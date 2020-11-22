import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import assert_that, close_to


class Testapp:
    def setup(self):
            capabilities = {}
            # Android平台测试
            capabilities['platformName'] = 'Android'
            # 测试手机版本为5.0
            capabilities['platformVersion'] = '5.1.1'
            capabilities['deviceName'] = '127.0.0.1:62001'
            # 系统手机中的联系人app的包名
            capabilities['appPackage'] = 'com.xueqiu.android'
            # 系统手机中的联系人app的主入口activity
            capabilities['appActivity'] = '.view.WelcomeActivityAlias'
            capabilities['noReset'] = 'True'
            # 连接测试机所在服务器服务器
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
            self.driver.implicitly_wait(8)
    def teardown(self):
        # 断开连接
        self.driver.quit()
    def test_touchactions(self):
        action = TouchAction(self.driver)
        time.sleep(10)
        window_rect = (self.driver.get_window_rect())
        print (window_rect)
        window_width= window_rect["width"]
        window_height = window_rect["height"]
        x1 = int(window_width/2)
        y_start = int(window_height * 0.9)
        y_end = int(window_height * 0.1)
        print (x1)
        print(y_start)
        print(y_end)
        action.press(x=x1,y=y_start).wait(400).move_to(x=x1,y=y_end).release().perform()

    def test_getattr(self):
        search_1= self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search")
        text = search_1.get_attribute("text")
        clickable = search_1.get_attribute("clickable")
        assert_that( close_to)






