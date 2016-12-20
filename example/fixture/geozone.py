# -*- coding: utf-8 -*-
from model.country import Country
from model.geozone import Geozone


class GeozoneHelper:

    geozone_cache = None
    country_cache = None

    def __init__(self, app):
        self.app = app

    def get_country(self):
        if self.country_cache is None:
            self.country_cache = []
            for element in self.app.wd.find_elements_by_class_name("row"):
                cells = element.find_elements_by_tag_name("td")
                country = cells[2].text.encode('utf-8')
                self.country_cache.append(Country(name=country))
            return list(self.country_cache)

    def get_zone_list_for_country(self, name_country):
        zone_list = []
        self.app.wd.find_element_by_link_text("%s" % name_country).click()
        for element in self.app.wd.find_elements_by_xpath("//table[@id='table-zones']/tbody/tr[not(@*)]"):
            options = element.find_elements_by_xpath("td[3]/select/option")
            for option in options:
                if option.get_attribute('selected'):
                    zone = option.get_attribute('text').encode('utf-8')
                    zone_list.append(Geozone(name=zone))
        self.app.navigation.open_geozones_page()
        return zone_list

