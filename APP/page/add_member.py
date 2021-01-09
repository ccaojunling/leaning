from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class AddMember:

    def __init__(self,driver):
        self.driver = driver

    def add_member(self,name,gender,tele):
        self.driver.find_element(MobileBy.XPATH, "//*[@text ='姓名　']/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text ='性别']/../android.widget.RelativeLayout/android.widget.RelativeLayout").click()
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text = '男']"))
            self.driver.find_element(MobileBy.XPATH, "//*[@text = '男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text = '女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机　']/..//android.widget.EditText").send_keys(tele)
        self.driver.find_element(MobileBy.XPATH, "//*[@text = '保存']").click()
        from APP.page.before_add_member import BeforeAddMember
        return BeforeAddMember(self.driver)