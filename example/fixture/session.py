# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username="admin", password="admin"):
        self.app.navigation.open_start_page()
        # Input usename
        self.app.wd.find_element_by_name("username").send_keys("admin")
        # Input password
        self.app.wd.find_element_by_name("password").send_keys("admin")
        # Click submit
        self.app.wd.find_element_by_name("login").click()
        # Confirm login
        WebDriverWait(self.app.wd, 10).until(EC.title_is("My Store"))