from selenium import webdriver
import time
import unittest
class testCase (unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome("D:\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to an automationpractice
        self.driver.get("http://automationpractice.com/index.php")
    def test_search_by_text(self):
        time.sleep(2)
        # get the search textbox
        self.searchField = self.driver.find_element_by_name("search_query")
        # enter search keyword and submit
        self.searchField.send_keys("Blouse")
        self.searchField.submit()
        #get the list of elements which are displayed after the search
        lists = self.driver.find_elements_by_class_name("product_img_link")
        no = len(lists)
        # if no > 0:
        #     for i in range(0,no):
        #         print (lists[i].get_attribute("href"))
        #         print (lists[i].get_attribute("title"))
        self.assertEqual(1, len(lists))
           
         
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
