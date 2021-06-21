import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DinamicElement(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/disappearing_elements")


    def test_dinamic_element(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()
            for i in range(1,menu+1):
                try:
                    option = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i}]/a')
                    options.append(option.text)
                    print(options)
                except:
                    print(f"The option number {i} was not found ")
                    tries += 1
                    driver.refresh()
        
        print(f"finished in {tries} tries")


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)