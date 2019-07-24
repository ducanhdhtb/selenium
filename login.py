from locator import Locator
class Login():
    def __init__(self, driver):
        self.driver = driver
        self.email = Locator.email_textbox_id
        self.password = Locator.password_textbox_id
        self.SubmitLogin = Locator.SubmitLogin_textbox_id
    def enter_email(self,email):
        self.driver.find_element_by_id(self.email).clear()
        self.driver.find_element_by_id(self.email).send_keys(email)

    def enter_pssword(self,pssword):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(pssword)

    def click_login(self):
        self.driver.find_element_by_id(self.SubmitLogin).click()