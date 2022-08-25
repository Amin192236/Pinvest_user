from Locators import *


class FundsPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_funds(self):
        self.driver.find_element('xpath', click_funds).click()

    def enter_funds_assert(self):
        assert_check_funds= self.driver.find_element('xpath', funds_show).text
        assert assert_check_funds== "صندوق دوم اکسیر فارابی"

    def enter_funds_profit_calculator(self, amount):
        self.driver.find_element('xpath', funds_profit_calculator).send_keys(amount)

    def enter_check_funds_container(self):
        assert_check_funds_container= self.driver.find_element('xpath', funds_container).text
        assert assert_check_funds_container== "50"

    def enter_check_funds_monthly_profit(self):
        assert_check_funds_monthly_profit= self.driver.find_element('xpath', funds_monthly_profit).text
        assert assert_check_funds_monthly_profit== "1,500"
