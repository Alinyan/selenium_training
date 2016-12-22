# -*- coding: utf-8 -*-
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPageHelper:

    products_cache = None

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def select_size_if_needed(self):
        if self.app.navigation.are_elements_present(self.app.wd, By.CLASS_NAME, 'options'):
            random.choice(self.app.wd.find_elements_by_xpath("//*[@class='options']/*/option[not(@selected)]")).click()

    def add_product_to_cart(self):
        old_count = self.app.wd.find_element_by_css_selector("span.quantity").text.encode('utf-8')
        self.app.wd.find_element_by_name("add_cart_product").click()
        new_count = int(old_count) + 1
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"), str(new_count)))
