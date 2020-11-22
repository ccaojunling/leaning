import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
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
            self.driver.implicitly_wait(20)
    def teardown(self):
        # 断开连接
        self.driver.quit()
    def test_app(self):
        search_text=self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search")
        print(search_text.get_attribute("text"))
        print(search_text.location)
        print(search_text.size)
        search_enabled = search_text.is_enabled()
        if search_enabled ==True:
            search_text.click()
            self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            time.sleep(3)
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            alibaba_enable = alibaba_element.is_enabled()
            if alibaba_enable == True:
                alibaba_element.click()
                time.sleep(8)
                change_ele = self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']/../../..//*[@resource-id='com.xueqiu.android:id/change_percentage']")
                change_percent = change_ele.get_attribute("text")
                print(change_percent)
            else:
                print("查询失败")

        time.sleep(2)



