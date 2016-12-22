# -*- coding: utf-8 -*-
from selenium.webdriver.support.events import AbstractEventListener


class ListenerHelper(AbstractEventListener):


    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)
