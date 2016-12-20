# -*- coding: utf-8 -*-

class Country:
    def __init__(self, id=None, name=None, count_zones=None):
        self.id = id
        self.name = name
        self.count_zones = count_zones

    def __repr__(self):
        return "%s" \
               % (self.id, self.name)

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name)

    def name_country(self):
        return self.name


