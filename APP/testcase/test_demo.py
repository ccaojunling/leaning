from APP.page.app_page import App


class TestDemo:
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.StopApp()

    def test_demo(self):
        name = "test1"
        gender="女"
        tele = "13300000001"
        self.addmember = self.app.StartApp().goto_MainPage().goto_contarct().goto_beforeaddmember().goto_addmember()
        text = self.addmember.add_member(name,gender,tele).get_toast()
        print(text)
        assert "添加成功" in text