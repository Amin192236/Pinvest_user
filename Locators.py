#check_home

plus= "//*[@id='create_fund']/div[1]/span[1]/svg"
total_investment= "//*[@id='create_fund']/div[2]/div[1]/div[2]/div/div/p[1]"

#check_home
click_login="//*[@id='landing_head']/nav[1]/ul/li[3]/a"
national_code="//*[@id='national_code']"
login_btn="//*[@id='btn_submit']"
edit_national_code="//*[@id='edit_nc']"
password="//*[@id='password']"
show_password="//*[@id='left_section']/div/div[1]/div/form/div[2]/div/div/div[1]/i[2]"
authentication="//*[@id='checked']/p[3]/a"
auth_next_step="//*[@id='app']/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/button"

logout="//*[@id='site_header']/div/a"
logout_no="//*[@id='confirm_logout_modal']/div/div/div[2]/button[1]"
logout_yes="//*[@id='confirm_logout_modal']/div/div/div[2]/button[2]"

# my_pinvest_desktop

click_desktop= "//*[@id='desktop_sidebar']/ul/li[1]"
desktop_show= "//*[@id='fund_details_section']/div[1]/div/div/div[1]"
desktop_refund_amount= "//*[@id='quick_refund_amount']"
desktop_refund_modal= "//*[@id='show_refund_modal']"
desktop_refund_modal_close= "//*[@id='refund_modal']/div/div/div[1]/i"
desktop_refund_modal_paytype= "//*[@id='refund_modal']/div/div/div[2]/div[2]/div/div"
desktop_refund_modal_paytype_select= "//*[@id='refund_paytype']/option[2]"
desktop_refund_modal_gateway= "//*[@id='refund_modal']/div/div/div[2]/div[3]/div"
desktop_refund_modal_gateway_select= "//*[@id='refund_gateway']/option[2]"
desktop_refund_modal_guide= "//*[@id='refund_modal']/div/div/div[3]/a"
desktop_confirm_quick_refund= "//*[@id='confirm_quick_refund']"
desktop_cashout_unit= "//*[@id='quick_cashout_unit']"
desktop_cashout_modal= "//*[@id='show_cashout_modal']"


# my_pinvest_funds

click_funds= "//*[@id='desktop_sidebar']/ul/li[2]"
funds_show= "//*[@id='funds_container']/div/div/div/div[1]/div/div[1]/span"
funds_profit_calculator= "//*[@id='amount2']"
funds_container= "//*[@id='funds_container']/div/div/div/div[2]/div[3]/div[2]/div/span[2]"
funds_monthly_profit= "//*[@id='funds_container']/div/div/div/div[2]/div[3]/div[3]/div/span[2]"

# my_pinvest_funds_report

click_report= "//*[@id='desktop_sidebar']/ul/li[3]"
report_show= "//*[@id='refund_link']"
report_fund_select= "//*[@id='fund_select']"
report_fund_select_option= "//*[@id='fund_select']/option"
report_refund_link= "//*[@id='refund_link']"
report_refund_link_show= "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[1]/span[1]"
report_refund_link_fund_select= "//*[@id='fund_select']"
report_refund_link_fund_option= "//*[@id='fund_select']/option"
report_refund_link_amount= "//*[@id='amount']"
report_refund_link_refund_paytype= "//*[@id='refund_paytype']"
report_refund_link_refund_paytype_option= "//*[@id='refund_paytype']/option[4]"
report_refund_link_transaction_date_dp= "//*[@id='transaction_date_dp']"
report_refund_link_transaction_date_dp_plotId= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[3]/td[6]/span"
report_refund_link_pinvest_bank_account_id= "//*[@id='pinvest_bank_account_id']"
report_refund_link_pinvest_bank_account_id_option= "//*[@id='pinvest_bank_account_id']/option[3]"
report_refund_link_receipt_number= "//*[@id='receipt_number']"
report_refund_link_description= "//*[@id='description']"
report_refund_link_opt_out= "//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/a"
report_refund_link_submit_refund= "//*[@id='submit_refund']"
report_cashout_link= "//*[@id='cashout_link']"
report_cashout_link_fund_select= "//*[@id='fund_select']"
report_cashout_link_fund_select_option= "//*[@id='fund_select']/option"
report_cashout_link_cashout_unit= "//*[@id='cashout_unit']"
report_cashout_link_schedule_date_dp= "//*[@id='schedule_date_dp']"
report_cashout_link_schedule_date_dp_next= "//*[@id='plotId']/div[1]/div[1]"
report_cashout_link_schedule_date_dp_plotId= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[4]/td[5]/span"
report_cashout_link_opt_out= "//*[@id='app']/div/div[2]/div[2]/form/div/div[2]/div/div/div/div/div/a"
report_cashout_link_show_confirm_modal= "//*[@id='show_confirm_modal']"
report_unit_price_tab= "//*[@id='unit_price_tab']"
report_profit_tab= "//*[@id='profit_tab']"
report_table_report_container_successful= "//*[@id='table_report_container']/div/div/div/div[2]/div[1]/div/div/label[2]"
report_table_report_container_unsuccessful= "//*[@id='table_report_container']/div/div/div/div[2]/div[1]/div/div/label[1]"



