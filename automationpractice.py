from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
import config


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

    def test_search_by_text(self):
        time.sleep(2)
        # get the search textbox
        self.searchField = self.driver.find_element_by_name("search_query")
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

    def test_register_valid(self):
        # Navigate to register
        self.driver.find_element_by_class_name("login").click()
        # textbox input
        self.driver.find_element_by_id("email_create").send_keys(config.CUSTOMER_EMAIL)
        self.driver.find_element_by_id("SubmitCreate").click()
        time.sleep(3)
        try:
            # Workking with textbox
            customer_firstname = self.driver.find_element_by_id(
                "customer_firstname")
            customer_firstname.clear()
            customer_firstname.send_keys(config.CUSTOMER_FIRSTNAME)

            customer_lastname = self.driver.find_element_by_id(
                "customer_lastname")
            customer_lastname.send_keys(config.CUSTOMER_LASTNAME)

            customer_password = self.driver.find_element_by_id("passwd")
            customer_password.send_keys(config.CUSTOMER_PASSWORD)

            firstname = self.driver.find_element_by_id("firstname")
            firstname.send_keys(config.FIRSTNAME)

            lastname = self.driver.find_element_by_id("lastname")
            lastname.send_keys(config.LASTNAME)

            company = self.driver.find_element_by_id("company")
            company.send_keys(config.COMPANY)

            address1 = self.driver.find_element_by_id("address1")
            address1.send_keys(config.ADDRESS1)

            address2 = self.driver.find_element_by_id("address2")
            address2.send_keys(config.ADDRESS2)

            city = self.driver.find_element_by_id("city")
            city.send_keys(config.CITY)

            postcode = self.driver.find_element_by_id("postcode")
            postcode.send_keys(config.POSTCODE)

            other = self.driver.find_element_by_id("other")
            other.send_keys("More information was add at here....")

            phone = self.driver.find_element_by_id("phone")
            phone.send_keys("028 7108 7108")

            phone_mobile = self.driver.find_element_by_id("phone_mobile")
            phone_mobile.send_keys("09 42 42 88 34")

            alias = self.driver.find_element_by_id("alias")
            alias.send_keys("alias change here")
            # working with selectbox state
            self.selectbox_state = self.driver.find_element_by_id(
                "id_state")  # choose selexbox with id = id_state
            self.drp_state = Select(self.selectbox_state)  # dropdown
            self.drp_state.select_by_index(4)
            self.number_options_state = len(self.drp_state.options)
            print("number of state oftions is : ", self.number_options_state)
            for i in range(self.number_options_state):
                self.selectbox_state = self.driver.find_element_by_id(
                    "id_state")
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
            # working with radio button
            self.driver.find_element_by_id("id_gender1").click()
            #submit form
            self.driver.find_element_by_id("submitAccount").click()
            time.sleep(10)
            print(self.driver.page_source)
        except:
            print("Failed.Check at test_register")

    def test_register_invalid(self):

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
