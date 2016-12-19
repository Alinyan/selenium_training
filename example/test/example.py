# -*- coding: utf-8 -*-

def test_login(app):
    app.session.login(app.username, app.password)

def test_click_left_elements_of_menu_and_check_header(app):
    app.session.login(app.username, app.password)
    app.navigation.click_left_elements_of_menu_and_check_header()

def test_check_sticker_product(app):
    app.session.login(app.username, app.password)
    app.navigation.open_start_page()
    app.navigation.check_count_sticker_product()
