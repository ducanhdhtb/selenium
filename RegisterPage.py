from locator import Locator
class RegisterPages():
    def __init__(self, driver):
        self.driver = driver
        self.customer_firstname_textbox_id = Locator.customer_firstname_textbox_id
        self.customer_lastname_textbox_id = Locator.customer_lastname_textbox_id
        self.customer_password_textbox_id = Locator.customer_password_textbox_id
        self.firstname_textbox_id = Locator.firstname_textbox_id
        self.lastname_textbox_id = Locator.lastname_textbox_id
        self.customer_company_textbox_id = Locator.customer_company_textbox_id
        self.customer_address1_textbox_id = Locator.customer_address1_textbox_id
        self.customer_address2_textbox_id = Locator.customer_address2_textbox_id
        self.customer_city_textbox_id = Locator.customer_city_textbox_id
        self.customer_postcode_textbox_id = Locator.customer_postcode_textbox_id
        self.customer_infor_textbox_id = Locator.customer_infor_textbox_id
        self.customer_phone_textbox_id = Locator.customer_phone_textbox_id
        self.customer_phone_mobile_textbox_id = Locator.customer_phone_mobile_textbox_id
        self.customer_alias_textbox_id = Locator.customer_alias_textbox_id
        self.customer_gender_textbox_id = Locator.customer_gender_textbox_id

    def enter_firstname(self, username):
        self.driver.find_element_by_id(
            self.customer_firstname_textbox_id).clear()
        self.driver.find_element_by_id(
            self.customer_firstname_textbox_id).send_keys(username)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_id(
            self.customer_lastname_textbox_id).clear()
        self.driver.find_element_by_id(
            self.customer_lastname_textbox_id).send_keys(lastname)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.customer_password_textbox_id)
        self.driver.find_element_by_id(
            self.customer_password_textbox_id).send_keys(password)

    def enter_fsname(self, firstname):
        self.driver.find_element_by_id(self.firstname_textbox_id).clear()
        self.driver.find_element_by_id(
            self.firstname_textbox_id).send_keys(firstname)

    def enter_lname(self, lastname):
        self.driver.find_element_by_id(self.lastname_textbox_id).clear()
        self.driver.find_element_by_id(
            self.lastname_textbox_id).send_keys(lastname)

    def enter_company(self, company):
        self.driver.find_element_by_id(
            self.customer_company_textbox_id).clear()
        self.driver.find_element_by_id(
            self.customer_company_textbox_id).send_keys(company)

    def enter_address1(self, address1):
        self.driver.find_element_by_id(
            self.customer_address1_textbox_id).clear()
        self.driver.find_element_by_id(
            self.customer_address1_textbox_id).send_keys(address1)

    def enter_address2(self, address2):
         self.driver.find_element_by_id(
             self.customer_address2_textbox_id).clear()
         self.driver.find_element_by_id(
             self.customer_address2_textbox_id).send_keys(address2)

    def enter_city(self, city):
        self.driver.find_element_by_id(self.customer_city_textbox_id).clear()
        self.driver.find_element_by_id(
            self.customer_city_textbox_id).send_keys(city)

    def enter_postcode(self, postcode):
        self.driver.find_element_by_id(
            self.customer_postcode_textbox_id).clear()
        self.driver.find_element_by_id(
            self.customer_postcode_textbox_id).send_keys(postcode)

    def enter_information(self, information):
        self.driver.find_element_by_id(self.customer_infor_textbox_id).clear()
        self.driver.find_element_by_id(
            self.customer_infor_textbox_id).send_keys(information)

    def enter_phone(self, phone):
        self.driver.find_element_by_id(self.customer_phone_textbox_id).clear()
        self.driver.find_element_by_id(
            self.customer_phone_textbox_id).send_keys(phone)

    def enter_phone_mobile(self, phone_mobile):
        self.driver.find_element_by_id(
            self.customer_phone_mobile_textbox_id).clear()
        self.driver.find_element_by_id(
            self.customer_phone_mobile_textbox_id).send_keys(phone_mobile)

    def enter_alias(self, alias):
        self.driver.find_element_by_id(self.customer_alias_textbox_id).clear()
        self.driver.find_element_by_id(self.customer_alias_textbox_id).send_keys(alias)

    def enter_gender(self):
        self.driver.find_element_by_id(self.customer_gender_textbox_id).click()

    def check_invalid_firstname(self):
        test = self.driver.find_element_by_id(self.customer_firstname_textbox_id).text
        return test
        

