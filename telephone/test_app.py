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
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()
        # 断开连接
       # self.driver.quit()

    @pytest.mark.parametrize('search_key, name', [('alibaba', '阿里巴巴'), ('xiaomi', '小米集团-W')])
    def test_app(self, search_key, name):
        search_text=self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search")
        print(search_text.get_attribute("text"))
        print(search_text.location)
        print(search_text.size)
        search_enabled = search_text.is_enabled()
        if search_enabled ==True:
            search_text.click()
            self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(search_key)
            locator2 = (By.XPATH, f"//*[@resource-id='com.xueqiu.android:id/name' and @text='{name}']")
            WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator2))
            alibaba_element = self.driver.find_element_by_xpath(f"//*[@resource-id='com.xueqiu.android:id/name' and @text='{name}']")
            alibaba_enable = alibaba_element.is_enabled()
            if alibaba_enable == True:
                alibaba_element.click()
                locator=(By.XPATH, f"//*[@resource-id='com.xueqiu.android:id/stockName' and @text='{name}']/../../..//*[@resource-id='com.xueqiu.android:id/change_percentage']")
                WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(locator))
                change_ele = self.driver.find_element(MobileBy.XPATH,f"//*[@resource-id='com.xueqiu.android:id/stockName' and @text='{name}']/../../..//*[@resource-id='com.xueqiu.android:id/change_percentage']")
                change_percent = change_ele.get_attribute("text")
                print(change_percent)
            else:
                print("查询失败")

        time.sleep(2)



