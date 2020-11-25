from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BaseMethod():
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            # 复用浏览器
            options = Options()
            options.debugger_address="localhost:9222"
            self.driver= webdriver.Chrome(options=options)
        else:
            self.driver = webdriver.Chrome()

    def find(self,by,locator):
        element = self.driver.find_element(by,locator)
        return element

    def finds(self,by,locator):
        elements = self.driver.find_elements(by,locator)
        return elements
