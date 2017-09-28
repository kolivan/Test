# -*- coding: utf8 -*-
from selenium import webdriver
from Pages.CalculatePage import CalculatePage


class Test():

    driver = webdriver.Firefox()
    driver.get('http://annodanini.it-devgroup.com/')
    driver.implicitly_wait(15)
    calcPage = CalculatePage()

    calcPage.input_text(calcPage.selectedCountry, "Беларусь".decode('utf-8'))
