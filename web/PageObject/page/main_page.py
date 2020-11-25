
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from web.PageObject.page.add_member_page import AddMember
from web.PageObject.page.base_page import BaseMethod


class MainPage(BaseMethod):

    def goto_add_member(self):
        # 点击通讯录
        self.find(By.ID,"menu_contacts").click()
        # 点击添加成员
        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")
        # 用显示等待
        # element = self.wait_for_click(locator)
        # element.click()

        # 判断页面是否跳转成功，添加成员按钮有时点了页面不跳转，判断跳转后的页面的元素是否出现
        def wait_for_next(x:WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID,"username")
            except:
                return False
        WebDriverWait(self.driver,10).until(wait_for_next)
        return AddMember(self.driver)
