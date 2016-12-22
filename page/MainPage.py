# -*- coding: utf-8 -*-
import random


class MainPageHelper:


    def __init__(self, app):
        self.app = app

    def open_start_page(self):
        self.app.wd.get(self.app.baseURL)

    def open_random_product_page(self):
        random.choice(self.app.wd.find_elements_by_css_selector(".image-wrapper")).click()

    def open_cart_page(self):
        self.app.wd.find_element_by_css_selector("#cart .link").click()
