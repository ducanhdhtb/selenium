from selenium import webdriver
import time
import config
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from RegisterPage import RegisterPages
from homepage import HomePage
from login import Login
from locator import Locator


class testCase (unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome("D:\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to an automationpractice
        self.driver.get(config.BASE_URL)
        # self.open("https://xkcd.com/378/")  # This method opens the specified page.
        # self.go_back()  # This method navigates the browser to the previous page.
        # self.go_forward()  # This method navigates the browser forward in history.
        # self.refresh_page()  # This method reloads the current page.
        # self.get_current_url()  # This method returns the current page URL.
        # self.get_page_source()  # This method returns the current page source.
    def selection(self):
        #self.driver.implicitly_wait(15)
        self.element = self.driver.find_element_by_id("selectProductSort")
        self.drp = Select(self.element)
        # select by visible text
        #self.drp.select_by_visible_text("Price: Lowest first") #lowest price
        number_options = len(self.drp.options)
        #select by index
        for i in range(number_options):
            old_page = self.driver.find_element_by_tag_name('html')
            self.element = self.driver.find_element_by_id("selectProductSort")
            self.drp = Select(self.element)
            self.drp.select_by_index(i)  # Price highest

        # self.element = self.driver.find_element_by_id("selectProductSort")
        # self.drp = Select(self.element)
        # self.drp.select_by_index(3)
        # self.element = self.driver.find_element_by_id("selectProductSort")
        # self.drp = Select(self.element)
        # self.drp.select_by_index(4)
        # self.drp.select_by_index(5)
        # self.drp.select_by_index(6)

        #select by value
        #self.drp.select_by_value("quantity:desc") # Stock
        # print(len(self.drp.options))
        # self.all_options = self.drp.options
        # for option in self.all_options:
        #     print(option.text)

    def _test_search_by_text(self):
        time.sleep(2)
        # get the search textbox
        self.searchField = self.driver.find_element_by_name("search_query")
        if self.searchField.is_displayed():
            print("Checkbox passed")
        # enter search keyword and submit
        self.key_search = "Blouse"
        self.searchField.send_keys(self.key_search)
        self.searchField.submit()
        #get the list of elements which are displayed after the search
        self.lists = self.driver.find_elements_by_class_name(
            "product_img_link")
        self.no = len(self.lists)
        # if no > 0:
        #     for i in range(0,no):
        #         print (lists[i].get_attribute("href"))
        #         print (lists[i].get_attribute("title"))
        self.assertEqual(1, len(self.lists))
        #self.assertIn(self.key_search,self.driver.title)
        self.selection()

    #def test_register_valid(self):
        # Navigate to register
        self.driver.find_element_by_class_name("login").click()
        # textbox input
        self.driver.find_element_by_id(
            "email_create").send_keys(config.CUSTOMER_EMAIL)
        self.driver.find_element_by_id("SubmitCreate").click()
        time.sleep(3)
        driver = self.driver
        # Instance of class RegisterPages
        register = RegisterPages(driver)

        register.enter_firstname(config.CUSTOMER_FIRSTNAME)
        register.enter_lastname(config.CUSTOMER_LASTNAME)
        register.enter_password(config.CUSTOMER_PASSWORD)
        register.enter_fsname(config.CUSTOMER_FIRSTNAME)
        register.enter_lname(config.CUSTOMER_LASTNAME)
        register.enter_company(config.CUSTOMER_COMPANY)
        register.enter_address1(config.CUSTOMER_COMPANY)
        register.enter_address2(config.CUSTOMER_ADDRESS2)
        register.enter_city(config.CUSTOMER_CITY)
        register.enter_postcode(config.CUSTOMER_POSTCODE)
        register.enter_information(config.CUSTOMER_INFOR)
        register.enter_phone(config.CUSTOMER_PHONE)
        register.enter_phone_mobile(config.CUSTOMER_PHONE_MOBILE)
        register.enter_alias(config.CUSTOMER_ALIAS)
        register.enter_gender()
        # working with selectbox state
        self.selectbox_state = self.driver.find_element_by_id(
            "id_state")  # choose selexbox with id = id_state
        self.drp_state = Select(self.selectbox_state)  # dropdown
        self.drp_state.select_by_index(4)
        self.number_options_state = len(self.drp_state.options)
        print("number of state oftions is : ", self.number_options_state)
        for i in range(self.number_options_state):
            self.selectbox_state = self.driver.find_element_by_id("id_state")
            self.drp_state = Select(self.selectbox_state)  # dropdown
            self.drp_state.select_by_index(i)  # Price highest

        # Working  with day month year select
        self.days = self.driver.find_element_by_id("days")
        self.day_select = Select(self.days)
        self.day_select.select_by_index(1)

        self.months = self.driver.find_element_by_id("months")
        self.months_select = Select(self.months)
        self.months_select.select_by_index(1)

        self.years = self.driver.find_element_by_id("years")
        self.years_select = Select(self.years)
        self.years_select.select_by_index(20)
        register.check_invalid_firstname()
        #submit form
        homepage = HomePage(driver)
        
        homepage.register()
        time.sleep(5)
        
        #homepage.sign_out()
        print("test complete!")
     
    def _test_login(self):
        driver = self.driver
        self.driver.find_element_by_class_name("login").click()
        login = Login(driver)
        login.enter_email(config.EMAIL_LOGIN)
        login.enter_pssword(config.PASSWORD_LOGIN)
        login.click_login()
        time.sleep(15)
        print("test login pass")

    #def test_login_invalid_email(self):
        driver = self.driver
        self.driver.find_element_by_class_name("login").click()
        login = Login(driver)
        login.enter_email(config.EMAIL_LOGIN_FAILED)        
        login.click_login()
        #message = driver.find_element_by_xpath("//li[contains(text(),'Invalid email address.')]").text
        message = login.get_text_from_warning_email()
        self.assertEqual(message, "Invalid email address.")  

    def test_login_invalid_password(self):
        driver = self.driver
        self.driver.find_element_by_class_name("login").click()
        login = Login(driver)
        login.enter_email(config.EMAIL_LOGIN)
        login.enter_pssword(config.PASSWORD_LOGIN_FAILED)        
        login.click_login()
        #message = driver.find_element_by_xpath("//li[contains(text(),'Invalid email address.')]").text
        login.get_text_from_warning_password("Invalid password12.")
        

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
