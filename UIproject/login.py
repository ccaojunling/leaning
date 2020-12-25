from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testcase:
    def test_login(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome()
        driver.get("http://172.16.101.139/ReportSys/index#")
        # cookies = driver.get_cookies()
        # print(cookies)
        cookies = [{'domain': '172.16.101.139', 'httpOnly': True, 'name': 'reportsys.session.id', 'path': '/ReportSys', 'secure': False, 'value': 'c12c5644-9457-40f4-8520-c0c6fa3af43f'}]
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        sleep(5)


