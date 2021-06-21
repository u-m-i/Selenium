import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        #driver.find_element_by_xpath('//*[@id="input-example"]/button').click()


    def dynamic_wait(self):

        driver = self.driver

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/input')))
        text_area = driver.find_element_by_xpath('//*[@id="input-example"]/input')
        text_area.click()
        text_area.send_keys("Buenas tardes cómo me les va?")


    def test_dyanamic_controls(self):
        
        driver = self.driver

        check_box = driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")

        check_box.click()

        remove_add_button = driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_button.click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))

        dis_able_button = driver.find_element_by_css_selector("#input-example > button")
        dis_able_button.click()

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))

        text_area = driver.find_element_by_css_selector("#input-example > input[type=text]")
        text_area.click()
        text_area.send_keys("No, my desire is not to be here")

        dis_able_button.click()



    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)