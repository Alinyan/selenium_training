# -*- coding: utf-8 -*-
from selenium import webdriver
from navigation import NavigationHelper
from session import SessionHelper


class Application:

    def __init__(self, browser, web_conf):
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
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.baseURL = web_conf['baseURL']
        self.loginURL = web_conf['loginURL']
        self.username = web_conf['username']
        self.password = web_conf['password']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

