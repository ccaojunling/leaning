from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class Testcontact:

    def setup(self):
        desire_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True
        }
        self.driver = webdriver.Remote("httP://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_addmember(self):
        name = "test01"
        genter = "男"
        tele="13011111111"
        self.driver.find_element(MobileBy.XPATH,"//*[@text ='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text ='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text ='姓名　']/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,"//*[@text ='性别']/../android.widget.RelativeLayout/android.widget.RelativeLayout").click()
        if genter == "男":
            WebDriverWait(self.driver,10).until(lambda x : x.find_element(MobileBy.XPATH,"//*[@text = '男']"))
            self.driver.find_element(MobileBy.XPATH,"//*[@text = '男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@text = '女']").click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机　']/..//android.widget.EditText").send_keys(tele)
        self.driver.find_element(MobileBy.XPATH, "//*[@text = '保存']").click()
        text= self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        assert "添加成功" in text


