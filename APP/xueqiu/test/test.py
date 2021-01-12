from APP.xueqiu.page.main_page import MainPage


class Testdemo:


    def test_search(self):
        main = MainPage()
        main.goto_market().goto_search()
        