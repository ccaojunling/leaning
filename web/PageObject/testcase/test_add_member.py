from web.PageObject.page.main_page import MainPage


class TestMember:
    def test_member(self):
        def setup():
            self.main = MainPage()

