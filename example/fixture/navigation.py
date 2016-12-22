# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        self.app.wd.get(self.app.adminURL)

    def open_start_page(self):
        self.app.wd.get(self.app.baseURL)

    def open_countries_page(self):
        self.app.wd.get('http://localhost:8585/litecart/admin/?app=countries&doc=countries')

    def open_geozones_page(self):
        self.app.wd.get('http://localhost:8585/litecart/admin/?app=geo_zones&doc=geo_zones')

    def open_catalog_page(self):
        self.app.wd.find_element_by_css_selector("#app-:nth-child(2)").click()  # кликаем на элемент
        self.app.wd.find_element_by_css_selector("#doc-catalog").click()  # кликаем на элемент

    def open_page_of_creating_country(self):
        self.app.navigation.open_countries_page()
        self.app.wd.find_element_by_css_selector("#content .button").click()

    def open_create_account_page(self):
        self.app.wd.get('http://localhost:8585/litecart/en/create_account')

    def open_first_campaign_product_page(self):
        self.app.wd.find_element_by_css_selector("#box-campaigns .link").click()

    def click_left_elements_of_menu_and_check_header(self):
        # проходим цикл по всем пунктам меню
        for index in range(len(self.app.wd.find_elements_by_id("app-"))):
            index = index + 1    # увеличиваем индекс, так как список начинается с 1
            self.app.wd.find_element_by_xpath("//li[@id='app-'][%s]/a" % index).click()  # кликаем на элемент
            assert self.are_elements_present(self.app.wd, By.TAG_NAME, 'h1') == 1   # проверяем наличие заголовка на странице
            xpath_inserted_list = "//li[@id='app-'][%s]/ul/li" % index     # формирование xpath для вложенного цикла
            if self.are_elements_present(self.app.wd, By.XPATH, xpath_inserted_list):   # проверяем количество элментов по сформированному xpath
                # если элементов > 0, то выполянем цикл по вложенным пунктам меню
                for n in range(len(self.app.wd.find_elements_by_xpath(xpath_inserted_list))):
                    n = n + 1    # увеличиваем индекс, так как список начинается с 1
                    self.app.wd.find_element_by_xpath("//li[@id='app-'][%s]/ul/li[%s]/a" % (index, n)).click()   # кликаем на каждый элемент пункта меню
                    assert self.are_elements_present(self.app.wd, By.TAG_NAME, 'h1') == 1     # проверяем наличие заголовка на странице

    def are_elements_present(self, driver, *args):
        """ Проверка наличия элемента"""
        return len(driver.find_elements(*args)) > 0