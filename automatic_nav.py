import unittest
from selenium import webdriver
from time import sleep


class NavegationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com")

    def test_navigation(self):
        
        driver = self.driver
        search_field = driver.find_element_by_name("q")

        search_field.clear()
        search_field.send_keys("basado meme")
        search_field.submit()
        driver.find_element_by_link_text("Imágenes").click()
        sleep(10)
        driver.refresh()


        driver.back()
        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys("Pollo con tenis")
        search_field.submit()
        sleep(20)
        driver.back()
        driver.forward()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

