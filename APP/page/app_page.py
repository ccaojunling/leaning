from appium import webdriver

from APP.page.main_page import MainPage


class App:

    def StartApp(self):
        desire_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True
        }
        self.driver = webdriver.Remote("httP://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)
        return self

    def StopApp(self):
        self.driver.quit()

    def RestartApp(self):
        pass

    def goto_MainPage(self):
        return MainPage(self.driver)