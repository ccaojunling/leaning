from appium.webdriver.common.mobileby import MobileBy

from APP.page.add_member import AddMember
from APP.page.base_page import BasePage


class BeforeAddMember(BasePage):

    def goto_addmember(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text ='手动输入添加']")
        return AddMember(self.driver)

    def get_toast(self):
        return self.get_toast_text()

