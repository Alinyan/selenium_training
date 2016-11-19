# -*- coding: utf-8 -*-
class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_start_page(self):
        self.app.wd.get(self.app.baseURL)

