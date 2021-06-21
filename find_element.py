import unittest
from selenium import webdriver

class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_search_field(self):
        search_field = self.driver.find_element_by_id("search")
    

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")
    
    def test_count_of_promo_banner(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def test_vp_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/ul/li[1]/a/img')


    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("#header > div > div.skip-links > div > div > a > span.icon")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
