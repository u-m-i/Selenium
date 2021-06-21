import csv,unittest
from ddt import ddt,data,unpack
from selenium import webdriver

def get_data(file_name):

    row_number = []
    data_file = open(file_name, "r")
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        row_number.append(row)
    return row_number


@ddt
class DataDrivenTest(unittest.TestCase):

    def setUp(self) -> None:

        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")


    @data(*get_data("testdata.csv"))
    @unpack
    def test_search_ddt(self, search_value, expect_result):
        
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        expect_result = int(expect_result)
        
        if expect_result > 0:
            self.assertEqual(expect_result, len(products))
        else:
            message = driver.find_elements_by_class_name("note-msg")
            self.assertEqual("Your search returns no results", message)
        
        print(f"Just found {len(products)} products")

    
            
        print(f"Found {len(products)} produtcs")

        for product in products:
            print(product.text)

        


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)