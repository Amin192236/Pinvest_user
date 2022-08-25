from Locators import *


class ContactPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_contact(self):
        self.driver.find_element('xpath', click_contact).click()

    def enter_contact_assert(self):
        assert_check_contact= self.driver.find_element('xpath', contact_show).text
        assert assert_check_contact== "اطلاعات تماس"
