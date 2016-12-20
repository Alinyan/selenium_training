# -*- coding: utf-8 -*-
from model.country import Country
from model.geozone import Geozone

def test_login(app):
    app.session.login(app.username, app.password)

def test_click_left_elements_of_menu_and_check_header(app):
    app.session.login(app.username, app.password)
    app.navigation.click_left_elements_of_menu_and_check_header()

def test_check_sticker_product(app):
    app.session.login(app.username, app.password)
    app.navigation.open_start_page()
    app.check.check_count_sticker_product()

def test_check_sorting_countries(app):
    app.session.login(app.username, app.password)
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
    app.session.login(app.username, app.password)
    app.navigation.open_geozones_page()
    country_list = app.geozone.get_country()
    for country in country_list:
        zone_list = app.geozone.get_zone_list_for_country(country.name)
        sorted_zone_list = sorted(zone_list, key=Geozone.name_geozone)
        assert sorted_zone_list == zone_list