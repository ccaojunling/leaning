from time import sleep

from appium import webdriver


class Testapp:
    def setup(self):
            capabilities = {}
            # Android平台测试
            capabilities['platformName'] = 'Android'
            # 测试手机版本为5.0
            capabilities['platformVersion'] = '6.0.1'
            capabilities['deviceName'] = '127.0.0.1:7555'
            capabilities['noReset'] = True
            capabilities['browser']="Browser"
            # 连接测试机所在服务器服务器
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
            self.driver.implicitly_wait(8)

    def teardown(self):
        # 断开连接
        self.driver.quit()

    def test_webview(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)