from Locators import *


class CardPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_card(self):
        self.driver.find_element('xpath', click_card).click()

    def enter_card_assert(self):
        assert_check_card= self.driver.find_element('xpath', card_show).text
        assert assert_check_card== "کاربر محترم پینوست، به زودی خدمات کارت در این بخش فعال خواهد شد."
