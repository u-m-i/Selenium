import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class SelectLanguage(unittest.TestCase):

    def setUp(self) -> None:

        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
    

    def test_select_language(self):

        lang_exp = ['English', "French", "German"]
        lang_options = []

        selected_lang = Select(self.driver.find_element_by_id("select-language"))
        self.assertEqual(3, len(selected_lang.options))

        for option in selected_lang.options:
            lang_options.append(option.text)

        self.assertListEqual(lang_options, lang_exp)

        self.assertEqual('English', selected_lang.first_selected_option.text)

        selected_lang.select_by_visible_text("German")

        self.assertTrue('store=german' in self.driver.current_url)

        selected_lang = Select(self.driver.find_element_by_id("select-language"))
        selected_lang.select_by_index(0)
        


    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)