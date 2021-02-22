from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testwait:

	def setup(self):
		capabilities = DesiredCapabilities.FIREFOX
		#capabilities['platform'] = "LINUX"
		# capabilities['version'] = "5"
		self.driver = webdriver.Remote(command_executor="http://localhost:5001/wd/hub", desired_capabilities={
			'browserName': 'chrome'
		})
		# self.driver = webdriver.Chrome()

		self.driver.get("http://home.testing-studio.com/")

	def teardown(self):
		self.driver.quit()

	def test_wait(self):
		WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable)
		sleep(5)

		self.a = webdriver.Chrome