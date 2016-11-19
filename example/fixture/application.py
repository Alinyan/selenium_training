# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.navigation import NavigationHelper


class Application:

    def __init__(self, browser, baseURL, web_username, web_password):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "opera":
            self.wd = webdriver.Opera()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd = webdriver.Ie()
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.baseURL = baseURL
        self.username = web_username
        self.password = web_password

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

