import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions.android.gsm import GsmCallActions


class Testapp:
    def setup(self):
            capabilities = {}
            # Android平台测试
            capabilities['platformName'] = 'Android'
            # 测试手机版本为5.0
            capabilities['platformVersion'] = '5.0'
            capabilities['deviceName'] = '127.0.0.1:62001'
            # 系统手机中的联系人app的包名
            capabilities['appPackage'] = 'com.xueqiu.android'
            # 系统手机中的联系人app的主入口activity
            capabilities['appActivity'] = '.view.WelcomeActivityAlias'
            capabilities['noReset'] = 'True'
            capabilities['avd'] = 'name'
            # 连接测试机所在服务器服务器
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
            self.driver.implicitly_wait(8)

    def teardown(self):
        # 断开连接
        self.driver.quit()

    def test_mobile(self):
        # self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)
        self.driver.send_sms('13110001111',"模拟发送短信")
        self.driver.set_network_connection(1)
        self.driver.start_recording_screen()
        time.sleep(3)
        # self.driver.get_screenshot_as_file('./pthtos/img.png')
        # search_text = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search")
        # print(search_text.get_attribute("text"))
        # print(search_text.location)
        # print(search_text.size)
        # search_enabled = search_text.is_enabled()
        # if search_enabled == True:
        #     search_text.click()
        #     self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        # time.sleep(2)
        self.driver.stop_recording_screen()




