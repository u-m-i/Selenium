# Import all the tools for the testing
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class Hello(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = "/home/umi/Documents/Projects/PY/test_2/chromedriver/chromedriver")
        driver = cls.driver
        driver.implicitly_wait(10)


    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')
        driver.find_element_by_id("search")


    def test_visit_wiki(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reports', report_name="hello_report" ))
