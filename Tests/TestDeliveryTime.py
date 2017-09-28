# -*- coding: utf8 -*-
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


    def test_check_auto_delivery_time(self):
        self.calcPage.input_country_name(self.driver, "Беларусь")
        self.calcPage.set_auto_delivery_mode(self.driver)
        self.actual = self.calcPage.get_delivery_time(self.driver)
        self.expected = '30 - 35 ДНЕЙ'
        self.assertEqual(self.actual, self.expected)

    def test_check_train_delivery_time(self):
        self.calcPage.input_country_name(self.driver, "Беларусь")
        self.calcPage.set_train_delivery_mode(self.driver)
        self.actual = self.calcPage.get_delivery_time(self.driver)
        self.expected = '19 - 24 ДНЕЙ'
        self.assertEqual(self.actual, self.expected)

    def test_check_plane_delivery_time(self):
        self.calcPage.input_country_name(self.driver, "Беларусь")
        self.calcPage.set_plane_delivery_mode(self.driver)
        self.actual = self.calcPage.get_delivery_time(self.driver)
        self.expected = '12 - 17 ДНЕЙ'
        self.assertEqual(self.actual, self.expected)
    #calcPage.input_weight(driver, "10")
    #calcPage.get_cost(driver)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()