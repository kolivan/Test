# -*- coding: utf8 -*-
from selenium import webdriver
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class CalculatePage(BasePage):

    def __init__(self):
        super(CalculatePage).__init__()

    def click_country_dropdown(self, driver):
        return driver.find_element_by_class_name('select2-selection__arrow').click()

    def input_country_name(self, driver, input):
        WebDriverWait(driver, 2)\
            .until(EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']")))\
            .send_keys(input, Keys.ENTER)

    def set_auto_delivery_mode(self, driver):
        WebDriverWait(driver, 5)\
            .until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Авто")]')))\
            .click()

    def set_train_delivery_mode(self, driver):
        WebDriverWait(driver, 5)\
            .until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Ж/Д")]')))\
            .click()

    def set_plane_delivery_mode(self, driver):
        WebDriverWait(driver, 5)\
            .until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Авиа")]')))\
            .click()

    def get_delivery_time(self, driver):
        return WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[1]/p/span[@class="js_delivery_time"]'))).text

    def input_weight(self, driver, weight):
        driver.find_element_by_xpath('//div[@class="input-box"][2]/input[@name="weight"]').send_keys(weight)

    def get_cost(self, driver):
        return WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div/p/span[@class="js_total_cost"]'))).text

    def get_price(self, driver):
        return WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[3]/p/span[@class="js_price_delivery"]'))).text
