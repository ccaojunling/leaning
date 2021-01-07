from appium.webdriver.common.mobileby import MobileBy

from APP.page.before_add_member import BeforeAddMember


class ContactAdd:

    def __init__(self,driver):
        self.driver = driver

    def goto_beforeaddmember(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        return BeforeAddMember(self.driver)