# -*- coding: utf8 -*-
from selenium import webdriver
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class CalculatePage(BasePage):

    driver = webdriver.Firefox()

    def __init__(self, driver):
        super(CalculatePage).__init__(driver)

    country = driver.find_element_by_class_name('select2-selection__arrow')

    selectedCountry = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']")))

    deliveryModeAuto = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Авто")]')))

    deliveryModeTrain = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Ж/Д")]')))

    deliveryModePlane = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Авиа")]')))

    deliveryTime = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//li[1]/p/span[@class="js_delivery_time"]')))

    deliveryPrice = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//li[3]/p/span[@class="js_price_delivery"]')))

    weight = driver.find_elements_by_xpath('//div[@class="input-box"][2]/input[@class="valid"]')

    def input_text(self, locator, input):
        locator.send_keys(input)

    def send_enter(self, locator):
        locator.send_keys(Keys.ENTER)

    def click_element(self, locator):
        locator.click()

    def get_text(self, locator):
        locator.text






