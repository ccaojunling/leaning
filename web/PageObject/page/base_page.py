from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseMethod():
    def __init__(self, driver:WebDriver = None):
        if driver == None:
            # 复用浏览器
            # options = Options()
            # options.debugger_address="localhost:9222"
            self.driver= webdriver.Firefox()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def find(self,by,locator):
        element = self.driver.find_element(by,locator)
        return element

    def finds(self,by,locator):
        elements = self.driver.find_elements(by,locator)
        return elements

    def wait_for_click(self,locator,timeout=10):
        element:WebElement = WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable(locator))
        return element

