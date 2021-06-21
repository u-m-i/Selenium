import unittest
from selenium import webdriver
from pageobject import  GooglePage   

class GTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")

    
    def test_search(self):
        google = GooglePage(self.driver)
        google.open_site()
        google.search("Testimonios de mujeres que abortaron")

        self.assertEqual("Testimonios de mujeres que abortaron", google.keyword)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)