from Locators import *


class DesktopPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_desktop_sidebar(self):
        self.driver.find_element('xpath', click_desktop).click()

    def enter_desk_assert(self):
        assert_check_desk= self.driver.find_element('xpath', desktop_show).text
        assert assert_check_desk== "دارایی های من"

    def enter_desktop_refund_amount(self, amount):
        self.driver.find_element('xpath', desktop_refund_amount).send_keys(amount)

    def enter_desktop_refund_modal(self):
        self.driver.find_element('xpath', desktop_refund_modal).click()

    def enter_desktop_refund_modal_close(self):
        self.driver.find_element('xpath', desktop_refund_modal_close).click()

    def enter_desktop_refund_modal_paytype(self):
        self.driver.find_element('xpath', desktop_refund_modal_paytype).click()

    def enter_desktop_refund_modal_paytype_select(self):
        self.driver.find_element('xpath', desktop_refund_modal_paytype_select).click()

    def enter_desktop_refund_modal_gateway(self):
        self.driver.find_element('xpath', desktop_refund_modal_gateway).click()

    def enter_desktop_refund_modal_gateway_select(self):
        self.driver.find_element('xpath', desktop_refund_modal_gateway_select).click()

    def enter_desktop_refund_modal_guide(self):
        self.driver.find_element('xpath', desktop_refund_modal_guide).click()

    def enter_desktop_confirm_quick_refund(self):
        self.driver.find_element('xpath', desktop_confirm_quick_refund).click()
# show_cashout_modal

    def enter_desktop_cashout_unit(self, unit):
        self.driver.find_element('xpath', desktop_cashout_unit).send_keys(unit)

    def enter_desktop_cashout_modal(self):
        self.driver.find_element('xpath', desktop_cashout_modal).click()
