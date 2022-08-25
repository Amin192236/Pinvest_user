from Locators import *


class StatementPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_statement(self):
        self.driver.find_element('xpath', click_statement).click()

    def enter_statement_assert(self):
        assert_check_statement= self.driver.find_element('xpath', statement_show).text
        assert assert_check_statement== "توضیحات"
