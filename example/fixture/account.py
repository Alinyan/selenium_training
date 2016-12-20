# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountHelper:

    def __init__(self, app):
        self.app = app

    def login(self, email, password):
        self.app.navigation.open_start_page()
        # Input usename
        self.app.wd.find_element_by_name("email").send_keys("%s" % email)
        # Input password
        self.app.wd.find_element_by_name("password").send_keys("%s" % password)
        # Click submit
        self.app.wd.find_element_by_name("login").click()

    def create_account(self, user):
        self.app.navigation.open_create_account_page()
        self.app.wd.find_element_by_name("firstname").send_keys("%s" % user.firstname)
        self.app.wd.find_element_by_name("lastname").send_keys("%s" % user.lastname)
        self.app.wd.find_element_by_name("address1").send_keys("%s" % user.address1)
        self.app.wd.find_element_by_name("postcode").send_keys("%s" % user.postcode)
        self.app.wd.find_element_by_name("city").send_keys("%s" % user.city)
        self.app.wd.find_element_by_name("email").send_keys("%s" % user.email)
        self.app.wd.find_element_by_name("phone").send_keys("%s" % user.phone)
        self.app.wd.find_element_by_name("password").send_keys("%s" % user.password)
        self.app.wd.find_element_by_name("confirmed_password").send_keys("%s" % user.password)
        # Click submit
        self.app.wd.find_element_by_name("create_account").click()

    def logout(self):
        self.app.wd.find_element_by_link_text('Logout').click()


