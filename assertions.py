import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        

    def test_search_field(self):

        self.assertTrue(self.is_element_prst(By.NAME, 'q'))
        # That we did was to use the function: is_element_prst, with the parameter NAME cuz is exactly the selector that we choosed

    def test_change_language(self):
        self.assertTrue(self.is_element_prst(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    def is_element_prst(self, how , what):
        try:
            self.driver.find_element(by = how, value = what)

        except NoSuchElementException as nse:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)