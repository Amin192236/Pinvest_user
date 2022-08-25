from Locators import *


class AccountsPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_accounts(self):
        self.driver.find_element('xpath', click_accounts).click()

    def enter_accounts_assert(self):
        assert_check_accounts= self.driver.find_element('xpath', accounts_show).text
        assert assert_check_accounts== "افزودن حساب"

    def enter_accounts_add_account_btn(self):
        self.driver.find_element('xpath', accounts_add_account_btn).click() 

    def enter_accounts_add_account_bank(self):
        self.driver.find_element('xpath', accounts_add_account_bank).click()

    def enter_accounts_add_account_bank_option(self):
        self.driver.find_element('xpath', accounts_add_account_bank_option).click()

    def enter_accounts_add_account_period(self):
        self.driver.find_element('xpath', accounts_add_account_period).click()

    def enter_accounts_add_account_period_daily(self):
        self.driver.find_element('xpath', accounts_add_account_period_daily).click()

    def enter_accounts_add_account_period_daily_next(self):
        self.driver.find_element('xpath', accounts_add_account_period_daily_next).click()

    def enter_accounts_add_account_period_daily_option1(self):
        self.driver.find_element('xpath', accounts_add_account_period_daily_option1).click()

    def enter_accounts_add_account_period_daily_option2(self):
        self.driver.find_element('xpath', accounts_add_account_period_daily_option2).click()

    def enter_accounts_add_account_period_daily_option3(self):
        self.driver.find_element('xpath', accounts_add_account_period_daily_option3).click()

        # weekly

    def enter_accounts_add_account_period_weekly(self):
        self.driver.find_element('xpath', accounts_add_account_period_weekly).click()

    def enter_accounts_add_account_period_weekly_option1(self):
        self.driver.find_element('xpath', accounts_add_account_period_weekly_option1).click()

    def enter_accounts_add_account_period_weekly_option2(self):
        self.driver.find_element('xpath', accounts_add_account_period_weekly_option2).click()

    def enter_accounts_add_account_period_weekly_option3(self):
        self.driver.find_element('xpath', accounts_add_account_period_weekly_option3).click()

    def enter_accounts_add_account_period_weekly_daily_next(self):
        # passw= self.driver.find_element('xpath', accounts_add_account_period_weekly_daily_next)
        # passw.location_once_scrolled_into_view
        self.driver.find_element('xpath', accounts_add_account_period_weekly_daily_next).click()

    def enter_accounts_add_account_period_weekly_daily_option1(self):
        self.driver.find_element('xpath', accounts_add_account_period_weekly_daily_option1).click()

    def enter_accounts_add_account_period_weekly_daily_option2(self):
        self.driver.find_element('xpath', accounts_add_account_period_weekly_daily_option2).click()

    def enter_accounts_add_account_period_weekly_daily_option3(self):
        self.driver.find_element('xpath', accounts_add_account_period_weekly_daily_option3).click()

    # monthly

    def enter_accounts_add_account_period_monthly(self):
        self.driver.find_element('xpath', accounts_add_account_period_monthly).click()

    def enter_accounts_add_account_period_monthly_option1(self):
        self.driver.find_element('xpath', accounts_add_account_period_monthly_option1).click()

    def enter_accounts_add_account_period_monthly_option2(self):
        self.driver.find_element('xpath', accounts_add_account_period_monthly_option2).click()

    def enter_accounts_add_account_period_monthly_option3(self):
        self.driver.find_element('xpath', accounts_add_account_period_monthly_option3).click()

    def enter_accounts_add_account_period_monthly_option4(self):
        self.driver.find_element('xpath', accounts_add_account_period_monthly_option4).click()

    def enter_accounts_add_account_period_max_withdraw(self, amount):
        self.driver.find_element('xpath', accounts_add_account_period_max_withdraw).send_keys(amount)

    def enter_accounts_add_account_period_accept(self):
        self.driver.find_element('xpath', accounts_add_account_period_accept).click()

    def enter_accounts_add_account_period_opt_out(self):
        self.driver.find_element('xpath', accounts_add_account_period_opt_out).click()

    def enter_accounts_add_account_period_submit_form(self):
        self.driver.find_element('xpath', accounts_add_account_period_submit_form).click()

    def enter_accounts_add_account_period_detail(self):
        assert_check_accounts= self.driver.find_element('xpath', accounts_add_account_period_detail).text
        assert_check_accounts_add_account_period_detail_modal_bank= self.driver.find_element('xpath', accounts_add_account_period_detail_modal_bank).text
        assert_check_accounts_add_account_period_detail_modal_max= self.driver.find_element('xpath', accounts_add_account_period_detail_modal_max).text
        assert assert_check_accounts== "جزییات برداشت از حساب"
        # print("با موفقیت وارد پینوست شد.")
        print("با موفقیت وارد" , assert_check_accounts , "شد.")
        print("بانک: " , assert_check_accounts_add_account_period_detail_modal_bank , ".")
        print("سقف برداشت از حساب: " , assert_check_accounts_add_account_period_detail_modal_max , "می باشد")
