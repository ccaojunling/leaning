from appium.webdriver.common.mobileby import MobileBy

from APP.page.add_member import AddMember


class BeforeAddMember:

    def __init__(self,driver):
        self.driver = driver

    def goto_addmember(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text ='手动输入添加']").click()
        return AddMember(self.driver)

    def get_toast(self):
        toast_text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast_text

