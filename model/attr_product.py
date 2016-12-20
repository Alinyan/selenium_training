# -*- coding: utf-8 -*-

class Geozone:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price


    def __repr__(self):
        return "%s" \
               % (self.name)

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name)

    def name_geozone(self):
        return self.name


