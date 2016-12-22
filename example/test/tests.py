# -*- coding: utf-8 -*-
from model.country import Country
from model.geozone import Geozone
from webcolors import *
import random
from model.account import Account
from model.product import Product

def test_login(app):
    app.session.login_to_admin(app.username, app.password)

def test_click_left_elements_of_menu_and_check_header(app):
    app.session.login_to_admin(app.username, app.password)
    app.navigation.click_left_elements_of_menu_and_check_header()

def test_check_sticker_product(app):
    app.navigation.open_start_page()
    app.check.check_count_sticker_product()

def test_check_sorting_countries(app):
    app.session.login_to_admin(app.username, app.password)
    app.navigation.open_countries_page()
    country_list = app.country.get_country()
    sorted_country_list = sorted(country_list, key=Country.name_country)
    assert sorted_country_list == country_list
    for country in country_list:
        if country.count_zones != '0':
            zone_list = app.country.get_zone_list_for_county(country.name)
            sorted_zone_list = sorted(zone_list, key=Geozone.name_geozone)
            assert sorted_zone_list == zone_list

def test_check_sorting_geozones(app):
    app.session.login_to_admin(app.username, app.password)
    app.navigation.open_geozones_page()
    country_list = app.geozone.get_country()
    for country in country_list:
        zone_list = app.geozone.get_zone_list_for_country(country.name)
        sorted_zone_list = sorted(zone_list, key=Geozone.name_geozone)
        assert sorted_zone_list == zone_list

def test_check_product_page(app):
    app.navigation.open_start_page()
    # переход на страницу со всеми товарами
    name_from_main_page = app.product.get_first_product_name_from_main_page()
    regular_price_from_main_page = app.product.get_first_product_regular_price_from_main_page()
    campaign_price_from_main_page = app.product.get_first_product_campaign_price_from_main_page()
    color_regular_price_from_main_page = app.product.get_style_regular_price_from_main_page('color')
    color_campaign_price_from_main_page = app.product.get_style_campaign_price_from_main_page('color')
    text_style_regular_price_from_main_page = app.product.get_style_regular_price_from_main_page('text-decoration')
    text_style_campaign_price_from_main_page = app.product.get_style_campaign_price_from_main_page('font-weight')
    # переход на страницу товара
    app.navigation.open_first_campaign_product_page()
    name_from_from_product_page = app.product.get_first_product_name_from_product_page()
    regular_price_from_product_page = app.product.get_first_product_regular_price_from_product_page()
    campaign_price_from_product_page = app.product.get_first_product_campaign_price_from_product_page()
    color_regular_price_from_product_page = app.product.get_style_regular_price_from_product_page('color')
    color_campaign_price_from_product_page = app.product.get_style_campaign_price_from_product_page('color')
    text_style_regular_price_from_product_page = app.product.get_style_regular_price_from_product_page('text-decoration')
    text_style_campaign_price_from_product_page = app.product.get_style_campaign_price_from_product_page('font-weight')
    # проверки
    assert name_from_main_page == name_from_from_product_page
    assert regular_price_from_main_page == regular_price_from_product_page
    assert campaign_price_from_main_page == campaign_price_from_product_page
    assert color_regular_price_from_main_page == 'rgba(119, 119, 119, 1)'
    assert color_regular_price_from_product_page == 'rgba(102, 102, 102, 1)'
    assert color_campaign_price_from_main_page == 'rgba(204, 0, 0, 1)'
    assert color_campaign_price_from_product_page == 'rgba(204, 0, 0, 1)'
    assert text_style_regular_price_from_main_page == 'line-through'
    assert text_style_campaign_price_from_main_page == '900'
    assert text_style_regular_price_from_product_page == 'line-through'
    assert text_style_campaign_price_from_product_page == '700'

def test_create_new_user_and_logout(app):
    char = string.ascii_letters + string.hexdigits  # символы для генерации
    email = "".join([random.choice(char) for i in range(random.randrange(15))])+"@mail.ru"
    password = '123456789'
    app.account.create_account(Account(firstname='Aleksandr', lastname='Ivanov', address1='Lenina 5', city='Spb',
                                       postcode='190000', email=email, phone='88001234567', password=password))
    app.account.logout()
    app.account.login(email=email, password=password)
    app.account.logout()

def test_add_new_product(app):
    char = string.ascii_letters + string.hexdigits  # символы для генерации
    name = "".join([random.choice(char) for i in range(15)])
    added_product = Product(name=name, code='1234546', quantity='5,75', keywords='qwerty1',
                 description='qwerty qwerty', head_title='qwerty2', short_description='qwerty3', meta_description='qwerty4', purchase_price='1456',
                 pricesUSD='1495', pricesEUR='1460')
    app.session.login_to_admin(app.username, app.password)
    list_old = app.product.get_product_list()
    app.product.create(added_product)
    list_new = app.product.get_product_list()
    list_old.append(added_product)
    count = app.product.get_count_products(added_product)
    assert len(list_old) == len(list_new)
    assert count == 1

def test_working_with_cart(app):
    app.product.add_to_cart_random_product()    # добавляем первый случайный продукт в корзину
    app.product.add_to_cart_random_product()    # второй случайный продукт
    app.product.add_to_cart_random_product()    # третий случай продукт
    app.product.delete_all_products_from_cart()   # удаляем поочередно все продукты из корзины

def test_checking_link_for_opening_in_new_window(app):
    app.session.login_to_admin(app.username, app.password)
    app.navigation.open_page_of_creating_country()
    app.country.check_opening_external_links_in_new_window()

def test_check_log_of_browser(app):
    app.session.login_to_admin(app.username, app.password)
    app.navigation.open_catalog_page()
    logs = app.product.get_logs_browser_all_products()
    assert logs == []

def test_page_object_working_with_cart(app):
    app.scenario.add_to_cart_random_product()    # добавляем первый случайный продукт в корзину
    app.scenario.add_to_cart_random_product()    # второй случайный продукт
    app.scenario.add_to_cart_random_product()    # третий случай продукт
    app.scenario.delete_all_products_from_cart()   # удаляем все продукты из корзины