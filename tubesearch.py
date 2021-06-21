import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TubeTest(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:

        cls.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = cls.driver
        driver.get("https://www.youtube.com")
        driver.maximize_window()


    def test_search_jacob(self):

        driver = self.driver

        search_field = driver.find_element_by_xpath('//*[@id="search"]')
        search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')

        search_field.send_keys("Ágila arpía versus oso perezoso")
        search_button.click()
        driver.implicitly_wait(20)


    def test_search_umi(self):

        driver = self.driver

        search_field = driver.find_element_by_xpath('//*[@id="search"]')
        search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
        
        search_field.send_keys("How to become a data scientist")
        search_button.click()
    
        video = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Why You Probably Won't Become a Data Scientist")))
    
        video.click()
        sleep(9)
        duration = driver.find_element_by_xpath('//*[@id="movie_player"]/div[32]/div[2]/div[1]/div[1]/span[3]')
        totalduration = duration.text

        WebDriverWait(driver, totalduration).until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="movie_player"]/div[32]/div[2]/div[1]/div[1]/span[1]'), totalduration))


    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(20)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
