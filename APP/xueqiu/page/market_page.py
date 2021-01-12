from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from APP.xueqiu.page.base_page import BasePage


class MarketPage(BasePage):

    def goto_search(self):
        # 点击行情页面的搜索按钮
        self.find(MobileBy.XPATH,'//*[@class = "android.widget.ImageButton" and @resource-id ="com.xueqiu.android:id/action_search"]').click()
        sleep(2)

