from web.PageObject.page.main_page import MainPage


class TestMember:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    def test_addmember(self):
        username='张三27'
        memberid='1234312317'
        telephone='13312341247'
        addmember = self.main.goto_add_member()
        addmember.add_member_info(username, memberid, telephone)
        assert addmember.get_member(username)

