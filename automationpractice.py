from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
class testCase (unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome("D:\chromedriver.exe")
        self.driver.implicitly_wait(30)
        #self.driver.maximize_window()
        # navigate to an automationpractice
        self.driver.get("http://automationpractice.com/index.php")

    def selection(self):
        self.element = self.driver.find_element_by_id("selectProductSort")
        self.drp = Select(self.element)
        # select by visible text
        #self.drp.select_by_visible_text("Price: Lowest first") #lowest price

        #select by index
        #self.drp.select_by_index(2) #Price highest

        #select by value 
        #self.drp.select_by_value("quantity:desc") # Stock
        print(len(self.drp.options))
        self.all_options = self.drp.options
        for option in self.all_options:
            print(option.text)


    def test_search_by_text(self):
        time.sleep(2)
        # get the search textbox
        self.searchField = self.driver.find_element_by_name("search_query")
        # enter search keyword and submit
        self.key_search = "Blouse"
        self.searchField.send_keys(self.key_search)
        self.searchField.submit()
        #get the list of elements which are displayed after the search
        self.lists = self.driver.find_elements_by_class_name("product_img_link")
        self.no = len(self.lists)
        # if no > 0:
        #     for i in range(0,no):
        #         print (lists[i].get_attribute("href"))
        #         print (lists[i].get_attribute("title"))
        self.assertEqual(1 , len(self.lists))  
        #self.assertIn(self.key_search,self.driver.title)
        self.selection()
         
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
