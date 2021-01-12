from appium.webdriver.common.mobileby import MobileBy

from APP.xueqiu.page.base_page import BasePage
from APP.xueqiu.page.market_page import MarketPage


class MainPage(BasePage):

    def goto_market(self):
        # 点击首页的行情按钮
        self.find(MobileBy.XPATH,'//*[@class = "android.widget.TabWidget"]//*[@text ="行情"]').click()
        return MarketPage(self.driver)