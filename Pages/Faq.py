from Locators import *


class FaqPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_faq(self):
        self.driver.find_element('xpath', click_faq).click()

    def enter_faq_assert(self):
        assert_check_faq= self.driver.find_element('xpath', faq_show).text
        assert assert_check_faq== "پاسخ پرسش های پر تکرار"
