import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class Testapp:
    def setup(self):
            capabilities = {}
            # Android平台测试
            capabilities['platformName'] = 'Android'
            # 测试手机版本为5.0
            capabilities['platformVersion'] = '8.0.0'
            capabilities['deviceName'] = 'b3b3a439'
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
    def test_app11(self):
        search_text=self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search")
        print(search_text.get_attribute("text"))
        print(search_text.location)
        print(search_text.size)
        search_enabled = search_text.is_enabled()
        if search_enabled ==True:
            search_text.click()
            self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element(MobileBy.XPATH,"//*[@resource-id=‘com.xueqiu.android:id/name’ and text='阿里巴巴']")
            alibaba_enable = alibaba_element.is_enabled()
            if alibaba_enable == True:
                print("成功")
            else:
                print("失败")

        time.sleep(2)



