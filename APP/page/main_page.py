from appium.webdriver.common.mobileby import MobileBy

from APP.page.base_page import BasePage
from APP.page.contact_add import ContactAdd


class MainPage(BasePage):

    def goto_message(self):
        pass

    def goto_contarct(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text ='通讯录']")
        return ContactAdd(self.driver)

    def goto_workspace(self):
        pass

    def goto_me(self):
        pass