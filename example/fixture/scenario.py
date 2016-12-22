# -*- coding: utf-8 -*-

class ScenarioHelper:


    def __init__(self, app):

        self.app = app

    def add_to_cart_random_product(self):
        self.app.MainPage.open_start_page()
        self.app.MainPage.open_random_product_page()
        self.app.ProductPage.select_size_if_needed()
        self.app.ProductPage.add_product_to_cart()

    def delete_all_products_from_cart(self):
        self.app.MainPage.open_start_page()
        self.app.MainPage.open_cart_page()
        self.app.CartPage.delete_all_products_from_cart()