# my_pinvest_accounts

click_accounts= "//*[@id='desktop_sidebar']/ul/li[4]"
accounts_show= "//*[@id='add_account_btn']"
accounts_add_account_btn= "//*[@id='add_account_btn']"
accounts_add_account_bank= "//*[@id='bank']"
accounts_add_account_bank_option= "//*[@id='bank']/option[3]"
accounts_add_account_period= "//*[@id='period']"
accounts_add_account_period_daily= "//*[@id='period']/option[2]"
accounts_add_account_period_daily_next= "//*[@id='plotId']/div[1]/div[1]"
accounts_add_account_period_daily_option1= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[5]/td[1]/span"
accounts_add_account_period_daily_option2= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[5]/td[2]/span"
accounts_add_account_period_daily_option3= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[6]/td[1]/span"
accounts_add_account_period_weekly= "//*[@id='period']/option[3]"
accounts_add_account_period_weekly_option1= "//*[@id='saturday_check']"
accounts_add_account_period_weekly_option2= "//*[@id='monday_check']"
accounts_add_account_period_weekly_option3= "//*[@id='thursday_check']"
accounts_add_account_period_weekly_daily_next= "//*[@id='weekly_exceptions_calendar']/div[1]/div[1]/div[1]/div"
# accounts_add_account_period_weekly_daily_option1= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[5]/td[3]/span"
accounts_add_account_period_weekly_daily_option1= "//*[@id='weekly_exceptions']/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr[3]/td[1]/span"
accounts_add_account_period_weekly_daily_option2= "//*[@id='weekly_exceptions']/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr[3]/td[5]/span"
accounts_add_account_period_weekly_daily_option3= "//*[@id='weekly_exceptions']/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr[4]/td[1]/span"


accounts_add_account_period_monthly= "//*[@id='period']/option[4]"
accounts_add_account_period_monthly_option1= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/span"
accounts_add_account_period_monthly_option2= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/span"
accounts_add_account_period_monthly_option3= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[3]/td[3]/span"
accounts_add_account_period_monthly_option4= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[4]/td[4]/span"
accounts_add_account_period_max_withdraw= "//*[@id='max_withdraw']"
accounts_add_account_period_accept= "//*[@id='accept']"
accounts_add_account_period_opt_out= "//*[@id='add_bank_account_form']/div[2]/div/div/div/div/div/a"
accounts_add_account_period_submit_form= "//*[@id='submit_form']"
accounts_add_account_period_detail= "//*[@id='refundDetailModalLabel']"
accounts_add_account_period_detail_modal_bank= "//*[@id='detail_modal_bank']"
accounts_add_account_period_detail_modal_max= "//*[@id='detail_modal_max']"




# my_pinvest_statement_report

click_statement= "//*[@id='desktop_sidebar']/ul/li[5]"
statement_show= "//*[@id='statement_report_table']/thead/tr/th[4]"

# my_pinvest_nexo_card

click_card= "//*[@id='desktop_sidebar']/ul/li[6]"
card_show= "//*[@id='checking_status']"

# my_pinvest_policy

click_policy= "//*[@id='desktop_sidebar']/ul/li[8]"
policy_show= "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/div/p"

# my_pinvest_faq

click_faq= "//*[@id='desktop_sidebar']/ul/li[9]"
faq_show= "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/div/p"

# my_pinvest_contact-us

click_contact= "//*[@id='desktop_sidebar']/ul/li[10]"
contact_show= "//*[@id='ways_container']/p"

