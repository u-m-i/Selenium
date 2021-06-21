import unittest
from selenium import webdriver

class TyposCheck(unittest.TestCase):

    def setUp(self) -> None:
        
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/typos")

    
    def test_find_typo(self):

        driver = self.driver

        sentence_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        
        extract = sentence_to_check.text

        self.assertTrue(extract)

        tries = 1
        found = False
        template_text = "Sometimes you'll see a typo, other times you won't."

        while extract != template_text:

            sentence_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            extract = sentence_to_check.text
            driver.refresh()

        while not found:

            if extract == template_text:

                tries += 1
                driver.refresh()
                found = True

        self.assertEqual(found,True)
        print(f"Took {tries} tries to find the typo.")


    def tearDown(self) -> None:
        
        self.driver.quit()


if __name__ == '__main__':

    unittest.main(verbosity=2)