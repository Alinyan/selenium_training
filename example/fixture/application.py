# -*- coding: utf-8 -*-
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium import webdriver
from navigation import NavigationHelper
from session import SessionHelper
from check import CheckHelper
from country import CountryHelper
from geozone import GeozoneHelper
from product import ProductHelper
from account import AccountHelper
from listener import ListenerHelper


class Application:

    def __init__(self, browser, web_conf):
        if browser == "firefox":
            self.wd = EventFiringWebDriver(webdriver.Firefox(), ListenerHelper())
        elif browser == "chrome":
            self.wd = EventFiringWebDriver(webdriver.Chrome(), ListenerHelper())
        elif browser == "ie":
            self.wd = EventFiringWebDriver(webdriver.Ie(), ListenerHelper())
        elif browser == "opera":
            self.wd = EventFiringWebDriver(webdriver.Opera(), ListenerHelper())
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.check = CheckHelper(self)
        self.country = CountryHelper(self)
        self.geozone = GeozoneHelper(self)
        self.product = ProductHelper(self)
        self.account = AccountHelper(self)
        self.adminURL = web_conf['adminURL']
        self.baseURL = web_conf['baseURL']
        self.username = web_conf['username']
        self.password = web_conf['password']
        self.wd.implicitly_wait(10)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
