class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.register_id = "submitAccount"
        self.sign_out_class = "logout"

    def register(self):
        self.driver.find_element_by_id(self.register_id).click()
    
    def sign_out(self):
        self.driver.find_element_by_class_name(self.sign_out_class).click()
    