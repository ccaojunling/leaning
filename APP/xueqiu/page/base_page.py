import logging

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions

from APP.xueqiu.page.hand_black import handle_balck


class BasePage:
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)
    black_list = [(MobileBy.XPATH,'//*[@resource-id = "com.xueqiu.android:id/tv_agree" and @text ="同意"]'),
                   (MobileBy.XPATH,'//*[@resource-id = "com.xueqiu.android:id/ib_close"]')]
    max_no = 3
    error_no = 0


    def __init__(self, driver:WebDriver = None):
        if driver is None:
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
            # capabilities['noReset'] = 'true'
            # capabilities["dontStopAppOnReset"] = 'true'
            # 连接测试机所在服务器服务器
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
            self.driver.implicitly_wait(20)
        else:
            self.driver = driver

    @handle_balck
    # 封装查找元素
    def find(self,by,locator = None):
        logging.info(by)
        logging.info(locator)
        if locator is None:
            from selenium.webdriver.support.wait import WebDriverWait
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*by))
            element = self.driver.find_element(*by)
        else:
            from selenium.webdriver.support.wait import WebDriverWait
            WebDriverWait(self.driver,5).until(lambda x: x.find_element(by,locator))
            element = self.driver.find_element(by,locator)
        return element

    def find_by_scroll(self,text):
        # 封装滚动查找
        logging.info("scroll")
        logging.info(text)
        element = self.find(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')
        return element

    def find_and_click(self,by,locator):
        # 封装查找并点击
        logging.info("click")
        logging.info(by)
        logging.info(locator)
        wdw = (by,locator)
        from selenium.webdriver.support.wait import WebDriverWait
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(wdw))
        self.find(by,locator).click()

    def get_toast_text(self):
        # 封装获取toast文本
        logging.info("get_toast_text")
        toast_text = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast_text
