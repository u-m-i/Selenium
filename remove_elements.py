import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddElement(unittest.TestCase):

    def setUp(self) -> None:
        
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")


    def test_add_five(self):
        driver = self.driver

        elements_to_add = int(input("How many elements will you add? : "))
        elements_to_remove = int(input("How many elements will you remove? : "))

        total_elements = elements_to_add - elements_to_remove

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        WebDriverWait(driver, 10)

        for i in range(1, elements_to_add+1):
            add_button.click()

        delete_button = driver.find_element_by_class_name("added_manually")

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(delete_button))

        for i in range(1, elements_to_remove+1):
            try:
                delete_button.click()
            
            except:
                print("You're tried to delete more elements that the existent")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There are zero elements on screen")

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "added-manually")))

        return 0


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
