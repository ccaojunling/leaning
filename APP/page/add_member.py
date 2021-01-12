from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from APP.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self,name,gender,tele):
        self.find(MobileBy.XPATH, "//*[@text ='姓名　']/../android.widget.EditText").send_keys(name)
        self.find_and_click(MobileBy.XPATH, "//*[@text ='性别']/../android.widget.RelativeLayout/android.widget.RelativeLayout")
        if gender == "男":
            self.find_and_click(MobileBy.XPATH, "//*[@text = '男']")
        else:
            self.find_and_click(MobileBy.XPATH, "//*[@text = '女']")

        self.find(MobileBy.XPATH, "//*[@text='手机　']/..//android.widget.EditText").send_keys(tele)
        self.find_and_click(MobileBy.XPATH, "//*[@text = '保存']")
        from APP.page.before_add_member import BeforeAddMember
        return BeforeAddMember(self.driver)