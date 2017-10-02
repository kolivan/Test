from selenium import webdriver
import unittest
from Pages.CalculatePage import CalculatePage
from ddt import ddt, data


@ddt
class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://annodanini.it-devgroup.com/')
        self.driver.implicitly_wait(15)
        self.calcPage = CalculatePage()
        self.calcPage.click_country_dropdown(self.driver)


    @data((0, '0,00'),(15, '64,50'), (150, '645,00'), (151, '573,80'), (300, '240,00'),(301, '240,80'))# в этот тест добавляешь все значения, которые надо проверить
    def test_check_auto_delivery_price_15_150(self,value):
        a,b = value
        self.calcPage.input_country_name(self.driver, "Беларусь")
        self.calcPage.set_auto_delivery_mode(self.driver)
        self.calcPage.input_weight(self.driver, a)
        self.driver.implicitly_wait(15)
        self.actual = self.calcPage.get_price(self.driver)
        #self.actual1 = self.calcPage.get_cost(self.driver)
        self.expected = b
        self.assertEqual(self.actual, self.expected)
        #self.assertEqual(self.actual1, self.expected)



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()