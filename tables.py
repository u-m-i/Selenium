import unittest
from selenium import webdriver

class TableTest(unittest.TestCase):

    def setUp(self) -> None:
        
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/tables")

    
    def test_sort_table(self):
        driver = self.driver
        
        table_data = [[] for i in range(7)]

        for i in range(1,7):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i}]/span')
            table_data[i].append(header.text)

            for j in range(4):

                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{j+1}]')
                table_data[i].append(row_data.text)

        print(table_data)


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)