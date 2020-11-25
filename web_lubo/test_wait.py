from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testwait:

	def setup(self):
		self.drver = webdriver.Chrome()
		self.drver.get("http://home.testing-studio.com/")

	def teardown(self):
		self.drver.quit()

	def test_wait(self):
		WebDriverWait(self.drver,10).until(expected_conditions.element_to_be_clickable)