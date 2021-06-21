import unittest
from selenium import webdriver
from selenium.webdriver.common import by
# Import by to interact with an elements by theirs css selectors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    

class NavegationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_account_links(self):

        WebDriverWait(self.driver, 12).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="select-language"]')))
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()


    def test_create_new_customer(self):

        self.driver.find_element_by_link_text("ACCOUNT").click()
        my_account = WebDriverWait(self.driver, 12).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "CREATE AN ACCOUNT")))
        create_account_button.click()

        WebDriverWait(self.driver, 8).until(EC.title_contains('Create New Customer Account'))



        return 0

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)