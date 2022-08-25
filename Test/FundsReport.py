from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from Pages.Login import LoginPage
from Pages.FundsReport import ReportPage


import unittest

o = Options()
o.add_argument('--no-sandbox')

s = Service('d:\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_Pinvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=s, options=o)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test1_pinvest_home(self):
        self.driver.get("https://pinvest.ir")
        assert_home= self.driver.find_element('xpath', "//*[@id='landing_head']/nav[1]/ul/li[2]/a").text
        assert assert_home== "تماس با ما"
        print("با موفقیت وارد پینوست شد.")


    # def test2_login_phone(self):
    #     home = HomePage(driver=self.driver)
    #     plus= self.driver.find_element('xpath', "//*[@id='create_fund']/p[1]")
    #     plus.location_once_scrolled_into_view
    #     home.enter_click_plus()
    #     home.enter_click_plus()
        # assert_check_plus= self.driver.find_element('xpath', "//*[@id='create_fund']/div[1]/span[1]/svg").text
        # assert assert_check_plus== "210,000,000"
        # home.enter_check_plus()

    def test2_login_register(self):
        login = LoginPage(driver=self.driver)
        login.enter_click_login_register()
        # login.enter_national_code("5920039027")
        # login.enter_click_login_btn()
        # login.enter_edit_national_code()
        login.enter_national_code("4073422571")
        login.enter_click_login_btn()
        login.enter_password("saPA27!3")
        login.enter_show_password()
        login.enter_click_login_btn()
        #assert login
        login.enter_show_desk()
        print("با موفقیت وارد صفحه کاربر شد.")
        # logout
        # login.enter_logout()
        # login.enter_logout_no()
        # login.enter_logout()
        # login.enter_logout_yes()

    def test3_funds_report(self):
        report = ReportPage(driver=self.driver)
        report.enter_click_report()
        report.enter_report_assert()
        print("با موفقیت وارد گزارشات سرمایه گذاری ها شد.")
        report.enter_report_fund_select()
        report.enter_report_fund_select_option()
        report.enter_report_refund_link()
        report.enter_report_refund_link_show()
        print("با موفقیت وارد صفحه واریز شد.")
        report.enter_report_refund_link_fund_select()
        report.enter_report_refund_link_fund_option()
        report.enter_report_refund_link_amount("100000")
        report.enter_report_refund_link_refund_paytype()
        report.enter_report_refund_link_refund_paytype_option()
        report.enter_report_refund_link_transaction_date_dp()
        report.enter_report_refund_link_transaction_date_dp_plotId()
        report.enter_report_refund_link_pinvest_bank_account_id()
        report.enter_report_refund_link_pinvest_bank_account_id_option()
        report.enter_report_refund_link_receipt_number("123456789")
        report.enter_report_refund_link_description("این یک تست می باشد")
        report.enter_report_refund_link_opt_out()
        # report.enter_report_refund_link_submit_refund()
        sleep(3)
        report.enter_report_cashout_link()
        report.enter_report_cashout_link_fund_select()
        report.enter_report_cashout_link_fund_select_option()
        report.enter_report_cashout_link_cashout_unit("100000")
        report.enter_report_cashout_link_schedule_date_dp()
        report.enter_report_cashout_link_schedule_date_dp_next()
        report.enter_report_cashout_link_schedule_date_dp_plotId()
        report.enter_report_cashout_link_opt_out()
        # report.enter_report_cashout_link_show_confirm_modal()

        report.enter_report_unit_price_tab()
        sleep(2)
        report.enter_report_profit_tab()
        sleep(2)
        report.enter_report_table_report_container_successful()
        sleep(2)
        report.enter_report_table_report_container_unsuccessful()


        sleep(3)




        # report.enter_click_report()





    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
