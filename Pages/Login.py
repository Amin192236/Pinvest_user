from Locators import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_login_register(self):
        self.driver.find_element('xpath', click_login).click()

    def enter_national_code(self, code):
        self.driver.find_element('xpath', national_code).send_keys(code)

    def enter_click_login_btn(self):
        self.driver.find_element('xpath', login_btn).click()

    def enter_edit_national_code(self):
        self.driver.find_element('xpath', edit_national_code).click()

    def enter_password(self, code):
        self.driver.find_element('xpath', password).send_keys(code)

    def enter_show_password(self):
        self.driver.find_element('xpath', show_password).click()

    def enter_authentication(self):
        self.driver.find_element('xpath', authentication).click()

    def enter_auth_next_step(self):
        self.driver.find_element('xpath', auth_next_step).click()

    def enter_logout(self):
        self.driver.find_element('xpath', logout).click()

    def enter_logout_no(self):
        self.driver.find_element('xpath', logout_no).click()

    def enter_logout_yes(self):
        self.driver.find_element('xpath', logout_yes).click()

    def enter_show_desk(self):
        assert_check_login= self.driver.find_element('xpath', click_desktop).text
        assert assert_check_login== "میزکار"