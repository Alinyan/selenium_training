# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPageHelper:

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)


    def delete_all_products_from_cart(self):
        count_products = len(self.app.wd.find_elements_by_class_name('shortcut'))
        for i in range(count_products - 1):
            element_in_table = self.app.wd.find_elements_by_css_selector(".dataTable tr td.item")[0]
            self.app.wd.find_elements_by_css_selector(".shortcut a")[0].click()
            self.app.wd.find_element_by_name("remove_cart_item").click()
            self.wait.until(EC.staleness_of(element_in_table))
        self.app.wd.find_element_by_name("remove_cart_item").click()
        self.wait.until(EC.staleness_of(element_in_table))

