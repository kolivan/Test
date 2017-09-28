# -*- coding: utf8 -*-
from selenium import webdriver

class BasePage():

    driver = webdriver.Firefox()

    def __init__(self, driver):
        self.driver = driver

    def openPage(self, url):
        self.driver.get(url)

