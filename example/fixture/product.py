# -*- coding: utf-8 -*-
import random
from model.product import Product
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def create(self, product):
        self.app.navigation.open_catalog_page()
        self.app.wd.find_element_by_link_text('Add New Product').click()
        # Заполнение вкладки General
        random.choice(self.app.wd.find_elements_by_name("status")).click()
        self.app.wd.find_element_by_name("name[en]").send_keys("%s" % product.name)
        self.app.wd.find_element_by_name("code").send_keys("%s" % product.code)
        random.choice(self.app.wd.find_elements_by_name("product_groups[]")).click()
        self.app.wd.find_element_by_name("quantity").clear
        self.app.wd.find_element_by_name("quantity").send_keys("%s" % product.quantity)
        random.choice(self.app.wd.find_elements_by_name("quantity_unit_id")).click()
        random.choice(self.app.wd.find_elements_by_name("delivery_status_id")).click()
        random.choice(self.app.wd.find_elements_by_name("sold_out_status_id")).click()
        # переход на вкладку Information
        self.app.wd.find_element_by_link_text('Information').click()
        # заполнение вкладки Information
        random.choice(self.app.wd.find_elements_by_name("manufacturer_id")).click()
        random.choice(self.app.wd.find_elements_by_name("supplier_id")).click()
        self.app.wd.find_element_by_name("keywords").send_keys("%s" % product.keywords)
        self.app.wd.find_element_by_name("short_description[en]").send_keys("%s" % product.short_description)
        self.app.wd.find_element_by_class_name("trumbowyg-editor").send_keys("%s" % product.description)
        self.app.wd.find_element_by_name("head_title[en]").clear
        self.app.wd.find_element_by_name("head_title[en]").send_keys("%s" % product.head_title)
        self.app.wd.find_element_by_name("meta_description[en]").clear
        self.app.wd.find_element_by_name("meta_description[en]").send_keys("%s" % product.meta_description)
        # переход на вкладку Prices
        self.app.wd.find_element_by_link_text('Prices').click()
        # заполнение вкладки Prices
        self.app.wd.find_element_by_name("purchase_price").clear
        self.app.wd.find_element_by_name("purchase_price").send_keys("%s" % product.purchase_price)
        random.choice(self.app.wd.find_elements_by_name("purchase_price_currency_code")).click()
        random.choice(self.app.wd.find_elements_by_name("tax_class_id")).click()
        self.app.wd.find_element_by_name("prices[USD]").send_keys("%s" % product.pricesUSD)
        self.app.wd.find_element_by_name("prices[EUR]").send_keys("%s" % product.pricesEUR)
        # переход на вкладку General
        self.app.wd.find_element_by_link_text('General').click()
        # Сохранение товара
        save_button = self.app.wd.find_element_by_name("save")
        ActionChains(self.app.wd).move_to_element(save_button).click_and_hold().release().perform()
        # Confirm title
        WebDriverWait(self.app.wd, 30).until(EC.title_is('Catalog | My Store'))

    def get_product_list(self):
        self.app.navigation.open_catalog_page()
        product_list = []
        products = self.app.wd.find_elements_by_css_selector(".row td:nth-child(3) a")
        for product in products:
            product_list.append(Product(name=product.text.encode('utf-8')))
        return product_list

    def get_count_product(self, product):
        self.app.navigation.open_catalog_page()
        products = self.app.wd.find_elements_by_link_text("%s" % product.name)
        return len(products)

