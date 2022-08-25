from Locators import *


class PolicyPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_policy(self):
        self.driver.find_element('xpath', click_policy).click()

    def enter_policy_assert(self):
        assert_check_policy= self.driver.find_element('xpath', policy_show).text
        assert assert_check_policy== "شرایط و قوانین استفاده از سرویس ها و خدمات"
