from Locators import *


class ReportPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_report(self):
        self.driver.find_element('xpath', click_report).click()

    def enter_report_assert(self):
        assert_check_report= self.driver.find_element('xpath', report_show).text
        assert assert_check_report== "واریز"

    def enter_report_fund_select(self):
        self.driver.find_element('xpath', report_fund_select).click()

    def enter_report_fund_select_option(self):
        self.driver.find_element('xpath', report_fund_select_option).click()

# refund_link

    def enter_report_refund_link(self):
        self.driver.find_element('xpath', report_refund_link).click()

    def enter_report_refund_link_show(self):
        assert_check_report_refund_link_show= self.driver.find_element('xpath', report_refund_link_show).text
        assert assert_check_report_refund_link_show== "واریز"

    def enter_report_refund_link_fund_select(self):
        self.driver.find_element('xpath', report_refund_link_fund_select).click()

    def enter_report_refund_link_fund_option(self):
        self.driver.find_element('xpath', report_refund_link_fund_option).click()

    def enter_report_refund_link_amount(self, amount):
        self.driver.find_element('xpath', report_refund_link_amount).send_keys(amount)

    def enter_report_refund_link_refund_paytype(self):
        self.driver.find_element('xpath', report_refund_link_refund_paytype).click()

    def enter_report_refund_link_refund_paytype_option(self):
        self.driver.find_element('xpath', report_refund_link_refund_paytype_option).click()

    def enter_report_refund_link_transaction_date_dp(self):
        self.driver.find_element('xpath', report_refund_link_transaction_date_dp).click()

    def enter_report_refund_link_transaction_date_dp_plotId(self):
        self.driver.find_element('xpath', report_refund_link_transaction_date_dp_plotId).click()

    def enter_report_refund_link_pinvest_bank_account_id(self):
        self.driver.find_element('xpath', report_refund_link_pinvest_bank_account_id).click()

    def enter_report_refund_link_pinvest_bank_account_id_option(self):
        self.driver.find_element('xpath', report_refund_link_pinvest_bank_account_id_option).click()

    def enter_report_refund_link_receipt_number(self, number):
        self.driver.find_element('xpath', report_refund_link_receipt_number).send_keys(number)

    def enter_report_refund_link_description(self, description):
        self.driver.find_element('xpath', report_refund_link_description).send_keys(description)

    def enter_report_refund_link_opt_out(self):
        self.driver.find_element('xpath', report_refund_link_opt_out).click()

    def enter_report_refund_link_submit_refund(self):
        self.driver.find_element('xpath', report_refund_link_submit_refund).click()

# cashout_link

    def enter_report_cashout_link(self):
        self.driver.find_element('xpath', report_cashout_link).click()

    def enter_report_cashout_link_fund_select(self):
        self.driver.find_element('xpath', report_cashout_link_fund_select).click()

    def enter_report_cashout_link_fund_select_option(self):
        self.driver.find_element('xpath', report_cashout_link_fund_select_option).click()

    def enter_report_cashout_link_cashout_unit(self, unit):
        self.driver.find_element('xpath', report_cashout_link_cashout_unit).send_keys(unit)

    def enter_report_cashout_link_schedule_date_dp(self):
        self.driver.find_element('xpath', report_cashout_link_schedule_date_dp).click()

    def enter_report_cashout_link_schedule_date_dp_next(self):
        self.driver.find_element('xpath', report_cashout_link_schedule_date_dp_next).click()

    def enter_report_cashout_link_schedule_date_dp_plotId(self):
        self.driver.find_element('xpath', report_cashout_link_schedule_date_dp_plotId).click()

    def enter_report_cashout_link_opt_out(self):
        self.driver.find_element('xpath', report_cashout_link_opt_out).click()

    def enter_report_cashout_link_show_confirm_modal(self):
        self.driver.find_element('xpath', report_cashout_link_show_confirm_modal).click()

    def enter_report_unit_price_tab(self):
        self.driver.find_element('xpath', report_unit_price_tab).click()

    def enter_report_profit_tab(self):
        self.driver.find_element('xpath', report_profit_tab).click()

    def enter_report_table_report_container_successful(self):
        self.driver.find_element('xpath', report_table_report_container_successful).click()

    def enter_report_table_report_container_unsuccessful(self):
        self.driver.find_element('xpath', report_table_report_container_unsuccessful).click()
