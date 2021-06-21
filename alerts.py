import unittest
from selenium import webdriver

class ClearPopup(unittest.TestCase):

    def setUp(self) -> None:

        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.maximize_window
        driver.get("http://demo-store.seleniumacademy.com/")

    
    def test_accept_popup(self):

        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys("tee")
        search_field.submit()


        driver.find_element_by_class_name("link-compare").click()
        driver.find_element_by_link_text("Clear All").click()

        alert = driver.switch_to_alert() 
        alert_text = alert.text

        self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)

        alert.dismiss()


    def tearDown(self) -> None:
        
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)