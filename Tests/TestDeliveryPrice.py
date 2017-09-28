from selenium import webdriver
import unittest
from Pages.CalculatePage import CalculatePage


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://annodanini.it-devgroup.com/')
        self.driver.implicitly_wait(15)
        self.calcPage = CalculatePage()
        self.calcPage.click_country_dropdown(self.driver)


    def test_check_auto_delivery_price_15(self):
        self.calcPage.input_country_name(self.driver, "Беларусь")
        self.calcPage.set_auto_delivery_mode(self.driver)
        self.calcPage.input_weight(self.driver, '15')
        self.actual = self.calcPage.get_price(self.driver)
        self.expected = 15*4.3
        self.assertEqual(self.actual, self.expected)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()