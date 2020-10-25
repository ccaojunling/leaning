from selenium import webdriver
from selenium.webdriver.common.by import By

from web.PageObject.page.add_member_page import AddMember
from web.PageObject.page.base_page import BaseMethod


class MainPage(BaseMethod):

    def goto_add_member(self):
        # 点击通讯录
        self.find(By.CSS_SELECTOR,".frame_nav_item_title:nth-child(2)").click()
        #点击添加成员
        self.find(By.CSS_SELECTOR,".qui_btn ww_btn js_add_member").click()
        return AddMember
