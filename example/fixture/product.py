# -*- coding: utf-8 -*-

class ProductHelper:

    products_cache = None

    def __init__(self, app):
        self.app = app

    def get_first_product_name_from_main_page(self):
        name_product = self.app.wd.find_element_by_css_selector("#box-campaigns .name").text
        return name_product

    def get_first_product_regular_price_from_main_page(self):
        return self.app.wd.find_element_by_css_selector("#box-campaigns .regular-price").text

    def get_first_product_campaign_price_from_main_page(self):
        return self.app.wd.find_element_by_css_selector("#box-campaigns .campaign-price").text

    def get_first_product_name_from_product_page(self):
        return self.app.wd.find_element_by_tag_name("h1").text

    def get_first_product_regular_price_from_product_page(self):
        return self.app.wd.find_element_by_css_selector(".regular-price").text

    def get_first_product_campaign_price_from_product_page(self):
        return self.app.wd.find_element_by_css_selector(".campaign-price").text

    def get_style_campaign_price_from_main_page(self, property):
        return self.app.wd.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property(property)

    def get_style_regular_price_from_main_page(self, property):
        return self.app.wd.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property(property)

    def get_style_campaign_price_from_product_page(self, property):
        return self.app.wd.find_element_by_css_selector(".campaign-price").value_of_css_property(property)

    def get_style_regular_price_from_product_page(self, property):
        return self.app.wd.find_element_by_css_selector(".regular-price").value_of_css_property(property)