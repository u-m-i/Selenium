import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.implicitly_wait(20)

    
    def test_register_user(self):

        driver = self.driver

        # driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]')
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text("Log In").click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a')

        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled)
        create_account_button.click()

        self.assertAlmostEqual('Create New Customer Account', driver.title)
        
        first_name = driver.find_element_by_id("firstname")
        lastname = driver.find_element_by_id("lastname")
        email = driver.find_element_by_id("email_address")
        passw = driver.find_element_by_id("password")
        confirm = driver.find_element_by_id("confirmation")
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(first_name.is_enabled() 
        and lastname.is_enabled() 
        and email.is_enabled() 
        and passw.is_enabled()
        and confirm.is_enabled()
        and submit_button.is_enabled())

        first_name.send_keys("umi")
        lastname.send_keys("maito")
        email.send_keys("umi@umi.com")
        passw.send_keys("Buenastardes_mi_nombre_es_rogelio")
        confirm.send_keys("Buenastardes_mi_nombre_es_rogelio")
        submit_button.click()
        
    
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)