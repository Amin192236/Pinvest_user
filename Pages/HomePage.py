from Locators import *
from selenium.webdriver.common.keys import Keys


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_plus(self):
        self.driver.find_element('xpath', plus).click()
        # assert_check_plus= self.driver.find_element('xpath', total_investment).text
        # assert assert_check_plus == "210,000,000"

    def enter_check_plus(self):
        assert_check_plus= self.driver.find_element('xpath', total_investment).text
        assert assert_check_plus == "210,000,000"