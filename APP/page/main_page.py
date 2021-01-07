from appium.webdriver.common.mobileby import MobileBy

from APP.page.contact_add import ContactAdd


class MainPage:

    def __init__(self,driver):
        self.driver = driver


    def goto_message(self):
        pass

    def goto_contarct(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text ='通讯录']").click()
        return ContactAdd(self.driver)

    def goto_workspace(self):
        pass

    def goto_me(self):
        pass