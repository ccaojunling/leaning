from appium.webdriver.common.mobileby import MobileBy

from APP.page.base_page import BasePage
from APP.page.before_add_member import BeforeAddMember


class ContactAdd(BasePage):

    def goto_beforeaddmember(self):
        self.find_by_scroll("添加成员").click()
        return BeforeAddMember(self.driver)