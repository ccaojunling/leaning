from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.PageObject.page.base_page import BaseMethod


class AddMember(BaseMethod):

    # 输入用户信息
    def add_member_info(self,name,num,telephone):
        # 输入姓名
        self.find(By.ID,"username").send_keys(name)
        self.find(By.ID,"memberAdd_acctid").send_keys(num)
        self.find(By.ID,"memberAdd_phone").send_keys(telephone)
        # 点击保存
        self.find(By.CSS_SELECTOR,"").click()

    # 判断用户信息
    def get_member(self,name):
        while True:
            name_list = []
            # 按页获取用户名列表
            member_list = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
            name_list=[element.get_attribute("title") for element in member_list]
            if name in name_list:
                return True
            # 没找到就翻页
            result: str = self.find(By.CSS_SELECTOR,". ww_pageNav_info_text").text
            num1,num2 = result.split("/",1)
            if int(num1)== int(num2):
                return False
            else:
                self.find(By.CSS_SELECTOR,".ww_commonImg ww_commonImg_PageNavArrowRightNormal").click()


