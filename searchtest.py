import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        

    def test_search_tshirt(self):
        
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        driver.implicitly_wait(5)
        #Clear method at search_field to clean any text in the field.
        search_field.send_keys("tee")
        driver.implicitly_wait(5)
        search_field.submit()   
    
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('salt shaker')
        search_field.submit()   
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))
        
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)