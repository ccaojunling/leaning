from appium import webdriver


class TestApp:
    def setup(self):
        capabilities = {}
        # Android平台测试
        capabilities['platformName'] = 'Android'
        # 测试手机版本为5.0
        capabilities['platformVersion'] = '5.1.1'
        capabilities['deviceName'] = '127.0.0.1:62001'
        capabilities['appPackage'] = 'com.android.systemui'
        capabilities['appActivity'] = '.Launcher'
        capabilities['noReset'] = 'True'
        # 连接测试机所在服务器服务器
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(8)

    def teardown(self):
        pass

    def test_app1(self):
        pass