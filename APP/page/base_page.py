import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver:WebDriver = None):
        self.driver = driver

    def find(self,by,locator):
        logging.info(by)
        logging.info(locator)
        WebDriverWait(self.driver,10).until(lambda x: x.find_element(by,locator))
        element = self.driver.find_element(by,locator)
        return element

    def find_by_scroll(self,text):
        logging.info("scroll")
        logging.info(text)
        element = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')
        return element

    def find_and_click(self,by,locator):
        logging.info("click")
        logging.info(by)
        logging.info(locator)
        wdw = [by,locator]
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(wdw))
        self.driver.find_element(by,locator).click()

    def get_toast_text(self):
        logging.info("get_toast_text")
        toast_text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast_text
